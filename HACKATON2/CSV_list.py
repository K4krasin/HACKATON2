from Students_message import get_message
def open_csv():
    with open('students.csv', encoding='UTf-8') as fopen:
        stud = fopen.readlines()
        stud = stud[1:len(stud)]

    return stud

def clear_csv(csv_of_students):
    student = []
    students = []
    for i in range(0,len(csv_of_students)):
        student = csv_of_students[i]
        student = (student.split(';'))
        students.append(student)

    for i in range(0, len(students)):
        task = students[i].pop(-2)
        task = int(task)
        students[i].append(task)

    for i in range(0, len(students)):
        grade = students[i].pop(-2)
        grade = int(grade)
        students[i].append(grade)

    return students





def main():

    list_of_studensts = open_csv()
    students = clear_csv(list_of_studensts)
    print(students)
    get_message(students)



if __name__ == '__main__':
    main()
