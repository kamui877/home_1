class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_l(self, lecturer, course, grade):
        if grade not in range(11):
            return 'Ошибка'
        elif isinstance(lecturer,
                        Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_rate(self):
        sum_1 = 0
        sum_2 = 0
        for val in self.grades.values():
            for rate in val:
                sum_1 += 1
                sum_2 += rate
        return sum_2 / sum_1

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self._average_rate()}" \
               f"\nКурсы в процессе изучения: {self.courses_in_progress[0]}, {self.courses_in_progress[1]}" \
               f"\nЗавершенные курсы: {self.finished_courses[0]}"

    def __lt__(self, any_student):
        if isinstance(any_student, Student):
            return self._average_rate().__lt__(any_student._average_rate())


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_rate(self):
        sum_1 = 0
        sum_2 = 0
        for val in self.grades.values():
            for rate in val:
                sum_1 += 1
                sum_2 += rate
        return sum_2 / sum_1

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self._average_rate()}"

    def __lt__(self, any_lecturer):
        if isinstance(any_lecturer, Lecturer):
            return self._average_rate().__lt__(any_lecturer._average_rate())


class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


lecturer_1 = Lecturer("James", "Jhonson")
lecturer_2 = Lecturer("Frenk", "Ross")

stud_1 = Student("Rick", "Even", "male")
stud_2 = Student("Anna", "Mark", "famale")

rev_1 = Reviewer("Carl", "Smith")
rev_2 = Reviewer('Lisa', "Clark")

rev_1.courses_attached.append('Python')
rev_2.courses_attached.append('Java')

lecturer_1.courses_attached.append('Python')
lecturer_2.courses_attached.append('Java')

stud_1.finished_courses.append('Git')
stud_2.finished_courses.append('Git')

stud_1.courses_in_progress.append('Python')
stud_1.courses_in_progress.append('Java')
stud_2.courses_in_progress.append('Java')
stud_2.courses_in_progress.append('Python')

stud_1.rate_l(lecturer_1, 'Python', 6)
stud_1.rate_l(lecturer_2, 'Java', 8)
stud_2.rate_l(lecturer_1, 'Python', 7)
stud_2.rate_l(lecturer_2, 'Java', 9)

rev_1.rate_hw(stud_1, 'Python', 6)
rev_1.rate_hw(stud_2, 'Python', 4)
rev_2.rate_hw(stud_1, 'Java', 3)
rev_2.rate_hw(stud_2, 'Java', 5)


stud_list = [stud_1, stud_2]
lect_list = [lecturer_1, lecturer_2]


def average_students_rate(students, name_curse):
    sum_1 = []
    for student in students:
        for keys, val in student.grades.items():
            if name_curse == keys:
                sum_1 += val
    return sum(sum_1) / len(sum_1)


def average_lecturer_rate(lectors, name_curse):
    sum_1 = []
    for lecturer in lectors:
        for keys, val in lecturer.grades.items():
            if name_curse == keys:
                sum_1 += val
    return sum(sum_1) / len(sum_1)


print(average_students_rate(stud_list, 'Python'))
print(average_lecturer_rate(lect_list, 'Python'))


#print(rev_1)
#print(rev_2)

#print(lecturer_1)
#print(lecturer_2)

#print(stud_1)
#print(stud_2)

#print(stud_1 < stud_2)
#print(lecturer_1 < lecturer_2)
