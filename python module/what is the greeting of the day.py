#!/usr/bin/env python3

# Given the military time in the argument miltime, return a string containing the greeting of the day.

# 0300-1159 "Good Morning"
# 1200-1559 "Good Afternoon"
# 1600-2059 "Good Evening"
# 2100-0259 "Good Night"
def q1(miltime):
    if 300 <= miltime <= 1159:
      return 'Good Morning'
    elif 1200<=miltime<=1559:
      return 'Good Afternoon'
    elif 1600<=miltime<=2059:
      return 'Good Evening'
    elif 0<=miltime<259 or 2100<=miltime<=2300:
      return 'Good Night'
q1(2300)
q1(300)