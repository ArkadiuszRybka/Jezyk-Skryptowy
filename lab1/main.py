#zad1
from datetime import date, datetime

a=5
b=8
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#zad2
c=input("Podaj imie ")
print("Czesc " + c)

#zad3
print(float(input("Podaj liczbe")) + float(input("Podaj liczbe")))

#zad4

print(sum(range(8,81)))

#zad5

print(date.fromisoformat("2023-03-02")-date.today())

#zad6
x=float(input("Podaj pierwsza liczbe: "))
y=float(input("Podaj druga liczbe: "))
z=input("Podaj dzialanie(+,-,*,/): ")

if z=="+": print(x+y)
if z=="-": print(x-y)
if z=="*": print(x*y)
if z== '/': print(x / y)
else: print("Błędne działanie")