import statistics

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        result_str = f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.__average_grade()}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return result_str    

    def  __average_grade(self):
        gradeList = []
        for value in self.grades.values():
            gradeList += value
        if len(gradeList):
            return round(statistics.mean(gradeList),1)           
        else:
            return 0
   
    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        return (self.__average_grade()) < (other.__average_grade())        

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []   
        self.grades = {} 

    def __str__(self):
        result_str = f'Имя: {self.name}\n' \
        f'Фамилия: {self.surname}\n' \
        f'Средняя оценка за лекции: {self.__average_grade()}'
        return result_str

    def  __average_grade(self):
        gradeList = []
        for value in self.grades.values():
            gradeList += value
        if len(gradeList):
            return round(statistics.mean(gradeList),1)            
        else:
            return 0
        
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        return (self.__average_grade()) < (other.__average_grade())

class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []    

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        print(student.grades)
   
    def __str__(self):
        result_str = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result_str
        
def average_grade_student(students, course):
    gradeList = []  
    for student in students:
        if isinstance(student, Student):
            for key, value in student.grades.items():
                if (key == course):
                    gradeList += value
    if len(gradeList):
         return round(statistics.mean(gradeList),1)           
    else:
         return 0
            
def average_grade_lecturer(lecturers , course):
    gradeList = []  
    for lector in lecturers:
        if isinstance(lector, Lecturer):
            for key, value in lector.grades.items():
                if (key == course):
                    gradeList += value
    if len(gradeList):
        return round(statistics.mean(gradeList),1)           
    else:
        return 0

student1 = Student('Олег', 'Васильев', 'male')
student1.courses_in_progress += ['Python', 'Матан','Дифференциальные уравнения']
student1.finished_courses += ['Дифференциальные уравнения', 'ФА']
student2 = Student('Анжела', 'Лойко', 'female')
student2.courses_in_progress += ['Python', 'Матан', 'Дифференциальные уравнения','C++']
student3 = Student('Иван', 'Петров', 'male')
student3.courses_in_progress += ['Python', 'ФА']
student4 = Student('Петр', 'Иванов', 'male')
student4.courses_in_progress += ['Python', 'ФА']

lecturer1 = Lecturer('Олег', 'Булыгин')
lecturer1.courses_attached += ['Python', 'ФА', 'C++']
lecturer2 = Lecturer('Анжелина', 'Джоли')
lecturer2.courses_attached += ['Матан', 'ФА', 'Python','Дифференциальные уравнения']

reviewer1 = Reviewer('Олег', 'Булыгин')
reviewer1.courses_attached += ['Python']
reviewer2 = Reviewer('Владимир', 'Зеленский')
reviewer2.courses_attached += ['JavaScript','Матан']
reviewer3 = Reviewer('Анжелина', 'Джоли')
reviewer3.courses_attached += ['ФА', 'Матан','Python']

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 4)
reviewer2.rate_hw(student1, 'Матан', 9)
reviewer3.rate_hw(student2, 'Python', 9)
reviewer3.rate_hw(student2, 'Python', 8)
reviewer3.rate_hw(student3, 'Python', 8)
reviewer3.rate_hw(student3, 'Python', 3)
reviewer3.rate_hw(student3, 'Python', 9)

student1.rate_lecturer(lecturer1, 'Python', 10)
student2.rate_lecturer(lecturer1, 'ФА', 7)
student3.rate_lecturer(lecturer1, 'ФА', 4)
student3.rate_lecturer(lecturer2, 'Python', 6)

print(student1)
print(student2)
print(student3)
print(student4)

print(reviewer1)
print(reviewer2)
print(reviewer3)

print(lecturer1)
print(lecturer2)

print(f'Средняя оценка лектора {lecturer1.name} {lecturer1.surname} меньше\n'\
f'cредней оценки лектора {lecturer2.name} {lecturer2.surname} {lecturer1 < lecturer2}')  
print(f'Первый студент меньше второго {student1 < student3}')

print(f"Средняя оценка студентов по курсу Python {average_grade_student([student1, student2, student3],'Python')}")
print(f"Средняя оценка лекторов по курсу Python {average_grade_lecturer([lecturer1, lecturer2],'Python')}")
