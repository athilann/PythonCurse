from turtle import *


shape("turtle")
ws = Screen()
ws.setup(1000,600)

def threeNPlus1(number):
    forward(number)
    color("green")
    dot(number)
    color("black")
    if number == 1 or number == 0:
        return
    if((number % 2) == 0):
        right(number)
        threeNPlus1(number / 2)
    else:
        left((number))
        threeNPlus1((number*3) + 1)

number = 0
while number < 20:
    threeNPlus1(number)
    number += 1
     
mainloop()
