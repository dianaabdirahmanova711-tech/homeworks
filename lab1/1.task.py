def analyze_text(text):
    words, letters, w = [], [], ""
    for ch in text:
        if 'A' <= ch <= 'Z':
            ch = chr(ord(ch) + 32)
        if 'a' <= ch <= 'z':
            w += ch
            letters.append(ch)
        elif w:
            words.append(w)
            w = ""
    if w: words.append(w)
    vowels = "aeiou"
    uniq_v = []
    for l in letters:
        is_v = False
        for v in vowels:
            if l == v:
                is_v = True
                break
        if is_v:
            found = False
            for uv in uniq_v:
                if uv == l:
                    found = True
                    break
            if not found:
                uniq_v.append(l)
    res, seen = [], []
    for w in words:
        l = 0
        for _ in w: l += 1
        if l < 5: continue
        if w[0] != w[-1]: continue
        dup = False
        for s in seen:
            if s == w:
                dup = True
                break
        if not dup:
            seen.append(w)
            res.append(w)
    out = ""
    for i in range(len(res)):
        if i: out += " "
        out += res[i]
    return (len(uniq_v), out)


#Dictionary16
#def update_counts(d, items):
    for item in items:
        if d in item:
            d[item] += 1
        else:
            d[item] = 1
    return d
#d={"apple":2,"banana":3}
#items = ["apple","banana"]
#n=update_counts(d, items)
#print(n)

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


