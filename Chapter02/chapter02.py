#!/usr/bin/env python3

year_cheese = [(2000, 29.87), (2001, 30.12), (2002, 30.6), (2003,
30.66),(2004, 31.33), (2005, 32.62), (2006, 32.73), (2007, 33.5),
(2008, 32.84), (2009, 33.02), (2010, 32.92)]
print(max(year_cheese))
print(max(year_cheese, key=lambda yc: yc[1]))

import math
def isprimer_procedural(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, (1 + math.sqrt(n))):
        if n % i == 0:
            return False
    return True
