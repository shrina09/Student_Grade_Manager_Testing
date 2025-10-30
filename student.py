# Used to find the median of the number
import statistics


# Object Sudent
class Student:
    # Takes in the name and the grade of the students
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    # Gives the average of the grades of students
    def get_avg(self):
        """ Gives the average of the student grades"""

        grade = list(map(int, self.grades))
        average = sum(grade) / len(grade)
        return average

    # Gives the highest of the grades of students
    def get_highest(self):
        """ Gives the highest of the student grades"""

        return max(self.grades, key=int)

    # Gives the lowest of the grades of students
    def get_lowest(self):
        """ Gives the lowest of the student grades"""

        return min(self.grades, key=int)

    # Gives the highest of the grades of students
    def get_median(self):
        """ Gives the median of the student grades"""

        return statistics.median(self.grades)
