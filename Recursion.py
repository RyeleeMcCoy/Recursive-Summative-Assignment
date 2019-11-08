#-----------------------------------------------------------------------
#Recursive Summative
#Ryelee McCoy
#November 7 2019
#
#--------------------------Functions/Lists------------------------------
import turtle

#--------------------------Actual Code----------------------------------


T = turtle.Turtle()
Screen = turtle.Screen()
lineLen = 100
T.width(3)

def simple_recursion_program(lineLen, T):
    if lineLen >10:
        T.left(90)
        T.forward(80)
        T.right(45)
        T.forward(80)
        lineLen = lineLen /1.35
        simple_recursion_program(lineLen, T)
        

simple_recursion_program(lineLen, T)
T.color("green")
T.goto(0,30)
simple_recursion_program(lineLen, T)
T.color("blue")
T.goto(0,60)
simple_recursion_program(lineLen, T)
T.color("red")
T.goto(0,-30)
simple_recursion_program(lineLen, T)
T.color("yellow")
T.goto(0,-60)
simple_recursion_program(lineLen, T)
T.color("pink")
T.goto(30,0)
simple_recursion_program(lineLen, T)
T.color("dark violet")
T.goto(60,0)
simple_recursion_program(lineLen, T)
T.color("cyan")
T.goto(-30,0)
simple_recursion_program(lineLen, T)
T.color("gold")
T.goto(-60,0)
simple_recursion_program(lineLen, T)
T.color("lime green")

#------------------Benefits & Specific Uses----------------------

#The positives of using external files are very expansive. It is near perfect for coding games with
#save games, it can be used to better clean your coding, by essentially “deleting” the extensive lists from
#the program and transferring into external files, and it can also give the player or user
#a significantly  easier way to look at the actual document of what they have, instead of using occasionally hard to read lists.
#they can just opt in and they have the option to call on the contents of the appropriate file.

#They are a fair amount of uses for External files, from making save games, to running lists,
#You can control your games from outside of the game, instead of having those long winded,
#print this print that, to explain part of a game or a story, you can just write it all into a part of the,
#file, and print that, boom, so many less program lines used.
