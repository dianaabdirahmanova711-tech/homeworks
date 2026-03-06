#Lambda_function
#1task
from selectors import SelectSelector

a=lambda x: "positive" if x>0 else "negative" if x<0 else "zero"
print(a(3))
print(a(-5))
print(a(0))

#2task
words = ["арбуз", "кот", "машина", "дом", "ананас"]
a=sorted(words, key=lambda word:len(word))
print(a)

#3task
numbers = [5, 12, 7, 20, 33, 8]
a=list(filter(lambda x: x%2==0 and x>10,numbers))
print(a)

#4task
numbers = [1, 2, 3, 4, 5, 6]
a=list(map(lambda x:x*x if x%2==0 else x*3 if x%2!=0 else x,numbers))
print(a)


#5task
c=lambda a,b: "а больше " if a>b else "б больше" if a<b else "равны"
print(c(10,9))
print(c(-3,8))
print(c(3,3))

#6task
numbers = [0, -3, 5, -7, 8]
a=lambda x:"положительное" if x>0 else "отрицательное" if x<0 else "ноль"
b=[a(x) for x in numbers]
print(b)


#Итераторы и comprehension
#1task
a=[]
for i in range(1,20+1):
    if i%2==0:
        a.append(i)
print(a)

#2task
from functools import reduce
matrix = [[1,2,3], [4,5,6], [7,8,9]]
result=[reduce(lambda x,y: x*y,row) for row in matrix]
print(result)


#3task
words = ["кот", "машина", "ананас", "дом"]
a=[x for x in words if len(x) > 4 and "а" not in x]
print(a)

#4task
numbers = [1,2,3,4,5]
a=["четное" if x%2==0 else "нечетное" for x in numbers]
print(a)

#5task
matrix = [[1,2], [3,4], [5,6]]
a=[x for row in matrix for x in row]
print(a)

#6task
result=["FizzBizz" if x%3==0 and x%5==0 else
        "Fizz" if x%3==0 else
        "Bizz" if x%5==0 else x
        for x in range(1,21)]
print(result)


#Смешанные сложные задачи
#1task
def special_numbers(n):
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            yield "FizzBizz"
        if i%5==0:
            yield "Fizz"
        elif i%3==0:
            yield "Bizz"
        else:
            yield i
for i in special_numbers(15):
    print(i)

#2task
words = ["кот", "машина", "арбуз", "дом", "ананас"]
process = lambda w: (w.upper() if len(w) > 4 else "short") + ("*" if "а" in w else "")
result=[process(word) for word in words]
print(result)

#3task

def process_numbers(numbers):
    a=filter(lambda x:"" if x<0 else "0",numbers)
    evens=map(lambda x:x/2 if x%2==0 else x*3+1 ,a)
    return list(evens)
numbers = [5, -2, 8, 0, -7, 3]
for num in process_numbers(numbers):
    print(num)

#4task
students = [("Иван", 85), ("Анна", 72), ("Пётр", 90), ("Мария", 60)]
nums=[score for name,score in students]
a=lambda x:"Отлично" if x>=90 else "Хорошо" if 70<=x<90 else "Удовлетворительно"
b={name:a(score) for name,score in students}
print(b)


#5task
def matrix_transform(matrix):
    result=(
        "кратно 6" if x%6==0 else
        "четное" if x%2==0 else
        "кратно 3" if x%3==0 else
        x
        for row in matrix
        for x in row
    )
    for item in result:
        yield item
matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
for x in matrix_transform(matrix):
    print(x)


#Задачи для понимания map and filter
#1task
numbers = [5, -2, 8, 0, -7, 3]
a=list(map(lambda x:x*2,numbers))
print(a)

#2task
words=["diana","zere","maral","ana"]
a=list(map(lambda x:x.upper() +"!" if len(x)>3 else x.upper(),words))
print(a)

#3task
numbers=[5, -2, 8,  -7, 3,6]
a=list(filter(lambda x:x%2==0,numbers))
print(a)


#4task
numbers = [0, 5, 12, 7, 20, -3, 8]
b=list(map(lambda x:x*0.5 if x%2==0 else x*3 ,numbers))
a=list(filter(lambda x: x>5,b))
print(a)

#generator
#1task
def even_numbers(n):
    for i in range(1,n+1):
        if i%2==0:
            if i%4==0:
                yield "Кратно 4"
            else:
                yield i
for x in even_numbers(10):
    print(x)

#2task
def filter_words(words):
    for word in words:
        if len(word) > 4:
            if "а" in word:
                yield "с а"
words = ["кот", "машина", "арбуз", "дом"]
for w in filter_words(words):
    print(w)

#3task
def infinite_numbers():
    i=1
    while i>=1:
        if i%15==0:
            yield "FizzBizz"
        if i%5==0:
            yield "Fizz"
        if i%3==0:
            yield "Bizz"
        else:
            yield i
        i+=1
count=0
for num in infinite_numbers():
    print(num, end="")
    count+=1
    if count>=15:
        break

#4task
def squares(n):
    for i in range(1,n+1):
        if i%2==0:
            yield "Четный квадрат"
        else:
            yield i
for x in squares(10):
    print(x)
