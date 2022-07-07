'''
Mr. Crenshaw needs to compute what a student needs to achieve on the final exam to receive an 'A' in his class.  An 'A' is a grade of at least a 90.
Students will enter their first 9 weeks grade (counts as 40%) and their second 9 weeks grade (counts as 40%).  
The program must compute the minimum score of the final exam (counts as 20%) to achieve an 'A'. 
'''

grade1 = int(input('Enter first nine weeks grade:'))
grade2 = int(input('Enter second nine weeks grade:'))

currentgrade = ((0.4 * grade1) + (0.4 * grade2))/0.8

finalgrade = ((90-((1-0.2)*currentgrade))/0.2)

print('The final grade needed for an A is:',finalgrade)



