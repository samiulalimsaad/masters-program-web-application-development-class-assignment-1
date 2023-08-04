# task-1 variable manipulation
def task_1_variable_manipulation():
    name = "Saad"
    age = 25

    print(f"My name is {name} and I am {age} years old")  # print the values


# task-2 data types and types conversion
def task_2_data_types_and_types_conversion():
    num1 = 11
    num2 = 11.11
    num1_float = float(num1)  # Convert num1 to a floating-point number
    num2_int = int(num2)  # Convert num2 to an integer

    print(f"type: {type(num1)}\tvalue: {num1}")
    print(f"type: {type(num2)}\tvalue: {num2}")
    print(f"type: {type(num1_float)}\tvalue: {num1_float}")
    print(f"type: {type(num2_int)}\tvalue: {num2_int}")


# task-3 string manipulation
def task_3_string_manipulation():
    sentence = '"Python programming is fun!"'

    print(f"sentence length = {len(sentence)}")
    print(f"8'th character  = {sentence[7]}")

    substr = sentence[:6]  # Extract substring from index 0 to 5 (exclusive)
    print(f"substring of 0 to 5  = {substr}")

    new_sentence = sentence + " I enjoy it!"  # Concatenate two strings
    print(f"new sentence  = {new_sentence}")


# task-4 List and List manipulation
def task_4_list_and_list_manipulation():
    fruits = ["apple", "banana", "cherry", "date"]
    fruits.append("grape")  # Add "grape" to the end of the list
    fruits.remove("banana")  # Remove "banana" from the list
    print(f"length = {len(fruits)}")

    sliced_fruits = fruits[2:4]  # Slice elements from index 2 to 3 (exclusive)
    extra_fruits = ["kiwi", "lemon"]

    combined_fruits = sliced_fruits + extra_fruits  # Concatenate two lists
    print(f"fruits = {combined_fruits}")


# task-5 Conditional statement
def task_5_conditional_statement():
    num = 6
    if num % 2:
        print("odd")
    else:
        print("even")


# task-6 Loops
def task_6_loops():
    for i in range(1, 11):
        print(i)
    sum = 0
    for i in range(1, 101):
        sum += i
    print(f"Sum = {sum}")


# Task 7: Functions
def calculate_square(number):
    return number * number


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return "Not a prime Number"
    return "Prime Number"


print(calculate_square(7))  # Call calculate_square() function with argument 7
print(is_prime(29))  # Call is_prime() function with argument 29


# Task 8: Dictionaries
def task_8_dictionaries():
    student = {
        "name": "saad",
        "age": 25,
        "grade": "A+",
    }
    student[
        "course"
    ] = "Web Application Development"  # Add a new key-value pair to the dictionary
    print(student)

    for i in student:
        print(f"{i}: {student[i]}")


task_1_variable_manipulation()  # Call task 1
task_2_data_types_and_types_conversion()  # Call task 2
task_3_string_manipulation()  # Call task 3
task_4_list_and_list_manipulation()  # Call task 4
task_5_conditional_statement()  # Call task 5
task_6_loops()  # Call task 6
task_8_dictionaries()  # Call task 8
