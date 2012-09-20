def asterix():
    """Prints a textbox with a nice asterix frame"""
    print("*" * (len(text) + 4))
    print("* " + text + " *")
    print("*" * (len(text) + 4))

text = input("Mata in en text: ")	#prompts the user to input something
asterix()				#Calls the asterix function
