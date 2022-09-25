from typing import Any, Dict, List
import pandas as pd
import mlflow
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from prefect import task, flow

@task
def load_data(path:str) -> pd.DataFrame:
    data =  pd.read_csv(path)
    return data

@task
def split_data(input_:pd.DataFrame,output_:pd.Series,test_data_ratio:float)->Dict[str,Any]:
    X_tr,X_te,y_tr,y_te=train_test_split(input_,output_,test_size=test_data_ratio,random_state=0)
    return {'X_TRAIN':X_tr,'Y_TRAIN':y_tr,'X_TEST':X_te,'Y_TEST':y_te}

@task
def get_scaler(data: pd.DataFrame) -> Any:
    scaler = StandardScaler()
    scaler.fit(data)
    return scaler

@task
def rescale_data(data: pd.DataFrame, scaler: Any) -> pd.DataFrame:    
    data_rescaled = pd.DataFrame(scaler.transform(data), 
                                columns = data.columns, 
                                index = data.index)
    return data_rescaled

@task
def label_encoder_train(data:pd.DataFrame) -> Any:
    X_train_cat_le = pd.DataFrame(index=data.index)
    
    cut_encoder = {'Fair' : 1, 'Good' : 2, 'Very Good' : 3, 'Ideal' : 4, 'Premium' : 5}
    X_train_cat_le['cut'] = data['cut'].apply(lambda x : cut_encoder[x])

    color_encoder = {'J':1, 'I':2, 'H':3, 'G':4, 'F':5, 'E':6, 'D':7}
    X_train_cat_le['color'] = data['color'].apply(lambda x : color_encoder[x])
    
    clarity_encoder = {'I1':1, 'SI2':2, 'SI1':3, 'VS2':4, 'VS1':5, 'VVS2':6, 'VVS1':7, 'IF':8}
    X_train_cat_le['clarity'] = data['clarity'].apply(lambda x : clarity_encoder[x])
    
    return X_train_cat_le

@task
def label_encoder_test(data:pd.DataFrame)->Any:
    X_test_cat_le = pd.DataFrame(index=data.index)
    
    cut_encoder = {'Fair' : 1, 'Good' : 2, 'Very Good' : 3, 'Ideal' : 4, 'Premium' : 5}
    X_test_cat_le['cut'] = data['cut'].apply(lambda x : cut_encoder[x])

    color_encoder = {'J':1, 'I':2, 'H':3, 'G':4, 'F':5, 'E':6, 'D':7}
    X_test_cat_le['color'] = data['color'].apply(lambda x : color_encoder[x])
    
    clarity_encoder = {'I1':1, 'SI2':2, 'SI1':3, 'VS2':4, 'VS1':5, 'VVS2':6, 'VVS1':7, 'IF':8}
    X_test_cat_le['clarity'] = data['clarity'].apply(lambda x : clarity_encoder[x])
    
    return X_test_cat_le

@task
def find_best_model(X_train: pd.DataFrame, y_train: pd.Series, estimator: Any, parameters: List) -> Any:
    # Enabling automatic MLflow logging for scikit-learn runs
    mlflow.sklearn.autolog(max_tuning_runs=None)

    with mlflow.start_run():        
        reg_model = GridSearchCV(
            estimator=estimator, 
            param_grid=parameters, 
            scoring='neg_mean_squared_error',
            cv=5,
            return_train_score=True,
            verbose=1
        )
        reg_model.fit(X_train, y_train)
        
        # Disabling autologging
        mlflow.sklearn.autolog(disable=True)
        
        return reg_model


# Workflow

@flow
def my_flow(path:str = './data/diamonds.csv'):
    
    mlflow.set_tracking_uri("sqlite:///mlflow.db")
    mlflow.set_experiment("Diamond Price prediction")

    # parameters
    TAGET_COL = 'price'
    TEST_DATA_RATIO = 0.2
    DATA_PATH = path
    
    # load the data 
    df = load_data(path = DATA_PATH)
    
    #Identifying X and y
    target_data = df[TAGET_COL]
    input_data = df.drop([TAGET_COL], axis = 1) 

    # split the data
    train_test_dict = split_data(input_=input_data,output_=target_data,test_data_ratio=TEST_DATA_RATIO)

    # get the scaler
    #Resscaling Train and Test Data on numerical features
    scaler=get_scaler(train_test_dict['X_TRAIN'].select_dtypes(include=['int64', 'float64']))
    train_test_dict['X_TRAIN_num']=rescale_data(data=train_test_dict['X_TRAIN'].select_dtypes(include=['int64', 'float64']),scaler=scaler)
    train_test_dict['X_TEST_num']=rescale_data(data=train_test_dict['X_TEST'].select_dtypes(include=['int64', 'float64']),scaler=scaler)

    #Labeling the train data
    label=label_encoder_train(train_test_dict['X_TRAIN'].select_dtypes(include=['object']))
    
    #Concatenating training data
    X_train_transformed = pd.concat([train_test_dict['X_TRAIN_num'], label], axis=1)
    
    #Lable encoding on test data
    label1=label_encoder_test(train_test_dict['X_TEST'].select_dtypes(include=['object']))
    
    #Concatenating test data
    X_test_transformed=pd.concat([train_test_dict['X_TEST_num'], label1], axis=1)

    #find the best model

    ESTIMATOR=KNeighborsRegressor()
    HYPERPARAMETERS = [{'n_neighbors':[i for i in range(1, 51)], 'p':[1, 2]}]
    
    regressor=find_best_model(X_train_transformed,train_test_dict['Y_TRAIN'],ESTIMATOR,HYPERPARAMETERS)
    print(regressor.best_params_)
    print(regressor.best_score_)

    # run the my_flow function
# my_flow('./data/diamonds.csv') 

#we can run this if we want to run the file instantly

# to schedule the flow
from prefect.deployments import Deployment
from prefect.orion.schemas.schedules import IntervalSchedule
from datetime import timedelta

deployment = Deployment.build_from_flow(            
    flow = my_flow,                                           
    name = "model_training",
    schedule = IntervalSchedule(interval=timedelta(days=7)),
    work_queue_name = "mlflow"
)

deployment.apply()