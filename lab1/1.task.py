#1
def analyze_text(text):
    vowels = "aeiouyаеёиоуыэюяAEIOUYАЕЁИОУЫЭЮЯ"
    text_lower = text.lower()

    found_vowels = []
    for ch in text_lower:
        if ch.isalpha() and ch in vowels.lower() and ch not in found_vowels:
            found_vowels.append(ch)
    unique_vowels = len(found_vowels)

    words = []
    for word in text.split():
        clean = ""
        for ch in word:
            if ch.isalpha():
                clean += ch
        if len(clean) >= 5 and clean[0].lower() == clean[-1].lower():
            if clean not in words:
                words.append(clean)

    return (unique_vowels, " ".join(words))
#2
task2 = lambda s: " ".join(
    word[::-1] for word in s.split()
    if not any(ch.isdigit() for ch in word) and len(word) % 2 == 0
)

#3
def top_k_words(text, k):
    clean_text = ""
    for ch in text:
        if ch.isalnum() or ch.isspace():
            clean_text += ch
        else:
            clean_text += " "

    words = clean_text.lower().split()

    freq = {}
    for w in words:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1

    items = []
    for key in freq:
        items.append((key, freq[key]))

    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j][1] < items[j + 1][1]:
                items[j], items[j + 1] = items[j + 1], items[j]
            elif items[j][1] == items[j + 1][1]:
                if items[j][0] > items[j + 1][0]:
                    items[j], items[j + 1] = items[j + 1], items[j]

    result = []
    for i in range(min(k, len(items))):
        result.append(items[i][0])

    return result

#4
task4 = lambda s: " ".join(
    w.lower() for w in s.split()
    if sum(1 for ch in w if ch.isupper()) == 1
    and not (w[0].isupper() or w[-1].isupper())
)

#5
def compress_text(text):
    if not text:
        return ""

    result = []
    count = 1
    for i in range(1, len(text)):
        if text[i].lower() == text[i - 1].lower():
            count += 1
        else:
            result.append(text[i - 1] + (str(count) if count > 1 else ""))
            count = 1
    result.append(text[-1] + (str(count) if count > 1 else ""))
    return "".join(result)

#6
task6 = lambda s: [
    w for w in s.split() if len(w) >= 4
    and w.isalpha()
    and len(set(w)) == len(w)
]


#7
def palindrome_words(text):
    words = []
    for w in text.split():
        clean = ""
        for ch in w:
            if ch.isalpha():
                clean += ch.lower()
        if len(clean) >= 3 and clean == clean[::-1]:
            if clean not in words:
                words.append(clean)

    n = len(words)
    for i in range(n):
        for j in range(0, n - i - 1):
            if len(words[j]) < len(words[j + 1]):
                words[j], words[j + 1] = words[j + 1], words[j]
            elif len(words[j]) == len(words[j + 1]):
                if words[j] > words[j + 1]:
                    words[j], words[j + 1] = words[j + 1], words[j]

    return words


#8
vowels = "aeiouyаеёиоуыэюяAEIOUYАЕЁИОУЫЭЮЯ"
task8 = lambda s: " ".join(
    "VOWEL" if w.isalpha() and w[0].lower() in vowels.lower() else
    "CONSONANT" if w.isalpha() and w[0].lower() not in vowels.lower() else
    w
    for w in s.split()
)

#9
def alternate_case_blocks(text, n):
    blocks = []
    for i in range(0, len(text), n):
        blocks.append(text[i:i + n])

    result = []
    for i in range(len(blocks)):
        if i % 2 == 0:
            result.append(blocks[i].upper())
        else:
            result.append(blocks[i].lower())

    return "".join(result)

#10
task10 = lambda s: sum(
    1 for w in s.split()
    if any(ch.isdigit() for ch in w)
    and not w[0].isdigit()
    and len(w) >= 5
)


#11
def common_unique_chars(s1, s2):
    s2_chars = []
    for ch in s2:
        if ch.isalpha() and ch not in s2_chars:
            s2_chars.append(ch)

    result = []
    for ch in s1:
        if ch.isalpha() and ch not in result:
            for ch2 in s2_chars:
                if ch == ch2:
                    result.append(ch)
                    break

    return "".join(result)

#12
task12 = lambda s: [
    w for w in s.split()
    if w[0].lower() == w[-1].lower()
    and w.lower() != w[::-1].lower()
    and len(w) > 3
]


#13
def replace_every_nth(text, n, char):
    result = list(text)
    count = 0
    i = 0
    while i < len(text):
        if text[i] not in " 0123456789":
            count += 1
            if count % n == 0:
                start = i
                while start >= 0 and text[start] not in " 0123456789":
                    start -= 1
                end = i
                while end < len(text) and text[end] not in " 0123456789":
                    end += 1
                word_len = end - start - 1
                if word_len >= 3:
                    result[i] = char
        i += 1
    return "".join(result)


#14
vowels = "aeiouyаеёиоуыэюяAEIOUYАЕЁИОУЫЭЮЯ"
task14 = lambda s: ", ".join(
    w for w in s.split()
    if len(set(w)) > 3
    and len([ch for ch in w if ch in vowels]) == len(set(ch for ch in w if ch in vowels))
)

#15
def word_pattern_sort(text):
    vowels = "aeiouyаеёиоуыэюяAEIOUYАЕЁИОУЫЭЮЯ"
    words_by_len = {}

    for w in text.split():
        l = len(w)
        if l not in words_by_len:
            words_by_len[l] = []
        words_by_len[l].append(w)

    result = []
    for length in sorted(words_by_len.keys()):
        group = words_by_len[length]

        vowel_counts = []
        for word in group:
            count = 0
            for ch in word.lower():
                if ch in vowels.lower():
                    count += 1
            vowel_counts.append((word, count))

        n = len(vowel_counts)
        for i in range(n):
            for j in range(0, n - i - 1):
                if vowel_counts[j][1] < vowel_counts[j + 1][1]:
                    vowel_counts[j], vowel_counts[j + 1] = vowel_counts[j + 1], vowel_counts[j]
                elif vowel_counts[j][1] == vowel_counts[j + 1][1]:
                    if vowel_counts[j][0] > vowel_counts[j + 1][0]:
                        vowel_counts[j], vowel_counts[j + 1] = vowel_counts[j + 1], vowel_counts[j]

        for word, _ in vowel_counts:
            result.append(word)

    return result

# 16.1
def transform_list(nums):
    result = []
    for i in nums:
        if i < 0:
            continue
        if i % 2 == 0:
            result.append(i ** 2)
        elif i > 10:
            summa = 0
            x = i
            while x > 0:
                summa += x % 10
                x //= 10
            result.append(summa)
        else:
            result.append(i)
    return result


nums = list(map(int, input().split()))
print(transform_list(nums))

# 17.1
result = lambda nums: list(
    map(
        lambda x: x ** 2,
        filter(
            lambda x: (x % 3 == 0 or x % 5 == 0)
                      and x % 15 != 0
                      and len(str(abs(x))) % 2 == 1,
            nums
        )
    )
)

nums = list(map(int, input().split()))
print(result(nums))



# 18.1
def flatten_and_filter(lst):
    result = []

    def flatten(sublist):
        for item in sublist:
            if isinstance(item, list):
                flatten(item)
            elif isinstance(item, int):
                if (
                        item > 0 and
                        item % 4 != 0 and
                        len(str(item)) > 1
                ):
                    result.append(item)

    flatten(lst)
    result.sort()
    return result


data = [1, [12, -5, [33, 8], 44], [[101, 3], 16], 25]
print(flatten_and_filter(data))

# 19.1
result = lambda lst1, lst2: list(
    filter(
        lambda x: x % 2 == 0,
        map(
            lambda pair: pair[0],
            filter(
                lambda pair: pair[0] == pair[1],
                zip(lst1, lst2)
            )
        )
    )
)

print(result([2, 3, 4, 6, 8], [2, 5, 4, 7, 8]))



# 20.1
def max_subarray_sum(nums, k):
    if k > len(nums) or k <= 0:
        return None
    max_sum = None
    for i in range(len(nums) - k + 1):
        window = nums[i:i + k]
        valid = True
        current_sum = 0

        for num in window:
            if num <= 0:
                valid = False
                break
            current_sum += num

        if valid:
            if max_sum is None or current_sum > max_sum:
                max_sum = current_sum
    return max_sum


print(max_subarray_sum([1, 0, 3, -2, 5], 2))

# 21.1
result = lambda strings: list(
    map(
        lambda s: s.upper(),
        filter(
            lambda s: (
                    s.isalpha() and
                    len(s) > 4 and
                    len(set(s)) == len(s)
            ),
            strings
        )
    )
)

print(result(["Hello", "world", "Python", "abcde", "letter", "Code"]))


# %%
# 22.1
def group_by_parity_and_sort(nums):
    evens = []
    odds = []

    for num in nums:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)

    evens.sort()
    odds.sort()

    return evens + odds


print(group_by_parity_and_sort([7, 2, 5, 8, 1, 4, 3]))


# 23.1
result = lambda nums: list(
    filter(
        lambda pair: (
                pair[0] > 1 and
                all(pair[0] % i != 0 for i in range(2, int(pair[0] ** 0.5) + 1)) and
                pair[1] % 2 != 0 and
                pair[1] > (reduce(lambda a, b: a + b, nums) / len(nums))
        ),
        enumerate(nums)
    )
)

result = lambda nums: [
    value for index, value in
    filter(
        lambda pair: (
                pair[0] > 1 and
                all(pair[0] % i != 0 for i in range(2, int(pair[0] ** 0.5) + 1)) and
                pair[1] % 2 != 0 and
                pair[1] > (reduce(lambda a, b: a + b, nums) / len(nums))
        ),
        enumerate(nums)
    )
]

print(result([1, 7, 3, 9, 2, 11, 4, 13]))



# 24.1
def longest_increasing_sublist(nums):
    if not nums:
        return []

    max_sublist = []
    current_sublist = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current_sublist.append(nums[i])
        else:
            if len(current_sublist) > len(max_sublist):
                max_sublist = current_sublist
            current_sublist = [nums[i]]

    if len(current_sublist) > len(max_sublist):
        max_sublist = current_sublist

    return max_sublist


print(longest_increasing_sublist([1, 2, 3, 2, 3, 4, 1, 2]))


# 25.1
from functools import reduce

result = lambda lst: list(
    map(
        lambda sub: reduce(lambda a, b: a + b, sub) / len(sub),
        filter(
            lambda sub: len(sub) >= 3 and reduce(lambda a, b: a + b, sub) % 2 == 0,
            lst
        )
    )
)

print(result([[1, 2, 3], [2, 4, 6], [1, 1], [5, 5, 2]]))



# 26.1
def remove_duplicates_keep_last(nums):
    seen = []
    result_reversed = []

    for num in reversed(nums):
        if num not in seen:
            seen.append(num)
            result_reversed.append(num)

    result = []
    for num in reversed(result_reversed):
        result.append(num)

    return result


print(remove_duplicates_keep_last([1, 2, 3, 2, 4, 1, 5]))


# 27.1
result = lambda strings: sorted(
    strings,
    key=lambda s: (-len(s), s)
)[:5]

print(result(["apple", "banana", "kiwi", "cherry", "date", "fig", "grapefruit"]))



# 28.1
def moving_average(nums, k):
    if k <= 0 or k > len(nums):
        return []

    averages = []

    for i in range(len(nums) - k + 1):
        window = nums[i:i + k]

        if any(n < 0 for n in window):
            continue

        total = 0
        for n in window:
            total += n

        avg = total / k
        averages.append(avg)

    return averages


print(moving_average([1, 2, 3, -1, 4, 5, 6], 3))

# 29.1
result = lambda lst1, lst2: list(
    filter(
        lambda x: x > (sum(lst1) / len(lst1)) and x not in lst2,
        lst1
    )
)

print(result([1, 4, 6, 8, 10], [4, 10]))


# 30.1
def analyze_strings_list(words):
    seen = set()
    result = []

    for word in words:
        if any(char.isdigit() for char in word):
            continue

        if len(word) % 2 == 0:
            processed = word[::-1]
        else:
            processed = word.upper()

        if processed not in seen:
            seen.add(processed)
            result.append(processed)

    return result


words = ["hello", "world1", "python", "code", "hello", "data", "AI2"]
print(analyze_strings_list(words))




#1 Dictionary
def analyze_text(text):
    text1 = text.lower()
    text2 = ""
    for alpha in text1:
        if isalpha1(alpha) or alpha == "":
            text2 += alpha
    dauysty = "aeiouy"
    new = ""
    for alpha in text2:
        if alpha in dauysty:
            new += alpha
    text3 = text2.split()


#1(dict and set)
def invert_unique(d):
    res = {}
    for key, value in d.items():
        if value not in res:
            res[value] = []
        if key not in res[value]:
            res[value].append(key)
    return res
d1 = {"a" : 1, "b" : 2, "c" : 1, "d" : 3}
print(invert_unique(d1))

#2
def calculate_average(nums):
    if not nums:
        return 0
    total = 0
    count = 0
    for num in nums:
        total += num
        count += 1
    return total / count

filter_numbers = lambda nums: {
    num for num in nums
    if num > calculate_average(nums)
    and num % 2 != 0
    and num % 5 != 0
}

s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(filter_numbers(s1))

#3
def merge_dicts_sum(d1, d2):
    res = {}
    for key in d1:
        res[key] = d1[key]
    for key in d2:
        key_exists = False
        for result_key in res:
            if key == result_key:
                key_exists = True
                break
        if key_exists:
            res[key] = res[key] + d2[key]
        else:
            res[key] = d2[key]
    return res

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print(merge_dicts_sum(dict1, dict2))

#4
def filter_sets(sets_list):
    res = []
    for set in sets_list:
       if len(set) > 3:
           negative = False
           even_number = False
           for num in set:
               if num < 0:
                   negative = True
               if num % 2 == 0:
                   even_number = True
           if even_number and not negative:
                res.append(set)
    return res

sets = [
    {1, 2, 3, 4},
    {-1, 2, 3, 4, 5},
    {1, 3, 5, 7},
    {1, 2, 3},
    {2, 4, 6, 8, 10},
    {0, 1, 2, 3, -5},
    {10, 20, 30, 40},
]
print(filter_sets(sets))

#5
dict_sorted = lambda d:(

)

#6
def deep_sum(d):
    total = 0
    for value in d.values():
        if type(value) == int or type(value) == float:
            total += value
        elif type(value) == list:
            for x in value:
                if type(x) == int or type(x) == float:
                    total += x
        elif type(value) == dict:
            total += deep_sum(value)
    return total

print(deep_sum({
    'a': 1, 'b': 2, 'c': [3, 4], 'd': {"e": 1, "f": 4}
}))

#7
task_7 = lambda s1, s2: {x for x in (s1 ^ s2) if x % 2 == 0}
A = {1, 2, 3, 4, 5}
B = {1, 3, 6, 9, 12}
print(task_7(A, B))

#8
def sort_dict_by_value_length(d):
    items = list(d.items())
    for i in range(len(items)):
        for j in range(len(items) - 1):
            if (len(items[j][1]) > len(items[j + 1][1])) or \
                    (len(items[j][1]) == len(items[j + 1][1]) and items[j][0] > items[j + 1][0]):
                items[j], items[j + 1] = items[j + 1], items[j]
    return items
res5 = {
    "a" : "hello",
    "b" : "world!",
    "c" : "Naz",
    "d" : "Diana",
    "e" : "Maral",
    "f" : "Zere"
}
print(sort_dict_by_value_length(res5))

#9
def common_elements_all(sets_list):
    if len(sets_list) == 0:
        return set()
    res = set()
    first_set = sets_list[0]

    for element in first_set:
        in_all = True

        for s in sets_list:
            if element not in s:
                in_all = False
                break

        if in_all:
            res.add(element)
    return res
res6 = [
    (1, 2, 3),
    (3, 4, 5, 2),
    (3, 2, 6)
]
print(common_elements_all(res6))

#10
def filter_lists(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
filter_dict10 = lambda d: {
    k: filter_lists([x for x in v if x%2 != 0])
    for k,v in d.items()
    if len([x for x in v if x % 2 != 0]) > 0
}
task_10 = {
    "a" : [1, 2, 3, 4],
    "b" : [1, 2, 3, 5],
    "c" : [3, 6, 9, 12]
}
print(filter_dict10(task_10))

#11
def group_by_length(words):
    res = {}
    for word in words:
        length = len(word)
        if length not in res:
            res[length] = []
        res[length].append(word)
    return res

task_11 = ["apple", "Almaty", "Nazerke"]
print(group_by_length(task_11))

#12
filter_strings = lambda s: {
    x for x in s
    if len(x) > 4
    and len({c for c in x}) == len(x)
    and all(('a' <= c <= 'z') or ('A' <= c <= 'Z') for c in x)
}

task_12 = {"apple", "Nazerke", "Ersultan", "house"}
print(filter_strings(task_12))

#13
def invert_dict_strict(d):
    counts = {}
    for v in d.values():
        if v in counts:
            counts[v] += 1
        else:
            counts[v] = 1
    res = {}
    for k, v in d.items():
        if counts[v] == 1:
            res[v] = k
    return res
task_13 = {
    "1" : "Naz",
    "2" : "Botagoz",
    "3" : "Botagoz",
    "4" : "Diana",
    "5" : "Zere",
    "6" : "Maral"
}
print(invert_dict_strict(task_13))

#14
def top_k_frequent(nums, k):
    res = set()
    count = 0
    x = {}
    for num in nums:
        if num in x:
            x[num] += 1
        else:
            x[num] = 1
    while count < k and len(x) > 0:
        best_num = None
        best = -1
        for num in x:
            if x[num] > best:
                best = x[num]
                best_num = num
            elif x[num] == best and num < best_num:
                best_num = num
        res.add(best_num)
        del x[best_num]
        count += 1
    return res

task_14 = [1, 1, 1, 3, 2, 4, 3]
print(top_k_frequent(task_14, 2))

#15
def filter_dict(d):
    total = 0
    count = 0
    for key in d:
        total += d[key]
        count += 1
    avg = total / count
    f = lambda d: {k: d[k] for k in d if d[k] >= avg and d[k] % 2 != 0}
    return f(d)

task_15 = {
    "Naz": 17,
    "Maral" : 13,
    "Diana" : 18,
    "Zere" : 12,
    "Botagoz" : 20

}
print(filter_dict(task_15))


#16
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

#33
filter_by_avg=lambda a:(
    lambda avg:{
        i:j
        for i,j in a.items()
        if sum(j)/len(j)>avg
    }
)(
    sum(sum(j) for j in a.values())/
    sum(len(j) for j in a.values())
    if a and sum(len(j) for j in a.values())>0 else 0
)
data={
    "a":[10,20,30],
    "b":[1,2,3],
    "c":[40,50]
}
print(filter_by_avg(data))

#34
def top_k_smallest_unique(a,b):
    unique=[]
    for i in a:
        if i not in unique:
            unique.append(i)
    j=0
    while j<len(unique):
        index=j
        k=j+1
        while k<len(unique):
            if unique[k]<unique[index]:
                index=k
            k+=1
        temp=unique[j]
        unique[j]=unique[index]
        unique[index]=temp
        j+=1
    result=set()
    count=0
    for i in unique:
        if count<b:
            result.add(i)
            count+=1
    return result
a=list(map(int,input().split()))
b=int(input())
print(top_k_smallest_unique(a,b))

#35
filter_dict2=lambda a:{
    i:j for i,j in a.items()
    if not (j%3==0 or len(i)%2==0)
}
data={
    "one":4,
    "two":9,
    "four":5,
    "cat":6,
    "hello":7
}
print(filter_dict2(data))

#36
def all_subsets_of_size_k(a,b):
    result=[]
    elems=[]
    for i in a:
        elems.append(i)
    def backtrack(c,d):
        if len(d)==b:
            e=set()
            for j in d:
                e.add(j)
            result.append(e)
            return
        k=c
        while k<len(elems):
            d.append(elems[k])
            backtrack(k+1,d)
            d.pop()
            k+=1
    backtrack(0,[])
    return result
a=list(map(int,input().split()))
b=int(input())
print(all_subsets_of_size_k(a,b))

#37
fact=lambda a:1 if a<=1 else a*fact(a-1)
transform=lambda b:{
    i:fact(j) if j<6 else j
    for i,j in b.items()
}
data= {
    "a":3,
    "b":5,
    "c":6,
    "d":2
}
print(transform(data))

#38
def multi_symmetric_difference(a):
    if len(a)==0:
        return []
    result=set()
    for i in a:
        new=set()
        for j in result:
            if j not in i:
                new.add(j)
        for j in i:
            if j not in result:
                new.add(j)
        result=new
    return result
a={1,2,3}
b={3,4,5}
c={5,6}
print(multi_symmetric_difference([a,b,c]))

#39
sort_keys=lambda a: sorted(
    a.keys(),
    key=lambda b:(
        sum(1 for i in b.lower() if i in "oiuyea"),
        -a[b]
    )
)
data={
    "apple":5,
    "sky":10,
    "orange":3,
    "grape":8
}
print(sort_keys(data))

#40
def analyze_dict_keys(a):
    result=set()
    punct=".,!@#$%^&*()[]{}<>?""''/\|+-*_=`~:;"
    for i in a:
        if type(i)==str:
            digit=False
            for j in i:
                if "0"<=j<="9":
                    digit=True
                    break
            if not digit:
                for j in i:
                    if j !=" " and j not in punct:
                        result.add(j)
    return result
data={
    "hello world":1,
    "test123":2,
    "good-day!":3,
    100:"number"
}
print(analyze_dict_keys(data))

#Big Data 1
def analyze_students(a):
    students=[]
    count={}
    all_vowels=[]
    vowels="oiuyea"
    k=0
    while k<len(a):
        name=a[k]["name"]
        digit=False
        for i in name:
            if "0"<=i<="9":
                digit=True
                break
            if digit:
                k+=1
                continue
            name=name.title()
            grades=a[k]["grades"]
            pro=[]
            j=0
            while j<len(grades):
                g=grades[j]
                if g<=0:
                    j+=1
                    continue
                if g%2==1 and g<10:
                    s=0
                    n=g
                    while n>0:
                        s+=n%10
                        n//=10
                    pro.append(s)
                elif g%2==0 and g>=10:
                    pro.append(g*g)
                else:
                    pro.append(g)
                j+=1
        text=" ".join(a[k]["comments"]).lower()
        word=text.split()
        unique=[]
        for w in word:
            if len(w)>=4 and w!=w[::-1]:
                exis=False
                for v in unique:
                    if v==w:
                        exis=True
                if not exis:
                    unique.append(w)
        for w in unique:
            if w in count:
                count[w]+=1
            else:
                count[w]=1
            for i in w:
                for t in vowels:
                    if i.lower()==t:
                        found=False
                        for v in all_vowels:
                            if v==t:
                                found=True
                        if not found:
                            all_vowels.append(t)
        students.append({
            "name":name,
            "processed":pro
        })
        k+=1
    return {
        "students":students,
        "count":count,
        "all_vowels":all_vowels
    }
data=[
    {
        "name":"Nazerke123",
        "grades":[12,9,15,8],
        "comments":["Good work","excellent effort","Needs Improvement"]
    },
    {
        "name":"Diana",
        "grades":[10,5,-2,7],
        "comments":["Good job","very nice work","level"]
    },
    {
        "name":"Maral",
        "grades":[14,3,11],
        "comments":["Excellent progress","Good work"]
    }
]
print(analyze_students(data))


#Big Data 2
def analyze_orders(a):
    pro_order=[]
    count={}
    all_vowels=[]
    unique=[]
    vowels="oiuyea"
    k=0
    while k<len(a):
        order=a[k]
        customer=order["customer"]
        digit=False
        for i in customer:
            if "0"<=i<="9":
                digit=False
                break
        if digit:
            k+=1
            continue
        costomer=customer.title()
        pro=[]
        summa=0
        j=0
        while j<len(order["items"]):
            item=order["items"][j]
            name=item["name"]
            price=item["price"]
            quantity=item["quantity"]
            if price <=0:
                j+=1
                continue
            if quantity%2==1:
                n=int(price)
                summa=0
                while n>0:
                    summa+=n%10
                    n//=10
                price=price+summa
            pro.append({
                "name":name,
                "price":price
            })
            summa+=price
            exis=False
            c=0
            while c<len(unique):
                if unique[c]==name:
                    exis=True
                c+=1
            if not exis:
                unique.append(name)
            j+=1
        text=" ".join(order["notes"])
        words=text.split()
        un_word=[]
        j=0
        while j<len(words):
            w=words[j]
            if len(w)>=4 and w!=w[::-1]:
                exis=False
                c=0
                while c<len(un_word):
                    if un_word[c]==w:
                        exis=True
                    c+=1
                if not exis:
                    un_word.append(w)
            j+=1
        j=0
        while j<len(un_word):
            w=un_word[j]
            if w in count:
                count[w]+=1
            else:
                count[w]=1
            m=0
            while m<len(w):
                i=w[m].lower()
                index=0
                while index<len(vowels):
                    if i==vowels[index]:
                        found=False
                        t=0
                        while t<len(all_vowels):
                            if all_vowels[t]==vowels[index]:
                                found=True
                            t+=1
                        if not found:
                            all_vowels.append(vowels[index])
                    index+=1
                m+=1
            j+=1
        pro_order.append({
            "order_id":order["order_id"],
            "customer":customer,
            "pro":pro,
            "total":summa
        })
        k+=1
    filtered={}
    for w in count:
        if count[w]>=2:
            filtered[w]=count[w]
    k=0
    while k<len(pro_order):
        best=k
        j=k+1
        while j<len(pro_order):
            if pro_order[j]["total"]>pro_order[best]["total"]:
                best=j
            elif pro_order[j]["total"]==pro_order[best]["total"]:
                if pro_order[j]["order_id"]<pro_order[best]["order_id"]:
                    best=j
            j+=1
        temp=pro_order[k]
        pro_order[k]=pro_order[best]
        pro_order[best]=temp
        k+=1
    or_total=[]
    k=0
    while k<len(pro_order):
        or_total.append(pro_order[k]["order_id"])
        k+=1
    or_item={}
    k=0
    while k<len(pro_order):
        amount=len(pro_order[k]["pro"])
        if amount in or_item:
            or_item[amount].append(pro_order[k]["order_id"])
        else:
            or_item[amount]=[pro_order[k]["order_id"]]
        k+=1
    return {
        "orders":pro_order,
        "word_counts":filtered,
        "all_vowels":all_vowels,
        "unique_products":unique,
        "orders_by_total":or_total,
        "orders_by_item_count":or_item
    }
data=[
    {
        "order_id":"A123",
        "customer":"maral_doe08",
        "items":[
            {"name":"Laptop","price":999.99,"quantity":1},
            {"name":"Mouse2","price":25,"quantity":2}
        ],
        "notes":["Nazerke TASTA","fragile package","handle with care"]
    },
    {
        "order_id":"B456",
        "customer":"diana_smith",
        "items":[
            {"name":"Manitor","price":200,"quantity":2},
            {"name":"Keyboard","price":50,"quantity":1}
        ],
        "notes":["Tumar with care","fast delivery"]
    },
    {
        "order_id":"C789",
        "customer":"nurshat",
        "items":[
            {"name":"Laptop","price":900,"quantity":2}
        ],
        "notes":["fragile package","deliver tomorrow"]
    }
]
print(analyze_orders(data))

