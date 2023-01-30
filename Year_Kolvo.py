den = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print("Введите год: ")
year = int(input())
summa = 0

if(year % 4 == 0):
    if(year % 100 == 0 and year % 400 !=0):
        den[1] = 28
    else: 
        den[1] = 29
for x in range(len(den)):
    day = den[x]
    i = 1
    while day >= i:
        if(i >= 10):
            stroka = str(i)
            summa += int(stroka[0]) + int(stroka[1])
        else:
            summa += i
        i += 1
    
print(summa)
