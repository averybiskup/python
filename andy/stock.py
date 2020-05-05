import random
'''
This program calculates the average interest rates for you invested money with random numbers.
'''

def accrue_interest(cur_balance, rate, years):
    '''
    Returns the new balance when cur_balance is invested for
    specified number of years at specified interest rate.
    '''
    for elapsed_years in range(years):  # For specified number of years..

        cur_balance += cur_balance * rate # Add interest to the balance

    return cur_balance

def range_interest(cur_balance, low, high, y):

    total = 0
    n = 0
    for i in range(0, 10):
        int = random.randrange(low, high)/100
        amt = accrue_interest(cur_balance, int, y)
        total += amt
        n += 1
        print('Illustration #{} You might end up with $ {}'.format(n, amt))
    print('The average of all 10 illustrations is $ {}'.format(total/10))


def getInput():

    init_balance = float(input("Please enter initial balance: $"))
    lowest_roi = int(input("Please enter the lowest rate of return you anticipate for this year: "))
    highest_roi = int(input("Please enter the highest rate of return you anticipate for this year: "))
    length = int(input('How many years will you keep the investment in these stocks: '))



    range_interest(init_balance, lowest_roi, highest_roi, length)

getInput()

'''
EXAMPLE OUTPUT:

Please enter initial balance: $100
Please enter the lowest rate of return you anticipate for this year: -5
Please enter the highest rate of return you anticipate for this year: 10
How many years will you keep the investment in these stocks: 10
Illustration #1 You might end up with $ 162.8894626777441
Illustration #2 You might end up with $ 215.89249972727865
Illustration #3 You might end up with $ 196.71513572895657
Illustration #4 You might end up with $ 134.3916379344122
Illustration #5 You might end up with $ 196.71513572895657
Illustration #6 You might end up with $ 196.71513572895657
Illustration #7 You might end up with $ 162.8894626777441
Illustration #8 You might end up with $ 90.43820750088047
Illustration #9 You might end up with $ 73.74241268949282
Illustration #10 You might end up with $ 196.71513572895657
The average of all 10 illustrations is $ 162.71042261233785


Please enter initial balance: $10000
Please enter the lowest rate of return you anticipate for this year: -3
Please enter the highest rate of return you anticipate for this year: 20
How many years will you keep the investment in these stocks: 15
Illustration #1 You might end up with $ 8600.583546412887
Illustration #2 You might end up with $ 6332.5118913678925
Illustration #3 You might end up with $ 27590.315407153343
Illustration #4 You might end up with $ 20789.28179411367
Illustration #5 You might end up with $ 13458.683383241296
Illustration #6 You might end up with $ 119737.47886018296
Illustration #7 You might end up with $ 41772.48169415652
Illustration #8 You might end up with $ 27590.315407153343
Illustration #9 You might end up with $ 8600.583546412887
Illustration #10 You might end up with $ 10000.0
The average of all 10 illustrations is $ 28447.223553019478


Please enter initial balance: $10
Please enter the lowest rate of return you anticipate for this year: -50
Please enter the highest rate of return you anticipate for this year: 50
How many years will you keep the investment in these stocks: 4
Illustration #1 You might end up with $ 38.416000000000004
Illustration #2 You might end up with $ 39.5254161
Illustration #3 You might end up with $ 2.6873855999999994
Illustration #4 You might end up with $ 4.3046720999999994
Illustration #5 You might end up with $ 0.7311616000000002
Illustration #6 You might end up with $ 1.1316496
Illustration #7 You might end up with $ 7.163929599999999
Illustration #8 You might end up with $ 0.9834495999999998
Illustration #9 You might end up with $ 0.625
Illustration #10 You might end up with $ 4.9787136
The average of all 10 illustrations is $ 10.054737780000002
'''
