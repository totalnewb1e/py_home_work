# задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

try:
    d = int(input("enter the day of the week from 1 to 7: "))
    days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
   
    if d == 6:
        print(days_of_the_week[-2])
        print("this is weekend")
    elif d == 7:
        print(days_of_the_week[-1])
        print("this is weekend")
    elif d == 1:
        print(days_of_the_week[0])
        print("this is weekday")
    elif d == 2:
        print(days_of_the_week[1])
        print("this is weekday")
    elif d == 3:
        print(days_of_the_week[2])
        print("this is weekday")
    elif d == 4:
        print(days_of_the_week[3])
        print("this is weekday")
    elif d == 5:
        print(days_of_the_week[-3])
        print("this is weekday")    
    else:
        print("something goes wrong, please enter number from 1 to 7")
except:
    print("please enter number from 1 to 7")