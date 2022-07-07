'''
Write a Python program to find the surface area of a rectangular prism.  
The length, height and width should be all user input integers.
'''

lenght = int(input('Enter length ===>'))
width = int(input('Enter width ===>'))
height = int(input('Enter height ===>'))

lw = (lenght * width)
lh = (lenght * height)
wh = (width * height)

area = 2 * (lw + lh + wh)

print('\nSA of this prism is', area)



