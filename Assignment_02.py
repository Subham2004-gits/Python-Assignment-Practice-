
scores = int(input('Enter the marks'))

if scores >= 90 :
    grade = 'A'
elif scores >= 80:
    grade = 'B'
elif scores >= 70:
    grade = 'C'
elif scores >= 60:
    grade = 'D'
else:
    grade = 'F'

print("the grade is :",grade)