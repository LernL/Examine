import random
#                                       №1
print("")
a=[1,1,2,3,5,8,13,21,34,55,89]
for i in a:
    if i<=5:
        print(i)
#                                       №2
print("")
k=1
b=[[random.randint(0,15)] for i in range(5)]
print(b)
print(b[0])
print(b[4])
for j in b:
    k=1*j
print(k)
#                                       №3
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217]
for i in numbers:
    if i%2==0:
        print(i)
    if i==237:
        break
#                                       №4
print("")
age=int(input("Введите возраст"))
if age<2:
    print("Младенец")
elif age>=2 and age<4:
    print("Малыш")
elif age>=4 and age<13:
    print("Ребенок")
elif age>=13 and age<20:
    print("Подросток")
elif age>=20 and age<65:
    print("Взрослый")
else:
    print("Пожилой человек")
#                                       №5
print(" ")
users_1=["user_1","user_2","user_3"]
users_2=[]
while users_2==users_1:
    users_2.append(users_1)
print(users_2)
#                                       №6
print(" ")
a=['pizza','falafel','carrot cake']
b=['pizza','falafel','carrot cake']
m=input("Введите мороженое")
b.append(m)
for i in b:
    print(i)
#                                       №7
print(" ")
g=0
list=[11,5,8,32,15,3,20,132,21,4,55,9,20]
for i in list:
    if i<30 and i%3==0:
        print(i)
    else:
        g+=i
print(g)
#                                       №8
print("")
list={'a':2,'b':4,'c':6,'d':8}
for i in list.values():
    if i>2:
        print(i)
#                                       №9
k=[]
t=int(input("Введите степень"))
print("")
a=[10,4,6,8,2]
b=[31,452,6,72,52]
list={
    'key': a,
    'value': b
    }
for i,j in list.items():
    for n in j:
        n=n**t
        if n==961:
            k=[]
        k.append(n)
    print(f'Я знаю твой ключ – {i}, его значение является {k}')
#                                       №11
e=[]
o=[]
dic={'a':1,'b':2,'c':3,'d':4}
for i,j in dic.items():
    if j%2==0:
        e.append(j)
    else:
        o.append(j)
print(f'even: {e}')
print(f'odd: {o}')
#                                   №12

n=int(input("n="))
m=int(input("m="))

a=[[random.randint(0,10) for j in range(m)] for i in range(n)]
print(a)

r=int(input("r="))
t=int(input("t="))
print(a[r][t])
