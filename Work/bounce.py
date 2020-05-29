# bounce.py
#
# Exercise 1.5
# A rubber ball is dropped from a height of 100 meters and each time it hits
# the ground, it bounces back up to 3/5 the height it fell. Write a program 
# bounce.py that prints a table showing the height of the first 10 bounces.

h = 100
ratio = 3/5
i = 1

while i <= 10:
    h = h * ratio
    print(i, round(h, ndigits=4))
    i = i + 1
    
