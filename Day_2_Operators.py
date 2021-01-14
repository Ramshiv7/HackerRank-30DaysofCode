import math
import os
import random
import re
import sys

# Complete the solve function below.

meal_cost = input()
tip =input()
tax = input()

tip_cal= float(meal_cost) * int(tip)/100
tax_cal= float(meal_cost) * int(tax)/100

total_price= float(meal_cost) + float(tip_cal) + float(tax_cal)
print(round(total_price))
