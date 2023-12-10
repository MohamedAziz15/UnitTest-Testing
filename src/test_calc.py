import unittest
import pytest 
import Calc
from Calc import Student,program

class TestProgramMethods(unittest.TestCase):

    def test_all_students(self):
        test_program = program()
        stds = test_program.all_students()
        self.assertEqual(len(stds), 5)


    def test_get_details(self):
        test_program = program()
        student_id_to_find = 3
        details = test_program.get_details(student_id_to_find)
        self.assertEqual(details[0].name, "Donia")

    def test_add_user(self):
        test_program = program()
        self.assertEqual(test_program.add_user(6,"Aziz","Male",[99,98,97,96,95]),"Success")


    def test_delete_user(self):
        test_program = program()
        # self.assertEqual(test_program.delete_user(6,"Aziz"),"Success")
        self.assertEqual(test_program.delete_user(1,"Ahmed"),"Success")
        

    # def test_total_result(self):
    #     pass

    def test_grade(self):
        test_program = program()
        std = test_program.get_details(1)
        degrees = list(std[0].degree)
        # print(degrees)
        self.assertEqual(test_program.grade(degrees[0]),"Very Good")
        


if __name__ == "__main__":
    unittest.main()







