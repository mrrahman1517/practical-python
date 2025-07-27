# mortgage.py
#
# Exercise 1.7

# mortgage.py

principal = 815660.0
rate = 0.05
one_time_payments = 1000
payment = 4206 + one_time_payments
total_paid = 0.0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    print('current principal remaining', principal)

print('Total paid', total_paid)
