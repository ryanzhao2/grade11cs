import random
import calendar

names = ['Bryant Manning',
'Rex Wong',
'Jeannie Santiago',
'Shelia Morales',
'Mathew Flowers',
'Alfred Francis',
'Jacob Lawrence',
'Alice Mcguire',
'Brent Schultz',
'Natasha Bush',
'Constance Medina',
'Philip Mack',
'Jana Hunter',
'Edna Porter',
'Ian Lyons',
'Alberta Hicks',
'Rudolph Bell',
'Violet Gardner',
'Lloyd Wilson',
'Pat Sullivan',
'Amy Nichols',
'Ignacio Williams',
'Sabrina May',
'Thelma Fisher',
'Geraldine Watkins']

cities = ['Belgrade', 'Tijuana', 'Hangzhou', 'Qom', 'Rome']

months = 'JanFebMarAprMayJunJulAugSepOctNovDec'

list_students = []

for name in names:

    student = []
    student.append(name)
    student.append(random.choice(cities))
    student.append(calendar.month_name[random.randint(1, 12)])
    student.append(random.randint(1, 30))
    student.append(random.randint(1990, 2005))


    list_students.append(student)


print(list_students)


# example 4
# print matrix of data as a table


for student in list_students:

    print(f'{student[0]:<20} Born in: {student[1]:<10} \
on {student[2]:>10} {student[3]:>2}, {student[4]}')


