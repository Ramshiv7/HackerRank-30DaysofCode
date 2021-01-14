#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    
    for _ in range(1,11):
        for i in range(1):
            print(f'{n} x {_} = {n*_}')
