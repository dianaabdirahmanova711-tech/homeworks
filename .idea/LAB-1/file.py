#1
import csv

with open("file.txt","w",encoding="utf-8") as f:
    f.write("Hello Diana\n")
    f.write("Hi Nazerke\n")

#2
with open("second.txt","w",encoding="utf-8") as f:
    for i in range(1,11):
        f.write(str(i)+"\n")
with open("second.txt","r",encoding="utf-8") as f:
    print(f.read())
#3
names=["diana","nazerke","maral"]
with open("names.txt","w",encoding="utf-8") as f:
    for name in names:
        f.write(name+"\n")
with open("names.txt","r",encoding="utf-8") as f:
    for line in f:
        print(line.strip().capitalize())

#4
import csv
info=[
    ["name", "age", "city"],
    ["Diana", "18", "Almaty"],
    ["Maral", "17", "Astana"]
]
with open("students.csv","w",newline="",encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(info)


#2task
import csv
employs=[]
with open("employees.csv","r",newline="",encoding="utf-8") as f:
    reader=csv.DictReader(f)
    for i in reader:
        i["salary"]=int(i["salary"])
        employs.append(i)
total_salary=sum(emp["salary"] for emp in employs)
average_salary=total_salary/len(employs)
print(f"Орташа жалақы: {average_salary:.2f}")

departments=[]
for n in employs:
    a=n["department"]
    if a not in departments:
        departments[a]=[]
    departments[a].append(n["salary"])

dept_averages={}
for a,salaries in departments.items():
    orta=sum(salaries)/len(salaries)
    dept_averages[a]=orta
    print(f"{a} орташа жалақысы: {orta:.2f}")

kop_jalaky=