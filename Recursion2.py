#-----------------------------------------------------------------------
#Recursive Summative
#Ryelee McCoy
#November 7 2019
#
#--------------------------Functions/Lists------------------------------
import turtle

#--------------------------Actual Code----------------------------------


def T_right(branchLen, T):
    T.forward(branchLen)
    T.right(20)

def T_left(branchLen, T):
    T.forward(branchLen)
    T.left(20)
        
#Main Code
T = turtle.Turtle()
Screen = turtle.Screen()
branchLen = 100
T.left(90)
while branchLen >=10:
    T_right(branchLen, T)
    branchLen = branchLen /2
T.penup()
T.goto(0,0)
T.left(90)
T.pendown()
branchLen = 100
T.right(10)
while branchLen >=10:
    T_left(branchLen, T)
    branchLen = branchLen /2
T.penup()
T.goto(0,0)
T.right(80)
T.pendown()
branchLen = 50
while branchLen >=10:
    T_left(branchLen, T)
    branchLen = branchLen /1.5
T.right(30)
T.backward(20)
