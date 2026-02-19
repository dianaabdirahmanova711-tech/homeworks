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
