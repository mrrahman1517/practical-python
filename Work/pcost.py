# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
    f = open(filename, 'rt')
    headers = next(f)
    print(headers)
    total_cost = 0
    for line in f:
        row = line.split(',')
        print(row)
        try:
            shares = int(row[1])
            price = float(row[2])
            total_cost += shares * price
        except ValueError:
            print('formatting error, continuing ...')
            continue
    return total_cost

print('Total cost ', portfolio_cost('Data/portfolio.csv'))
