'''
Steve is inputting a new password to protect his system.  The network supervisor will force Steve to choose a password that is strong.  To be considered a ‘strong’ password, Steve must have the following elements:
•	Password must be at least 8 characters in length
•	Password cannot contain a space
•	Password must contain either ‘#’ or ‘@’ somewhere at least once.
•	Password cannot have repeated consecutive repeated letters
Program must repeatedly loop until a valid password is entered.
The user will enter a password.  Your program must tell them if it is acceptable or not. 
'''

condition = True

while condition:
    password = input('Enter a password: ')
    
    size = len(password)
    
    symbol1 = password.count('#')
    symbol2 = password.count('@')
    
    symbols = symbol1 + symbol2
    
    space = password.count(' ')
    
    repeated = False
    
    for i in range(size - 1):
        if password[i] == password[i + 1]:
            repeated = True

    if size >= 8 and space == 0 and symbols > 0 and repeated == False:
        print('This is acceptable, program terminating')
        condition = False
    else:
        print('This is unacceptable, try again')



        
        
