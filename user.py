import os

def reg():
    file = open('User.txt','a', enconding = 'ANSI')
    user = input('Введите имя, фамилию и группу')
    user = user + '\n'
    file.write(user)
    file.close()
def printUser():
    file = open('User.txt','r',enconig = 'ANSI')
    for user in file:
        print(user,end'')
def delUser():
    old = open('user.txt','r',enconing = 'ANSI')
    user = input
