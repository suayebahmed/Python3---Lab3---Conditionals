# Zeller's congruence
import math

# taking month, year, day as input from the user
month = int(input("Enter the month (1-12): "))
day = int(input("Enter the day of the month (1-31): "))
year = input("Enter the year: ")

# Solving tricky part of the month 1, 2
if month == 1:
    month_ = 13
    year = str(int(year) - 1)
elif month == 2:
    month_ = 14
    year = str(int(year) - 1)
else:
    month_ = month

# Re-assigning the value according to the formula.
q = day                 # day of the month (1-31)
m = month_              # month (1-12)
K = int(year[-2:])      # year of the century ('21' for 2021)
J = int(year[:2])       # century ('20' for 2021)

# working with Formula
part_of_h = math.floor((13 * (m + 1)) / 5)
h = (q + part_of_h + K + math.floor(K // 4) + math.floor(J // 4) + 5 * J) % 7

# value of h to day of the week
# Showing the results
if h == 0:
    print(f"{month}/{day}/{year} is a Saturday")
elif h == 1:
    print(f"{month}/{day}/{year} is a Sunday")
elif h == 2:
    print(f"{month}/{day}/{year} is a Monday")
elif h == 3:
    print(f"{month}/{day}/{year} is a Tuesday")
elif h == 4:
    print(f"{month}/{day}/{year} is a Wednesday")
elif h == 5:
    print(f"{month}/{day}/{year} is a Thursday")
elif h == 6:
    print(f"{month}/{day}/{year} is a Friday")
