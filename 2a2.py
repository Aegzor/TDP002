"""Tihi"""

def make_triangle(num):
    """Prints a triangle with the height of the input number"""
    for v in range(1, (num + 1)):
        print (' ' * (num - v) + '*' * (2 * v - 1) + ' ' * (num - v))

def triangle():
    """Prompts the user to input a value, if value isn't an integer... ask the 
    user to try again"""
    number_of_rows = input('Ange ett heltal: ')
    while number_of_rows.isdigit() == False:
        number_of_rows = input('Värdet du angav var inte ett heltal, försök igen: '
                            )
 
    number_of_rows = int(number_of_rows)	#Converts the number to an int
    make_triangle(number_of_rows)		#Calls the make_triangle function

triangle()	#Calls the triangle function
