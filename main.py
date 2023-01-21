class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_score(self):
        total = 0
        len_total = 0
        for row in list(self.grades.values()):
            total += sum(row)
            len_total += len(row)
        return round(total / len_total, 2)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задание: {self.average_score()}\n' \
              f'Курсы в процессе изучения: {self.courses_in_progress}\n' \
              f'Завершенные курсы: {self.finished_courses}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            return ('Это не студент')
        return self.average_score() < other.average_score()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_score(self):
        total = 0
        len_total = 0
        for row in list(self.grades.values()):
            total += sum(row)
            len_total += len(row)
        return round(total / len_total, 2)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {self.average_score()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return ('Это не лектор')
        return self.average_score() < other.average_score()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

def average_score_students(students_list, course):
    sum_avarage = 0
    counter = 0
    for stud in students_list:
        if course in stud.grades:
            sum_avarage += sum(stud.grades[course])
            counter += len(stud.grades[course])
        else:
            return f'По данному курсу у студентов нет оценок'
    return round(sum_avarage / counter, 2)

def average_score_lectors(lectors_list, course):
    sum_avarage = 0
    counter = 0
    for lector in lectors_list:
        if course in lector.grades:
            sum_avarage += sum(lector.grades[course])
            counter += len(lector.grades[course])
        else:
            return f'По данному курсу еще не было лекций'
    return round(sum_avarage / counter, 2)




best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Architecture']


awesome_student = Student('Barni', 'Stinson','male')
awesome_student.courses_in_progress += ['Python']
awesome_student.courses_in_progress += ['Architecture']


cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Architecture']


sweet_reviewer = Reviewer('Marshall', 'Erikson')
sweet_reviewer.courses_attached += ['Python']
sweet_reviewer.courses_attached += ['Architecture']

cool_lecturer = Lecturer('Lili', 'Oldrin')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Architecture']

verycool_lecturer = Lecturer('Lili', 'Pad')
verycool_lecturer.courses_attached += ['Python']
verycool_lecturer.courses_attached += ['Architecture']

best_student.rate_hw(cool_lecturer, 'Python', 8)
best_student.rate_hw(cool_lecturer, 'Python', 7)
best_student.rate_hw(cool_lecturer, 'Architecture', 7)
best_student.rate_hw(cool_lecturer, 'Architecture', 5)
best_student.rate_hw(verycool_lecturer, 'Python', 5)
best_student.rate_hw(verycool_lecturer, 'Python', 7)
best_student.rate_hw(verycool_lecturer, 'Architecture', 8)
best_student.rate_hw(verycool_lecturer, 'Architecture', 6)

awesome_student.rate_hw(cool_lecturer, 'Python', 5)
awesome_student.rate_hw(cool_lecturer, 'Python', 6)
awesome_student.rate_hw(cool_lecturer, 'Architecture', 4)
awesome_student.rate_hw(cool_lecturer, 'Architecture', 9)
awesome_student.rate_hw(verycool_lecturer, 'Python', 6)
awesome_student.rate_hw(verycool_lecturer, 'Python', 4)
awesome_student.rate_hw(verycool_lecturer, 'Architecture', 5)
awesome_student.rate_hw(verycool_lecturer, 'Architecture', 3)

cool_reviewer.rate_hw(awesome_student, 'Python', 2)
cool_reviewer.rate_hw(awesome_student, 'Python', 4)
cool_reviewer.rate_hw(awesome_student, 'Architecture',7)
cool_reviewer.rate_hw(awesome_student, 'Architecture',9)
cool_reviewer.rate_hw(best_student, 'Python', 6)
cool_reviewer.rate_hw(best_student, 'Python', 4)
cool_reviewer.rate_hw(best_student, 'Architecture', 9)
cool_reviewer.rate_hw(best_student, 'Architecture', 3)

sweet_reviewer.rate_hw(awesome_student, 'Python', 2)
sweet_reviewer.rate_hw(awesome_student, 'Python', 6)
sweet_reviewer.rate_hw(awesome_student, 'Architecture',7)
sweet_reviewer.rate_hw(awesome_student, 'Architecture',9)
sweet_reviewer.rate_hw(best_student, 'Python', 6)
sweet_reviewer.rate_hw(best_student, 'Python', 4)
sweet_reviewer.rate_hw(best_student, 'Architecture', 9)
sweet_reviewer.rate_hw(best_student, 'Architecture', 3)

my_student_list = [best_student,awesome_student ]
my_lecturer_list = [verycool_lecturer,cool_lecturer]

print(best_student)
print(awesome_student)
print(cool_lecturer)
print(verycool_lecturer)
print(cool_reviewer)
print(sweet_reviewer)

print(average_score_students(my_student_list, 'Architecture'))
print(average_score_lectors(my_lecturer_list, 'Architecture'))


