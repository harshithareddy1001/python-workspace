
# def hello(name):
#     print("Hello",name)
# hello("Harshi")


# def greet_people(name,title):
#     print("Hello",title,name)
# greet_people("harshi","ms")


# def sum(a,b):
#     return(a+b)
# result=sum(10,20)
# print(result)

# a="10"
# b="20"
# c=20
# print(a+b)
"""
Program: Student Utility Program
Purpose: Demonstrate how to define and call functions in Python
"""

def greet_student(name):
    """
    Function to greet a student.
    """
    print(f"Hello {name}, welcome to the Python class!")


def calculate_total(marks):
    """
    Function to calculate total marks.
    """
    return sum(marks)


def calculate_average(total, count):
    """
    Function to calculate average marks.
    """
    return total / count


def check_result(average):
    """
    Function to determine pass or fail.
    """
    if average >= 40:
        return "PASS"
    return "FAIL"


def display_result(name, marks):
    """
    Main function that calls other functions.
    """
    total = calculate_total(marks)
    average = calculate_average(total, len(marks))
    result = check_result(average)

    greet_student(name)
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", average)
    print("Result:", result)

if __name__ == "__main__":
    name = "Upasana"
    marks = [65, 70, 55, 80, 60]
    display_result(name,marks)

