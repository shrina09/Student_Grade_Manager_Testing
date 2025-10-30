# Shrina, P
# Sorts the student grades from the student_grades.csv file according to user input of average, highest, lowest and median and writes it in the sorted_grades.csv.

# Allows the student.py to be used (allows acess) and the Student object in it
from student import Student

# Allows to use csv reader and writer
import csv


# Merge sort for the average of student grades
def merge_sort_avg(arr):
    """ Merge sort for the average of student grades.

  Keyword argument:
  arr -- student grades
  """
    size = len(arr)
    if size > 1:
        middle = size // 2

        # Allows the grades to be splited into first half and second half from the middle
        left = arr[:middle]
        right = arr[middle:]

        # Recursive call of left and right from the middle of the array (allows to sort them)
        merge_sort_avg(left)
        merge_sort_avg(right)

        p = 0
        q = 0
        r = 0
        # Length of left and right side of the grades
        left_s = len(left)
        right_s = len(right)

        # Sorting it
        while p < left_s and q < right_s:
            #.get_avg() allows to use that function in Student class so the merge sort sorts it for average of student grades
            if left[p].get_avg() < right[q].get_avg():
                arr[r] = left[p]
                p += 1
            else:
                arr[r] = right[q]
                q += 1
            r += 1

        while p < left_s:
            arr[r] = left[p]
            p += 1
            r += 1

        while q < right_s:
            arr[r] = right[q]
            q += 1
            r += 1


# Merge sort for the highest of student grades
def merge_sort_high(arr):
    """ Merge sort for the highest of student grades.

  Keyword argument:
  arr -- student grades
  """
    size = len(arr)
    if size > 1:
        middle = size // 2

        # Allows the grades to be splited into first half and second half from the middle
        left = arr[:middle]
        right = arr[middle:]

        # Recursive call of left and right from the middle of the array (allows to sort them)
        merge_sort_high(left)
        merge_sort_high(right)

        p = 0
        q = 0
        r = 0
        # Length of left and right side of the grades
        left_s = len(left)
        right_s = len(right)

        # Sorting it
        while p < left_s and q < right_s:
            #.get_highest() allows to use that function in Student class so the merge sort sorts it for the highest of student grades
            if (int(left[p].get_highest())) < (int(right[q].get_highest())):
                arr[r] = left[p]
                p += 1
            else:
                arr[r] = right[q]
                q += 1

            r += 1

        while p < left_s:
            arr[r] = left[p]
            p += 1
            r += 1

        while q < right_s:
            arr[r] = right[q]
            q += 1
            r += 1


# Merge sort for the lowest of student grades
def merge_sort_low(arr):
    """ Merge sort for the lowest of student grades.

  Keyword argument:
  arr -- student grades
  """
    size = len(arr)
    if size > 1:
        middle = size // 2

        # Allows the grades to be splited into first half and second half from the middle
        left = arr[:middle]
        right = arr[middle:]

        # Recursive call of left and right from the middle of the array (allows to sort them)
        merge_sort_low(left)
        merge_sort_low(right)

        p = 0
        q = 0
        r = 0
        # Length of left and right side of the grades
        left_s = len(left)
        right_s = len(right)

        # Sorting it
        while p < left_s and q < right_s:
            #.get_lowest() allows to use that function in Student class so the merge sort sorts it for the lowest of student grades
            if (int(left[p].get_lowest())) < (int(right[q].get_lowest())):
                arr[r] = left[p]
                p += 1

            else:
                arr[r] = right[q]
                q += 1
            r += 1

        while p < left_s:
            arr[r] = left[p]
            p += 1
            r += 1

        while q < right_s:
            arr[r] = right[q]
            q += 1
            r += 1


# Merge sort for the median of student grades
def merge_sort_median(arr):
    """ Merge sort for the median of student grades.

  Keyword argument:
  arr -- student grades
  """
    size = len(arr)
    if size > 1:
        middle = size // 2

        # Allows the grades to be splited into first half and second half from the middle
        left = arr[:middle]
        right = arr[middle:]

        # Recursive call of left and right from the middle of the array (allows to sort them)
        merge_sort_median(left)
        merge_sort_median(right)

        p = 0
        q = 0
        r = 0
        # Length of left and right side of the grades
        left_s = len(left)
        right_s = len(right)

        # Sorting it
        while p < left_s and q < right_s:
            #.get_median() allows to use that function in Student class so the merge sort sorts it for the median of student grades
            if (int(left[p].get_median())) < (int(right[q].get_median())):
                arr[r] = left[p]
                p += 1
            else:
                arr[r] = right[q]
                q += 1
            r += 1

        while p < left_s:
            arr[r] = left[p]
            p += 1
            r += 1

        while q < right_s:
            arr[r] = right[q]
            q += 1
            r += 1


# For writing the sorted_grades.csv file
def Write_file(students):
    """For writing the sorted_grades.csv file."""

    with open('sorted_grades.csv', 'w', newline='') as csv_file:
        words = csv.writer(csv_file)
        # writes the first line
        words.writerow(["Name,A0,A1,A2,A3,A4,A5,A6"])

        # loops through all of the students with their grades and names
        for i in students:
            # allows to put a comma after the name
            row = i.name + ','
            for t in i.grades:
                # allows to put a comma after each grade
                row += str(t) + ','
            (words.writerow([row]))


# For user input and reading the student_grades.csv file
def main():
    """For user input and reading the student_grades.csv file."""

    # Making an empty list where all the students name and grades can fill it
    students = []

    # Reading the student_grades.csv file
    with open('student_grades.csv') as csv_file:
        text = csv.reader(csv_file)
        # Skips the first line so the grades can be read
        next(text)

        # Takes all the grades and puts in the students list
        for row in text:
            student = Student(row[0], row[1:])
            students.append(student)

        # User input on how they want to sort the student grades
        speak = input(
            "how would you like to sort it (avg for average, high for highest, low for lowest and median for median): "
        )

        # Calls the appropritate function according to the user input
        # Calls for the average function
        if speak == "avg":
            merge_sort_avg(students)

        # Calls for the highest function
        elif speak == "high":
            merge_sort_high(students)

        # Calls for the lowest function
        elif speak == "low":
            merge_sort_low(students)

        # Calls for the median function
        elif speak == "median":
            merge_sort_median(students)
        Write_file(students)


# Name guard
# runs main() function the first
if __name__ == '__main__':
    main()
