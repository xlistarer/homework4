# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
'''Task 1

The Guessing Game.

Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated. The result should be sent back to the user via a print statement.'''
import random



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    num=random.randint(1,10)
    while(True):
        user=int(input("Put your int number beetween 1 and 10. Try to guess my number"))
        if (user<1 or user>10):
            print("PLease input number beetwen 1 and 10")
        elif num<user:
            print("Too big")
        elif num>user:
             print("Too small")
        else:
            break
    print("You guess! My number is",num,"!")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''ask 2

The birthday greeting program.

Write a program that takes your name as input, and then your age as input and greets you with the following:

“Hello <name>, on your next birthday you’ll be <age+1> years”   '''
print("Hello {}, on your next birthday you’ll be {} years".format(input("What is your name?"),int(input("How old are you?"))+1))
'''Task 3

Words combination

Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.

For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters ‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …

Tips: Use random module to get random char from string)'''
start="hello"
for i in range (5):
    mas=random.sample(start,5)
    for j in range(5):
        print(mas[j],end='')
    print()
'''Task 4

The math quiz program

Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong, and then responds with a message accordingly.'''
while True:
    level = input("please select your level. print E if you want easy, M if you want midle, H if you want hard!")
    if level.lower() == 'e':
        num = 10
        break
    elif level.lower() == 'm':
        num = 100
        break
    elif level.lower() == 'h':
        num = 1000
        break

point = 0
for i in range(5):
    a = random.randint(1, num)
    b = random.randint(1, num)
    act = random.randint(1, 3)
    if act == 1:
        answer = int(input("{}+{}=?".format(a, b)))
        if a + b == answer:
            point += 1
    elif act == 2:
        answer = int(input("{}-{}=?".format(a, b)))
        if a - b == answer:
            point += 1
    else:
        answer = int(input("{}*{}=?".format(a, b)))
        if a * b == answer:
            point += 1
if point >= 3:
    print("Good job! You have {} right answer".format(point))
else:
    print("Try more! You have only {} right answer".format(point))