# class Student:
#     def __init__(self,name, surname, school_class, grade, missing):
#         self.name = name
#         self.surname = surname
#         self.scholl_class = school_class
#         self.grade = grade
#         self.missing = missing
#
#     def show_students(self):
#         print(self.name, self.surname, self.scholl_class, self.grade, self.missing)



def student_creator():
    student = []
    while True:
        try:
            student_class = input("Podaj klasę ucznia: ")
            name = input("Podaj imię ucznia: ")
            surname = input("Podaj nazwisko ucznia: ")
            grade = int(input("Podaj ocenę ucznia: "))
            missing = int(input("Podaj ilość brakujących zadań ucznia: "))
            return name, surname, student_class, grade, missing
        except ValueError:
            print("To musi być liczba")

    return student.append(student_class, name, surname, grade,missing)

def get_message(students):

    date = '25.06.2022'
    for s in students:
        mess = f'Welcome {s[1]} {s[2]},\n ' \
               f'This is a kindly reminder that you have {s[4]} tasks left to submit before you can graduate\n'\
               f'Your current grade is {s[3]} and can increase to {s[3] + 1} if you submit all assignments before the due date {date}.'

        with open(f'student_msg_{s[1]}', 'w', encoding='UTF-8') as f:
            f.write(mess)

    return mess



def main():

    student1 = student_creator()
    student2 = student_creator()
    student3 = student_creator()
    students = [student1, student2, student3]


    get_message(students)


if __name__ == '__main__':
    main()
