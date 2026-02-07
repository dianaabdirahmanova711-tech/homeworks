def analyz_text(text):
    text1=text.lower()
    text2=""
    for i in text1:
        if i.isalpha() or i=="":
            text2+=i
        dauysty="aeioy"
        new_text=""
        for i in text2:
            if i in dauysty:
                new_text+=i
        text3=text2.split()
        result=""
        text4=''
        for word in text3:
            if len(word)>=5:
                if word[0]==word[-1]:
                    if word not in result:
                        result+=word+""
                        text4+=word+","+""
                        return {"дауысты әріптер:":set(new_text),
                                "дауысты әріптер саны:":len(set(new_text))
                                "слова длиной>=5":text4
                                "жауабы:":result}
matin=input()
print(analyz_text(matin))