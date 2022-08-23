import code
import streamlit as st


st.title("Welcome o My DashBoard!")

st.header("This is a header")

st.subheader("This is a subheader")

st.markdown("This is the markdown")

st.text("This is the text")

code_snippet = """

st.title("Welcome o My DashBoard!")

st.header("This is a header")

st.subheader("This is a subheader")

st.markdown("This is the test")

st.text("This is the text")

"""
# show code if user hits the button
button_click = st.button("Show code for the current page")
# button returns the boolean value
if button_click == True:
    st.code(code_snippet)
