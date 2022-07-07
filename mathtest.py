'''
You will create a basic math test for your class.  
There will be five questions.  Each question is worth 20 points.  
After each question is answered, reveal if they got it right or not.  
At the end of the test, reveal their score.
'''

tot= 0

q1 = int(input('What is 8 x 3? '))
if q1 == 24:
    print('That is correct!\n')
    tot += 20
else:
    print('That is incorrect!\n')
    
q2 = int(input('What is 5 + 7? '))
if q2 == 12:
    print('That is correct!\n')
    tot += 20
else:
    print('That is incorrect!\n')

q3 = int(input('What is 30/2? '))
if q3 == 15:
    print('That is correct!\n')
    tot += 20
else:
    print('That is incorrect!\n')

q4 = int(input('What is 7 - (-3)? '))
if q4 == 10:
    print('That is correct!\n')
    tot += 20
else:
    print('That is incorrect!\n')

q5 = int(input('What is 74 + 23? '))
if q5 == 97:
    print('That is correct!\n')
    tot += 20
else:
    print('That is incorrect!\n')
    
print('Your final score: ', tot)



