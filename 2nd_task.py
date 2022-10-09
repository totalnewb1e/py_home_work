# задача 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

try:
    x = int(input("value for x: "))
    y = int(input("value for y: "))
    z = int(input("value for z: "))

    left_part = not (x or y or z)
    right_part = not x and not y and not z

    if left_part == right_part:
        print("statement is true")
    else:
        print("statement is false")
except:
    print("enter numbers!")