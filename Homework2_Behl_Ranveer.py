from cmath import pi
import math

# Q1
Day_of_week = 'Tuesday, '
Month = 'September'
Day_of_month = '12, '
Year = '2023'

print(Day_of_week, Month, Day_of_month, Year)

#Q2
quote = 'The newscaster said, “And Now for Something Completely Different!”\n\n'"One quote: '"', Two quotes “, Red Quotes, Blue Quotes'

print(quote)

#Q3
print('5' + '4') # here both values are not integers so thier ascii values 52 and 53 are added, this equals 54 as both values add to the next ascii number, 54.
print(5 + 4) # this give the correct integer math as both values are integers.

ouput = int('5') + int('4')
print(ouput)

#Q4
#a
output = ((5*5)/5)-5
print(output)
#b
output = (5-5)**(5*5)
print(output)
#c
output = ((60-40)*1.5)+((5**2)-25)
print(output)

#6
quaters = 543/25
nickels = (543%25)/5
pennies = ((543%25)%5)/5

print(quaters, 'Quaters,', nickels, 'Nickels,', pennies, 'Pennies,')

#7
def average(num1, num2, num3):
    return (num1+num2+num3)/3

print(average(5,12,15))

#8
def print_and_repeat(args):
    print('You entered: \n')
    print(args, '\n')
    for i in range(3):
        print(args, end=' ')
    print('\n')

print_and_repeat('hello')

#9
def sum_of_avgs(avg1, avg2):
    return avg1+avg2

print(sum_of_avgs(average(10,12,15),average(100,2,13)))

#10
def compute_biorythems(age_in_days):
    phys = math.sin((2*pi*age_in_days)/23)
    emo = math.sin((2*pi*age_in_days)/28)
    int = math.sin((2*pi*age_in_days)/33)

    print(f"Physical: {phys:.2f}", f"Emotional: {emo:.2f}", f"Intellectual: {int:.2f}")

print(compute_biorythems(22130))