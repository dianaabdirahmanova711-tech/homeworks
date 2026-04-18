#1
check=lambda x:"положительные" if x>0 else "отрицательные" if x<0 else "0"
print(check(0))
print(check(1))
print(check(-2))

#4
numbers = [1, 2, 3, 4, 5, 6]
a=list(map(lambda x:x*x if x%2==0 else x*3, numbers))
print(a)



#4
def squares(n):
    for i in range(1,n+1):
        if i*i>0:
            if i%2==0:
                yield "четный квадрат"
            else:
                yield i
for a in squares(5):
    print(a)


#4
numbers = [1,2,3,4,5]
a=["четное " if x%2==0 else "нечетное" for x in numbers  ]
print(a)

#4
students = [("Иван", 85), ("Анна", 72), ("Пётр", 90), ("Мария", 60)]
a=[score for name,score in students]
b=lambda x:"great" if x>=90 else "good" if 70<x<90 else "bad"
c={name:b(score) for name,score in students}
print(c)



#4
numbers=[10,-2,8,5,9,4,0]
a=filter(lambda x: x>5, numbers)
b=list(map(lambda x:x*0.5 if x%2==0 else x*3 ,a))
print(b)