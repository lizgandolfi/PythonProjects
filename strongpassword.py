'''
Steve is inputting a new password to protect his system.  The network supervisor will force Steve to choose a password that is strong.  To be considered a ‘strong’ password, Steve must have the following elements:
•	Password must be at least 6 characters in length
•	Password cannot contain a space
•	Password must contain either ‘#’ or ‘@’ somewhere at least once.
The user will enter a password.  Your program must tell them if it is acceptable or not.  Program must display "This is unacceptable" or "This is acceptable" at the end.
'''

pw = input('Enter a password: ')

if len(pw) < 6:
    print('This is unacceptable')
elif pw.find(' ') > 0:
    print('This is unacceptable')
elif pw.find('#') < 0 and pw.find('@'):
    print('This is unacceptable')
else:
    print('This is acceptable')
