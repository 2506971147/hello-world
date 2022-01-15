import random
import shlex

'''
num = 0
file = open('chenjibiao.txt', 'a')
while num < 10000:
    number = random.randint(1, 3000)
    report = random.randint(0, 100)
    identifier = random.randint(1, 10)
    file.write(str(number))
    file.write(' ')
    file.write(str(report))
    file.write(' ')
    file.write(str(identifier))
    file.write('\n')
    num = num + 1
'''
fileobject = open('chenjibiao.txt', 'r')
num = 0
list = []
a = input("输入的学号是")
people = int(a)
quantity = 0
score = 0
d = input("科目是")
num4 = int(d)
quantity1 = 0
score1 = 0
while num < 10000:
    text = fileobject.readline()
    number = text.split()
    element = number[0]
    b = number[1]
    report = int(b)
    element1 = number[2]
    num5 = int(element1)
    num1 = int(element)
    list.append(num1)
    int(people)
    if people == num1:
        examination = number[1]
        exam = number[2]
        quantity = quantity + 1
        print("%d号学生的%s成绩是%s" % (people, exam, examination))
        c = int(examination)
        score = score + c
    if num4 == num5:
        examination1 = number[1]
        f = int(examination1)
        score1 = score1 + f
        quantity1 = quantity1 + 1
    num = num + 1
list.sort()
list1 = set(list)
print(list1)
num2 = len(list1)
print(num2)
print(quantity)
average = score / quantity
print(average)
average1 = score1 / quantity1
print(average1)
