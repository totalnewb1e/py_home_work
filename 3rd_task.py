# задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

try:
    x = float(input("enter x coordinate: "))
    y = float(input("enter y coordinate: "))

    if (x == 0 and y == 0):
        print("this dot has no sector")
    elif (x < 0 and y < 0):
        print("3rd sector")
    elif (x < 0 and y > 0):
        print("4th sector")
    elif (x > 0 and y > 0):
        print("1st sector")
    elif (x < 0 and y > 0):
        print("2nd sector")
    elif (x == 0 and y < 0 or x == 0 and y > 0 ):
        print("dot is on Y axis")
    elif (y == 0 and x < 0 or y == 0 and x > 0  ):
        print("dot is on X axis")
except:
    print("try numbers...")