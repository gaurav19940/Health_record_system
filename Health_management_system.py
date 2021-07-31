# to make 6  files with name-3 , diet and exercise plan
# file - names - factors
# input in them string differently
# then func for reading

from datetime import datetime

print('This is to enter the data \n\n')


def entry():
    d_stamp = datetime.now()
    date = str(d_stamp.date())
    time = str(d_stamp.time().replace(microsecond=0, second=0))
    name = int(input('Enter 1 for Harry, 2 for Rohan , 3 for Hammad: '))


    if name == 1:
        param_h = int(input('Enter 1 for Diet , 2 for exercise: '))

        if param_h == 1:
            with open('Harry_Diet.txt', 'r+') as harry_D:
                flag = False
                for line in harry_D:
                    if date in line:
                        flag = True
                        break
                if not flag:
                    harry_D.write((date + '\n'))
                harry_D.write(time + '    ')
                meal = input('Enter your meal: ')
                harry_D.write((meal + '\n'))
                print("Entered Successfully")

        if param_h == 2:
            with open('Harry_Exercise.txt', 'r+') as harry_ex:
                flag = False
                for line in harry_ex:
                    if date in line:
                        flag = True
                        break
                if not flag:
                    harry_ex.write((date + '\n'))
                harry_ex.write(time + '    ')
                exercise = input('Enter your exercises: ')
                harry_ex.write((exercise + '\n'))
                print("Entered Successfully")


    if name == 2:
        param_r = int(input('Enter 1 for Diet , 2 for exercise: '))

        if param_r == 1:
            with open('Rohan_Diet.txt', 'r+') as rohan_D:
                flag = False
                for line in rohan_D:
                    if date in line:
                        flag = True
                        break
                if not flag:
                    rohan_D.write((date + '\n'))
                rohan_D.write(time + '    ')
                meal = input('Enter your meal: ')
                rohan_D.write((meal + '\n'))
                print("Entered Successfully")

        if param_r == 2:
            with open('Rohan_Exercise.txt', 'r+') as rohan_ex:
                flag = False
                for line in rohan_ex:
                    if date in line:
                        flag = True
                        break
                if not flag:
                    rohan_ex.write((date + '\n'))
                rohan_ex.write(time + '    ')
                exercise = input('Enter your exercises: ')
                rohan_ex.write((exercise + '\n'))
                print("Entered Successfully")


    if name == 3:
        param_hm = int(input('Enter 1 for Diet , 2 for exercise: '))

        if param_hm == 1:
            flag = False
            with open('Hammad_Diet.txt', 'r+') as hammad_D:
                for line in hammad_D:
                    if date in line:
                        flag = True
                        break
                if not flag:
                    hammad_D.write((date + '\n'))
                hammad_D.write(time + ' ')
                meal = input('Enter your meal: ')
                hammad_D.write((meal + '\n'))
                print("Entered Successfully")

        if param_hm == 2:
            with open('Hammad_Exercise.txt', 'r+') as hammad_ex:
                flag = False
                for line in hammad_ex:
                    if date in line:
                        flag = True
                        break
                if not flag:
                    hammad_ex.write((date + '\n'))
                hammad_ex.write(time + '    ')
                exercise = input('Enter your exercises: ')
                hammad_ex.write((exercise + '\n'))
                print("\nEntered Successfully")


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


perform()

repeat = input('\nWant to add/retrieve more: Y/N  : ')
if repeat == 'Y':
    perform()
