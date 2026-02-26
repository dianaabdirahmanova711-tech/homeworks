#1
import json

file= open("shop_logs.txt", "r")
unique_users=set() #пользователи
total_purchases=0 #кол-во покупок
total_sum=0 #общая сумма
user_spending={}
for line in file:

    lines=line.strip().split(";")
    if len(lines) < 3:
        continue
    user_id=lines[1]
    print(user_id)
    action=lines[2]
    unique_users.add(user_id)
    if action=="BUY":
        total_purchases+=1
        amount=int(lines[3])
        total_sum+=amount
        if user_id not in user_spending:
            user_spending[user_id]=amount
        else:
            user_spending[user_id]+=amount
file.close()
max_user=""
max_spent=0
for user in user_spending:
    if user_spending[user]>max_spent:
        max_user=user
        max_spent=user_spending[user]
if total_purchases>0:
    total_average=total_sum/total_purchases
else:
    total_average=0
report=open("shop_log.txt","w",encoding="utf-8")
report.write("Уникальных пользователей:" + str(len(unique_users)) + "\n")
report.write("Кол-во покупок:"+str(total_purchases)+"\n")
report.write("Общая сумма:"+str(total_sum)+"\n")
report.write("Cамы активный покупатель:"+str(max_user)+"\n")
report.write("Средний чек:"+str(total_average)+"\n")
report.close()
print("Отчет успешно создан!")


#2task
import csv

file = open("employees.csv", "r")
reader = csv.DictReader(file)

employees = []
for row in reader:
    employees.append(row)

file.close()

total_salary = 0
for emp in employees:
    total_salary += int(emp["salary"])
average = total_salary / len(employees)

departments = {}
for emp in employees:
    dept = emp["department"]
    salary = int(emp["salary"])

    if dept not in departments:
        departments[dept] = {"total": 0, "count": 0}

    departments[dept]["total"] += salary
    departments[dept]["count"] += 1

dept_averages = {}
for dept in departments:
    dept_averages[dept] = departments[dept]["total"] / departments[dept]["count"]

best_dept = ""
best_avg = 0
for dept in dept_averages:
    if dept_averages[dept] > best_avg:
        best_avg = dept_averages[dept]
        best_dept = dept

top_employee = ""
top_salary = 0
for emp in employees:
    salary = int(emp["salary"])
    if salary > top_salary:
        top_salary = salary
        top_employee = emp["name"]

high_earners = []
for emp in employees:
    if int(emp["salary"]) > average:
        high_earners.append(emp)

print("ОРТАША ЖАЛАҚЫ: " + str(average))
print("БӨЛІМДЕР БОЙЫНША ОРТАША:")
for dept in dept_averages:
    print("  " + dept + ": " + str(dept_averages[dept]))
print("ҮЗДІК БӨЛІМ: " + best_dept)
print("ҮЗДІК ҚЫЗМЕТКЕР: " + top_employee + " (" + str(top_salary) + ")")
print("ОРТАШАДАН ЖОҒАРЫ АЛАТЫНДАР (" + str(len(high_earners)) + "):")
for emp in high_earners:
    print("  " + emp["name"] + " - " + emp["salary"])

report = open("high_salary.csv", "w", encoding="utf-8")
for emp in high_earners:
    report.write(emp["name"] + "," + emp["department"] + "," + emp["salary"] + "\n")
report.close()

print("\n✅ high_salary.csv файлы құрылды!")


#3task
import json
file=open("orders.json","r")
data=json.load(file)
file.close()


total_sum=0
user_orders={}
item_list=[]
order_details=[]
max_order_value=0
top_user_by_order=""
for order in data:
    total_sum+=order["total"]
    user=order["user"]
    if user in user_orders:
        user_orders[user]+=1
    else:
        user_orders[user]=1

    for item in order["items"]:
        item_list.append(item)

    order_details.append({
        "user": user,
        "total": order["total"],
    })
total_items_sold=len(item_list)

for order in order_details:
    if order["total"]>max_order_value:
        max_order_value=order["total"]
        top_user_by_order=order["user"]

item_count={}
for item in item_list:
    if item in item_count:
        item_count[item]+=1
    else:
        item_count[item]=1

most_popular_item=""
max_count=0
for item,count in item_count.items():
    if count>max_count:
        max_count=count
        most_popular_item=item

print("=" * 50)
print("ЕСЕПТЕУ НӘТИЖЕЛЕРІ")
print("=" * 50)

print(f"1. Барлық тапсырыстардың жалпы сомасы: {total_sum} теңге")

print("\n2. Әр пайдаланушының тапсырыс саны:")
for user, count in user_orders.items():
    print(f"   - {user}: {count} тапсырыс")

print(f"\n3. Барлығы сатылған тауарлар саны: {total_items_sold} дана")

print(f"\n4. Ең қымбат тапсырыс жасаған пайдаланушы: {top_user_by_order}")
print(f"   Тапсырыс сомасы: {max_order_value} теңге")

print(f"\n5. Ең популярлы тауар: '{most_popular_item}' ({max_count} рет сатылған)")
summary = {
    "total_revenue": total_sum,
    "top_user": top_user_by_order,
    "most_popular_item": most_popular_item,
    "total_orders": len(data)
}

with open("summary.json", "w", encoding="utf-8") as file:
    json.dump(summary, file, ensure_ascii=False, indent=2)

print("\n✅ 'summary.json' файлы сәтті құрылды!")


#4task

import csv
import json

transactions = []
with open("transactions.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["amount"] = int(row["amount"])
        transactions.append(row)

suspicious_transactions = []
user_transaction_count = {}
suspicious_users = set()
total_suspicious_amount = 0

for transaction in transactions:
    user = transaction["user_id"]
    amount = transaction["amount"]

    if user in user_transaction_count:
        user_transaction_count[user] += 1
    else:
        user_transaction_count[user] = 1

    if amount > 500000:
        suspicious_transactions.append(transaction)
        total_suspicious_amount += amount

for user, count in user_transaction_count.items():
    if count > 3:
        suspicious_users.add(user)

print("=" * 50)
print("АНТИФРОД ЖҮЙЕСІ - ЕСЕПТЕУ НӘТИЖЕЛЕРІ")
print("=" * 50)

print(f"Подозрительных транзакций: {len(suspicious_transactions)}")
for t in suspicious_transactions:
    print(f"  - {t['user_id']}: {t['amount']}")

print(f"\nПодозрительных пользователей: {len(suspicious_users)}")
print(f"Список пользователей: {', '.join(suspicious_users) if suspicious_users else 'жоқ'}")

print(f"\nОбщая сумма подозрительных операций: {total_suspicious_amount}")

with open("fraud_report.txt", "w", encoding="utf-8") as report:
    report.write("Подозрительных транзакций: " + str(len(suspicious_transactions)) + "\n")
    report.write("Подозрительных пользователей: " + str(len(suspicious_users)) + "\n")
    report.write("Список пользователей: " + (', '.join(suspicious_users) if suspicious_users else '') + "\n")
    report.write("Общая сумма подозрительных операций: " + str(total_suspicious_amount) + "\n")

fraud_data = {
    "suspicious_users": list(suspicious_users),
    "suspicious_transactions_count": len(suspicious_transactions),
    "total_suspicious_amount": total_suspicious_amount
}

with open("fraud_users.json", "w", encoding="utf-8") as file:
    json.dump(fraud_data, file, ensure_ascii=False, indent=2)

print("\n✅ fraud_report.txt файлы құрылды!")
print("✅ fraud_users.json файлы құрылды!")


