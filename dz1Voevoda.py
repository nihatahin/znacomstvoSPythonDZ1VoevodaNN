def taskChoice():
    while True:
        global taskNum
        taskNum = int(input("Enter task number: "))
        if 0 < taskNum <= maxTaskNum:
            return
        else:
            print("Invalid task number was entered. Please, try again.")
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------            
def taskFuncChoice():
    global taskNum
    match taskNum:
        case 1:
            task1()
        case 2:
            task2()
        case 3:
            task3()
        case 4:
            task4()
        case 5:
            task5()
        case _:
            print('Invalid task number')
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def task1():
    print('Task #1.')
    weekDay = None
    weekSunday = 7
    weekSaturday = 6
    while True:
        weekDay = input("Enter week day number or '/break' to change task: ")
        if weekDay == '/break':
            return
        else:
            weekDay = int(weekDay)
        if 0 < weekDay <= weekSunday:
            if weekDay >= weekSaturday:
                print(f'{weekDay} is a holiday!')
            else:
                print(f'{weekDay} is a workday...')
        else:
            print("Invalid week day was entered. Please, try again.")
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def task2():
    print('Task #2.')
    print("Let's prove trueness of expression:\n\t\t!(X|Y|Z) = !X & !Y & !Z\n")
    print("X\t\tY\t\tZ\t\t!(X|Y|Z)\t\t!X & !Y & !Z\t\tResut") 
    print("---------------------------------------------------------------------------------------------------------")
    boolRange = [False, True]
    firstExppression = False
    secondExppression = False
    strAnswer = ""
    for i in range(2):
        for j in range(2):
            for k in range(2):
                firstExppression = not(boolRange[i] or boolRange[j] or boolRange[k])
                secondExppression = not boolRange[i] and not boolRange[j] and not boolRange[k]
                if (firstExppression == secondExppression):
                    strAnswer = "Is equal!"
                else:
                    strAnswer = "Isn't equal!"
                print(f'{boolRange[i]}\t\t{boolRange[j]}\t\t{boolRange[k]}\t\t{firstExppression}\t\t\t{secondExppression}\t\t\t{strAnswer}')
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def task3():
    print('Task #3.')
    x = 0
    y = 0
    while True:
        x = input("Enter non-zero x coordinate or '/break' to change task: ")
        if x == '/break':
            return
        else:
            x = int(x)
        y = int(input("Enter non-zero y coordinate: "))
     
        quarter = ""
        if y > 0:
            if x > 0:
                quarter = "first"
            elif x < 0:
                quarter = "second"
            else:
                print('You are dummy-dum! It was told: "NON-ZERO coordinate." Your point is on the X-axis.')
                continue
        elif y < 0:
            if x > 0:
                quarter = "fourth"
            elif x < 0:
                quarter = "third"
            else:
                print('You are dummy-dum! It was told: "NON-ZERO coordinate." Your point is on the X-axis.')
                continue
        else:
            if x == 0:
                print('You are dummy-dum! It was told: "NON-ZERO coordinate." Your point is coordinate origin.')
                continue
            else:
                print('You are dummy-dum! It was told: "NON-ZERO coordinate." Your point is on the Y-axis.')
                continue

        print(f"Point ({x}, {y}) is located on the {quarter} quarter.")
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def task4():
    print('Task #4.')
    while True:
        quart = input("Enter quarter number or '/break' to change task: ")
        if quart == '/break':
            return
        else:
            quart = int(quart)
        
        xMin = ""
        xMax = ""
        yMin = ""
        yMax = ""
        match quart:
            case 1:
                xMin = "0"
                xMax = "inf"
                yMin = "0"
                yMax = "inf"
            case 2:
                xMin = "-inf"
                xMax = "0"
                yMin = "0"
                yMax = "inf"
            case 3:
                xMin = "-inf"
                xMax = "0"
                yMin = "-inf"
                yMax = "0"
            case 4:
                xMin = "0"
                xMax = "inf"
                yMin = "-inf"
                yMax = "0"
            case _:
                print('Invalid quarter number!')
                continue
        strQuart = ['First', 'Second', 'Third', 'Fourth']
        print(f'{strQuart[quart - 1]} quarter range of point coordinate is (x, y) where:')
        print(f'\tx is over the {xMin} (excluded) to {xMax} (excluded) range ({xMin}, {xMax})\n\ty is over the {yMin} (excluded) to {yMax} (excluded) range ({yMin}, {yMax})')
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def task5():
    print('Task #5.')
    while True:
        ax = input("Enter A point x coordinate or '/break' to change task: ")
        if ax == '/break':
            return
        else:
            ax = int(ax)
        ay = int(input("Enter A point y coordinate: "))
        bx = int(input("Enter B point x coordinate: "))
        by = int(input("Enter B point y coordinate: "))
        print(f'Distancse between A({ax}, {ay}) and B({bx}, {by}) is {round((((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5), 2)}')
#####################################################################
#####################################################################
##################################################################### 
taskNum = None
maxTaskNum = 5

while True:
    taskChoice()
    print()
    taskFuncChoice()
    print()

    
    