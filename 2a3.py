def make_flag(size):
    """prints a neat little (dependant on user input) flag)"""
    print(('*' * (10 * size) +  ' ' * (2 * size) + '*' * (10 * size)
           + ('\n')) * 4)
    print(('*' * (10 * size) +  ' ' * (2 * size) + '*' * (10 * size)
           + ('\n')) * 4)

def flag():
    """Prompts the user to input a value, if value isn't an integer... ask the 
    user to try again"""
    width = input('Skriv ett heltal, få en flagga: ')
    while width.isdigit() == False:
        width = input('Värdet du angav var inte ett heltal, försök igen: '
                            )
 
    width = int(width)			#Converts the number to an int
    make_flag(width)			#Calls make_triangle()

flag()		#Calls flag()
