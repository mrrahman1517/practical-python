# sears.py

bill_thikness = 0.11 * 0.001
sears_height = 442
num_bills = 1
day = 1

while num_bills * bill_thikness < sears_height:
    print(day, num_bills, num_bills * bill_thikness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thikness)

name = input('Enter your name: ')
print('Hello', end = ' ')
print('My name is', name)