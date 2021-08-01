# to make 6  files with name-3 , diet and exercise plan
# file - names - factors
# input in them string differently
# then func for reading

from datetime import datetime
d_stamp = datetime.now()
date = str(d_stamp.date())
time = str(d_stamp.time().replace(microsecond=0, second=0))

print('This is management of diet and exercise of 3 persons , You can add and retrieve from these files  \n\n')

def diet(a = 'Harry_Diet.txt',b = 'harry_D'):
    with open(a,'a') as b:
        with open(a, 'r+') as s:
            flag = False
            for line in s:
                if date in line:
                    flag = True
                    break
        if not flag:
            b.write((date + '\n'))
        b.write(time + '    ')
        meal = input('Enter your meal: ')
        b.write((meal + '\n'))
        print("Entered Successfully")

def exer(a = 'Harry_Exercise.txt',b = 'harry_ex'):
    with open(a,'a') as b:
        with open(a, 'r+') as s:
            flag = False
            for line in s:
                if date in line:
                    flag = True
                    break
        if not flag:
            b.write((date + '\n'))
        b.write(time + '    ')
        exercise = input('Enter your exercises: ')
        b.write((exercise + '\n'))
        print("Entered Successfully")

    
    



def entry():
    name = int(input('Enter 1 for Harry, 2 for Rohan , 3 for Hammad: '))


    if name == 1:
        param_h = int(input('Enter 1 for Diet , 2 for exercise: '))
        
        if param_h == 1:
            diet(a = 'Harry_Diet.txt',b = 'harry_D')

        if param_h == 2:
            exer(a = 'Harry_Exercise.txt',b = 'harry_ex')
            

    if name == 2:
        param_r = int(input('Enter 1 for Diet , 2 for exercise: '))

        if param_r == 1:
           diet(a = 'Rohan_Diet.txt',b = 'rohan_D')

        if param_r == 2:
           exer(a = 'Rohan_Exercise.txt',b = 'rohan_ex')
           

    if name == 3:
        param_hm = int(input('Enter 1 for Diet , 2 for exercise: '))

        if param_hm == 1:
            diet(a = 'Hammad_Diet.txt',b = 'hammad_D')

        if param_hm == 2:
            exer(a = 'Hammad_Exercise.txt',b = 'hammad_ex')
            

def retrieve():
    a = int(input('Enter 1 for Harry , 2 for Rohan, 3 for Hammad: '))
    b = int(input('Enter 1 for Diet , 2 for Exercises: '))
    try:
        if a == 1:
            if b == 1:
                with open('Harry_Diet.txt') as f:
                    print(f.read())
            elif b == 2:
                with open('Harry_Exercises.txt') as f:
                    print(f.read())

        elif a == 2:
            if b == 1:
                with open('Rohan_Diet.txt') as f:
                    print(f.read())
            elif b == 2:
                with open('Rohan_Exercises.txt') as f:
                    print(f.read())

        elif a == 3:
            if b == 1:
                with open('Hammad_Diet.txt') as f:
                    print(f.read())
            elif b == 2:
                with open('Hammad_Exercise.txt') as f:
                    print(f.read())

    except Exception as e:
        print('Error: ', e)


def perform():
    op = int(input('Enter 1 for log , 2 for Retrieve : '))
    if op == 1:
        entry()
    elif op == 2:
        retrieve()
    repeat = input('\nWant to add/retrieve more: Y/N  : ')
    if repeat == 'Y':
        perform()
    else:
        pass



perform()

