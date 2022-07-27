if __name__ == '__main__':
    scoresheet = []
    for n in range(int(input())):
        name = input()
        score = float(input())
        scoresheet.append([name, score])
    li = []
    for i in scoresheet:
        li.append(i[1])
    li = set(li)
    li.remove(min(li))
    second_min_score = min(li)
    second_lowest_grade_student = []
    for i in scoresheet:
        if i[1] == second_min_score:
            second_lowest_grade_student.append(i[0])
    name = sorted(second_lowest_grade_student)
    for i in range(0, len(name)):
        print(name[i])

