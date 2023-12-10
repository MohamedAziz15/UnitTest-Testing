import unittest
import pytest 

class Student:
    def __init__(self, id, name, gender, degree):
        self.id = id
        self.name = name
        self.gender = gender
        self.degree = [degree]


class program:
    def __init__(self):
        self.students = [
            Student(1, "Ahmed", "male", [94, 83, 72, 56, 98]),
            Student(4, "Aml", "Female", [60, 89, 65, 74, 55]),
            Student(3, "Donia", "Female", [80, 95, 93, 97, 98]),
            Student(2, "Mohamed", "male", [80, 84, 87, 90, 68]),
            Student(5, "Ali", "male", [49, 55, 30, 50, 48])
        ]

    def all_students(self):
        return self.students

    def get_details(self, student_id):
        return [std for std in self.students if std.id == student_id]

    def add_user(self, student_id, name, gender, degree):
        if not student_id or not name:
            return "Student ID or Name couldn't be empty"
        else:
            self.students.append(Student(int(student_id), name, gender, degree))
            return "Success"

    def delete_user(self, student_id, name):
        for student in self.students:
            if student.id == student_id and student.name == name:
                self.students.remove(student)
                return "Success"
        return "Fail"

    @staticmethod
    def total_result(degrees):
        return sum(degrees)

    @staticmethod
    def grade(degrees):
        result = program.total_result(degrees)
        percentage = (result / 500) * 100
        if percentage >= 85:
            return "Excellent"
        elif 85 > percentage >= 75:
            return "Very Good"
        elif 75 > percentage >= 50:
            return "Good"
        else:
            return "Fail"

# class TEST:
#     def test_get_details():
#         # Test get_details method
#         student_id_to_find = 3
#         ss = program()
#         details = ss.get_details(student_id_to_find)
#         assert details.name == "Donia" 



if __name__ == "__main__":
    std = Student(6,"Aziz","male",[98, 97, 96, 95, 94])
    ss = program()
    print(ss.add_user(6,"Aziz","male",[98, 97, 96, 95, 94]))

    # result = ss.test_get_details()
    # print(result)
    # unittest.main()















