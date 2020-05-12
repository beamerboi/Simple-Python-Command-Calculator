import re

previous = 0
run = True
print("Hello and welcome to this simple python command calculator")
print("Type 'quit' to quit the calculator!")


def meine_calculator():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Type your math equation -> ")
    else:
        equation = input(str(previous))

    if equation == "quit":
        print("Come back whenever you feel you are stuck!")
        run = False
    else:
        equation = re.sub('[A-Za-z:;.?,()" "]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    meine_calculator()
