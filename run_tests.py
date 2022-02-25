def return_10():
    return 10

def add(number_1, number_2):
    return number_1 + number_2

def subtract(number_1, number_2):
    return number_1 - number_2

def multiply(number_1, number_2):
    return number_1 * number_2

def divide(number_1, number_2):
    return number_1 / number_2

def length_of_string(string):
    return len(string)

def join_string(string1, string2):
    return string1 + string2

def add_string_as_number(string1, string2):
    return int(string1) + int(string2)

def number_to_full_month_name(number):
    months_of_year = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return months_of_year[number - 1]

def number_to_short_month_name(number):
    short_months_of_year = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    return short_months_of_year[number - 1]

def volume_of_cube(side):
    return side ** 3

def reverse_string(string):
    return string[::-1]

def fahrenheit_to_celsius(number):
    return ((number - 32) * 5%9)


# (32°F − 32) × 5/9 = 0°C
# fahrenheit_to_celsius
