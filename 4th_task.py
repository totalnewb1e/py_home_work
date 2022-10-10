# задача 4 HARD необязательная Напишите простой калькулятор, который считывает с пользовательского ввода три строки: 
# первое число, второе число и операцию, после чего применяет операцию к введённым числам("первое число" "операция" "второе число") 
# и выводит результат на экран.

try:
    samp = float(input('enter 1st sample: '))
    sing = str(input('enter sing such like +, -, /, *, %, ** or //: '))
    samp_two = float(input('enter 2nd sample: '))
    op = ['+', '-', '/', '*', '%', '**', '//']

    if sing == op[0]:
        print(f'answer is {samp + samp_two}')
    elif sing == op[1]:
        print(f'answer is {samp - samp_two}')
    elif sing == op[2]:
        print(f'answer is {samp / samp_two}')
    elif sing == op [3]:
        print(f'answer is {samp * samp_two}')
    elif sing == op[-3]:
        print(f'answer is {samp % samp_two}')
    elif sing == op[-2]:
        print(f'answer is {samp ** samp_two}')
    elif sing == op[-1]:
        print(f'answer is {samp // samp_two}')
except:
    if samp_two == 0:
        print('fatal. div by zero')