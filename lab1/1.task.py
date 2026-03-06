#Dictionary16
def update_counts(d, items):
    for item in items:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    return d
d={"apple":2,"banana":3}
items = ["apple","banana"]
n=update_counts(d, items)
print(n)

#17
task=lambda set1,set2,set3:(set1&set2)-set3
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
C = {5, 6, 9, 10}
result=task(A,B,C)
print(result)


#18
def sort_dict_by_value_sum(d):
    kos={}
    for key in d:
        total=0
        for num in d[key]:
            total+=num
            kos[num]=total
    items=[]
    for key in d:
        items.append((key,kos[num]))
    n=len(items)
    for i in range(n):
        for j in range(0,n-i-1):
            if items[j][1]>items[j+1][1]:
                items[j],items[j+1]=items[j+1],items[j]
            elif items[j][1]==items[j+1][1]:
                if items[j][0]>items[j+1][0]:
                    items[j],items[j+1]=items[j+1],items[j]

    return items
d1 = {
    "a": [1, 2, 3],
    "b": [10, 20],
    "c": [5, 5, 5],
    "d": [1, 1, 1, 1]
}
print(sort_dict_by_value_sum(d1))


#19
def filter_by_digit_sum(nums):
    result =set()
    for num in nums:
        if num%2!=0:
            n=num
            total_sum=0
            if n<0:
                n=-n
            while n>0:
                total=n%10
                total_sum+=total
                n=n//10
            if total_sum%2==0:
                result.add(num)
    return result
nums={13,12,21,15,44,34}
print(filter_by_digit_sum(nums))



#20
task = lambda d: [k for k, v in sorted(d.items(), key=lambda item: (item[1], len(item[0])))][:3]
d1 = {
    "apple": 5,
    "banana": 2,
    "kiwi": 5,
    "pear": 3,
    "plum": 2
}
result = task(d1)
sorted_items = sorted(d1.items(), key=lambda item: (item[1], len(item[0])))
print(f"Алынған кілттер: {result}")

#21
def count_leaf_values(d):
    count=0
    for key in d:
        value=d[key]
        if type(value)==dict:
            count+=count_leaf_values(value)
        else:
            count+=1
    return count
d1={
    "apple": 5,
    "banana": [1,2,3],
    "kiwi": {
        "d":10,
        "e":{
            "f":20,
        }
    }
}
result = count_leaf_values(d1)
print(result)


#22
a=lambda x1,x2:{
    x for x in x1
    if x not in x2 and x>(lambda t:(
        (lambda total=0: (
            (lambda s=0: (
                s
            ))()
        ))()
    ))(x2)
}
b={3,5,7,10}
d={2,4,6}
print(a(b,d))


#23
def group_by_last_letter(words):
    result={}
    for word in words:
        last=word[-1]
        if last not in result:
            result[last]=[]
        if word not in result[last]:
            result[last].append(word)
    return result
words=["diana","maral","bota","asyl","zere","nazerke"]
print(group_by_last_letter(words))


#24
def union_of_filtered_sets(sets_list):
    result=set()
    for s in sets_list:
        for num in s:
            if num >10 and num%2!=0:
                result.add(num)
    return result
sets_list=[
    {5,11,20},
    {13,8,25},
    {7,30,15}
]
print(union_of_filtered_sets(sets_list))


#25
san=lambda d:{
    k: __import__("functools").reduce(lambda a,b:a*b,[x for x in v if x>0])
    for k,v in d.items()
    if len([x for x in v if x>0])>0
}
data={
    "a": [1,2,-3],
    "b": [-6,-9],
    "c": [2,4],
}
print(san(data))


#26
def remove_elements_with_common_digits(a):
    digit_sum={}
    for num in a:
        n=abs(num)
        digits=set()
        if n==0:
            digits.add(0)
        while n>0:
            digits.add(n%10)
            n=n//10
        for d in digits:
            if d in digit_sum:
                digit_sum[d]+=1
            else:
                digit_sum[d]=1
    result=set()
    for num in a:
        n=abs(num)
        digits=set()
        if n==0:
            digits.add(0)
        while n>0:
            digits.add(n%10)
            n=n//10
        if all(digit_sum[d]==1 for d in digits):
            result.add(num)
    return result
a={12,23,34,45,56,11}
print(remove_elements_with_common_digits(a))



#27
is_prime=lambda n: n>1 and all(n%i!=0 for i in range(2,int(n**0.5)+1))
filter_d=lambda d:{k:v for k,v in d.items() if len(k)%2==1 and is_prime(v)}
data={
    "a": 2,
    "diana":5,
    "sum":4,
    "asd":5
}
print(filter_d(data))


#28
def sorted_unique_chars(d):
    chars=set()
    for a in d:
        for b in a:
            if b<'0' or b>'9':
                if b !='':
                    chars.add(b)
    return sorted(chars)
d=["diana","banana","zere2","a l a"]
print(sorted_unique_chars(d))


#29
sort_keys_by_last_digit=lambda a: sorted(a.keys() ,key=lambda k:(a[k]%10,k))
data={
    "apple": 23,
    "diana":15,
    "zere":32,
    "almaty":25,
}
sort_keys=sort_keys_by_last_digit(data)
print(sort_keys)


#30
def partition_by_sum_parity(a):
    even_set=set()
    odd_set=set()
    for num in a:
        total=0
        for digit in str(abs(num)):
            total+=int(digit)
        if total%2==0:
            even_set.add(total)
        else:
            odd_set.add(total)
    return (even_set,odd_set)
nums={123,245,78,9,12}
even,odd=partition_by_sum_parity(nums)
print("жұп сандар:",even)
print("тақ сандар:",odd)



#31
filter_d=lambda a:{k: v for k,v in a.items() if len(v)==len(set(v)) and all(len(s)>3 for s in v)}
data={
    "apple": ["sary","kyzyl","zhasyl"],
    "pets":["it","mysyk","homiyak"],
    "dari":["analgin","ketonav","paracetamol"]
}
print(filter_d(data))


#32
def parawise_intersections(sets_list):
    intersections=[]
    for i in range(len(sets_list)-1):
        intersections.append(sets_list[i] & sets_list[i+1])
    return intersections
sets_list=[{9,8,7},{6,8,7},{7,6,1}]
print(parawise_intersections(sets_list))