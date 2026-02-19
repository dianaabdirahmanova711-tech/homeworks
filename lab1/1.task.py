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
def update_counts(d, items):
    for item in items:
        if d in item:
            d[item] += 1
        else:
            d[item] = 1
    return d
d={"apple":2,"banana":3}
items = ["apple","banana"]
n=update_counts(d, items)
print(n)

#17



