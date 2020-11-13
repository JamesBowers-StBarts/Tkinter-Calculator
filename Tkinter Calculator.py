import math
from tkinter import *
root = Tk()
root.title("Calculator")

row1=Frame(master=root)
row2=Frame(master=root)
row3=Frame(master=root)
row4=Frame(master=root)
row5=Frame(master=root)
row6=Frame(master=root)
row7=Frame(master=root)

#Row 1 (calculator display)

display=Label(
    text="3267487888878",
    width=48,
    height=5
)

#Row 2 (%,CE,C,>_)

percentbtn=Button(
    master=row2,
    text="%",
    width=12,
    height=5
)

cebtn=Button(
    master=row2,
    text="CE",
    width=12,
    height=5
)

cbtn=Button(
    master=row2,
    text="C",
    width=12,
    height=5
)

bkspcbtn=Button(
    master=row2,
    text="_<",
    width=12,
    height=5
)

#Row 3 (1/x,x^2,2√x,÷)
 
frcbtn=Button(
    master=row3,
    text="1/x",
    width=12,
    height=5
)
sqbtn=Button(
    master=row3,
    text="x^2",
    width=12,
    height=5
)

sqrtbtn=Button(
    master=row3,
    text="2√x",
    width=12,
    height=5
)

devidebtn=Button(
    master=row3,
    text="÷",
    width=12,
    height=5
)

#Row 4 (7,8,9,x)

btn7=Button(
    master=row4,
    text="7",
    width=12,
    height=5
)

btn8=Button(
    master=row4,
    text="8",
    width=12,
    height=5
)

btn9=Button(
    master=row4,
    text="9",
    width=12,
    height=5
)

multiplybtn=Button(
    master=row4,
    text="x",
    width=12,
    height=5
)

#Row 5 (4,5,6,-)

btn4=Button(
    master=row5,
    text="4",
    width=12,
    height=5
)

btn5=Button(
    master=row5,
    text="5",
    width=12,
    height=5
)

btn6=Button(
    master=row5,
    text="6",
    width=12,
    height=5
)

btnnegative=Button(
    master=row5,
    text="-",
    width=12,
    height=5
)

#Row 6 (1,2,3,+)

btn1=Button(
    master=row6,
    text="1",
    width=12,
    height=5
)

btn2=Button(
    master=row6,
    text="2",
    width=12,
    height=5
)

btn3=Button(
    master=row6,
    text="3",
    width=12,
    height=5
)

btnplus=Button(
    master=row6,
    text="+",
    width=12,
    height=5
)

#Row 7 (+/-,0,.,=)

pmbtn=Button(
    master=row7,
    text="+/-",
    width=12,
    height=5
)

btn0=Button(
    master=row7,
    text="0",
    width=12,
    height=5
)

btndot=Button(
    master=row7,
    text=".",
    width=12,
    height=5
)

btnequals=Button(
    master=row7,
    text="=",
    width=12,
    height=5
)

display.pack()
row1.pack()

percentbtn.pack(side=LEFT)
cebtn.pack(side=LEFT)
cbtn.pack(side=LEFT)
bkspcbtn.pack(side=LEFT)
row2.pack()

frcbtn.pack(side=LEFT)
sqbtn.pack(side=LEFT)
sqrtbtn.pack(side=LEFT)
devidebtn.pack(side=LEFT)
row3.pack()

btn7.pack(side=LEFT)
btn8.pack(side=LEFT)
btn9.pack(side=LEFT)
multiplybtn.pack(side=LEFT)
row4.pack()

btn6.pack(side=LEFT)
btn5.pack(side=LEFT)
btn4.pack(side=LEFT)
btnnegative.pack(side=LEFT)
row5.pack()

btn1.pack(side=LEFT)
btn2.pack(side=LEFT)
btn3.pack(side=LEFT)
btnplus.pack(side=LEFT)
row6.pack()

pmbtn.pack(side=LEFT)
btn0.pack(side=LEFT)
btndot.pack(side=LEFT)
btnequals.pack(side=LEFT)
row7.pack()

root.mainloop()