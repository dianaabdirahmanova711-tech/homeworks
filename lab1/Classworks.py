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
    writer.writerows(info) get init

    import json

    file = open("shop_logs.txt", "r")
    unique_users = set()  # пользователи
    total_purchases = 0  # кол-во покупок
    total_sum = 0  # общая сумма
    user_spending = {}
    for line in file:

        lines = line.strip().split(";")
        if len(lines) < 3:
            continue
        user_id = lines[1]
        print(user_id)
        action = lines[2]
        unique_users.add(user_id)
        if action == "BUY":
            total_purchases += 1
            amount = int(lines[3])
            total_sum += amount
            if user_id not in user_spending:
                user_spending[user_id] = amount
            else:
                user_spending[user_id] += amount
    file.close()
    max_user = ""
    max_spent = 0
    for user in user_spending:
        if user_spending[user] > max_spent:
            max_user = user
            max_spent = user_spending[user]
    if total_purchases > 0:
        total_average = total_sum / total_purchases
    else:
        total_average = 0
    report = open("shop_log.txt", "w", encoding="utf-8")
    report.write("Уникальных пользователей:" + str(len(unique_users)) + "\n")
    report.write("Кол-во покупок:" + str(total_purchases) + "\n")
    report.write("Общая сумма:" + str(total_sum) + "\n")
    report.write("Cамы активный покупатель:" + str(max_user) + "\n")
    report.write("Средний чек:" + str(total_average) + "\n")
    report.close()
    print("Отчет успешно создан!")

    # 2task
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

    # 3task
    import json

    file = open("orders.json", "r")
    data = json.load(file)
    file.close()

    total_sum = 0
    user_orders = {}
    item_list = []
    order_details = []
    max_order_value = 0
    top_user_by_order = ""
    for order in data:
        total_sum += order["total"]
        user = order["user"]
        if user in user_orders:
            user_orders[user] += 1
        else:
            user_orders[user] = 1

        for item in order["items"]:
            item_list.append(item)

        order_details.append({
            "user": user,
            "total": order["total"],
        })
    total_items_sold = len(item_list)

    for order in order_details:
        if order["total"] > max_order_value:
            max_order_value = order["total"]
            top_user_by_order = order["user"]

    item_count = {}
    for item in item_list:
        if item in item_count:
            item_count[item] += 1
        else:
            item_count[item] = 1

    most_popular_item = ""
    max_count = 0
    for item, count in item_count.items():
        if count > max_count:
            max_count = count
            most_popular_item = item

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

    # 4task

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

    # Lambda_function
    # 1task
    from selectors import SelectSelector

    a = lambda x: "positive" if x > 0 else "negative" if x < 0 else "zero"
    print(a(3))
    print(a(-5))
    print(a(0))

    # 2task
    words = ["арбуз", "кот", "машина", "дом", "ананас"]
    a = sorted(words, key=lambda word: len(word))
    print(a)

    # 3task
    numbers = [5, 12, 7, 20, 33, 8]
    a = list(filter(lambda x: x % 2 == 0 and x > 10, numbers))
    print(a)

    # 4task
    numbers = [1, 2, 3, 4, 5, 6]
    a = list(map(lambda x: x * x if x % 2 == 0 else x * 3 if x % 2 != 0 else x, numbers))
    print(a)

    # 5task
    c = lambda a, b: "а больше " if a > b else "б больше" if a < b else "равны"
    print(c(10, 9))
    print(c(-3, 8))
    print(c(3, 3))

    # 6task
    numbers = [0, -3, 5, -7, 8]
    a = lambda x: "положительное" if x > 0 else "отрицательное" if x < 0 else "ноль"
    b = [a(x) for x in numbers]
    print(b)

    # Итераторы и comprehension
    # 1task
    a = []
    for i in range(1, 20 + 1):
        if i % 2 == 0:
            a.append(i)
    print(a)

    # 2task
    from functools import reduce

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = [reduce(lambda x, y: x * y, row) for row in matrix]
    print(result)

    # 3task
    words = ["кот", "машина", "ананас", "дом"]
    a = [x for x in words if len(x) > 4 and "а" not in x]
    print(a)

    # 4task
    numbers = [1, 2, 3, 4, 5]
    a = ["четное" if x % 2 == 0 else "нечетное" for x in numbers]
    print(a)

    # 5task
    matrix = [[1, 2], [3, 4], [5, 6]]
    a = [x for row in matrix for x in row]
    print(a)

    # 6task
    result = ["FizzBizz" if x % 3 == 0 and x % 5 == 0 else
              "Fizz" if x % 3 == 0 else
              "Bizz" if x % 5 == 0 else x
              for x in range(1, 21)]
    print(result)


    # Смешанные сложные задачи
    # 1task
    def special_numbers(n):
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                yield "FizzBizz"
            if i % 5 == 0:
                yield "Fizz"
            elif i % 3 == 0:
                yield "Bizz"
            else:
                yield i


    for i in special_numbers(15):
        print(i)

    # 2task
    words = ["кот", "машина", "арбуз", "дом", "ананас"]
    process = lambda w: (w.upper() if len(w) > 4 else "short") + ("*" if "а" in w else "")
    result = [process(word) for word in words]
    print(result)


    # 3task

    def process_numbers(numbers):
        a = filter(lambda x: "" if x < 0 else "0", numbers)
        evens = map(lambda x: x / 2 if x % 2 == 0 else x * 3 + 1, a)
        return list(evens)


    numbers = [5, -2, 8, 0, -7, 3]
    for num in process_numbers(numbers):
        print(num)

    # 4task
    students = [("Иван", 85), ("Анна", 72), ("Пётр", 90), ("Мария", 60)]
    nums = [score for name, score in students]
    a = lambda x: "Отлично" if x >= 90 else "Хорошо" if 70 <= x < 90 else "Удовлетворительно"
    b = {name: a(score) for name, score in students}
    print(b)


    # 5task
    def matrix_transform(matrix):
        result = (
            "кратно 6" if x % 6 == 0 else
            "четное" if x % 2 == 0 else
            "кратно 3" if x % 3 == 0 else
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

    # Задачи для понимания map and filter
    # 1task
    numbers = [5, -2, 8, 0, -7, 3]
    a = list(map(lambda x: x * 2, numbers))
    print(a)

    # 2task
    words = ["diana", "zere", "maral", "ana"]
    a = list(map(lambda x: x.upper() + "!" if len(x) > 3 else x.upper(), words))
    print(a)

    # 3task
    numbers = [5, -2, 8, -7, 3, 6]
    a = list(filter(lambda x: x % 2 == 0, numbers))
    print(a)

    # 4task
    numbers = [0, 5, 12, 7, 20, -3, 8]
    b = list(map(lambda x: x * 0.5 if x % 2 == 0 else x * 3, numbers))
    a = list(filter(lambda x: x > 5, b))
    print(a)


    # generator
    # 1task
    def even_numbers(n):
        for i in range(1, n + 1):
            if i % 2 == 0:
                if i % 4 == 0:
                    yield "Кратно 4"
                else:
                    yield i


    for x in even_numbers(10):
        print(x)


    # 2task
    def filter_words(words):
        for word in words:
            if len(word) > 4:
                if "а" in word:
                    yield "с а"


    words = ["кот", "машина", "арбуз", "дом"]
    for w in filter_words(words):
        print(w)


    # 3task
    def infinite_numbers():
        i = 1
        while i >= 1:
            if i % 15 == 0:
                yield "FizzBizz"
            if i % 5 == 0:
                yield "Fizz"
            if i % 3 == 0:
                yield "Bizz"
            else:
                yield i
            i += 1


    count = 0
    for num in infinite_numbers():
        print(num, end="")
        count += 1
        if count >= 15:
            break


    # 4task
    def squares(n):
        for i in range(1, n + 1):
            if i % 2 == 0:
                yield "Четный квадрат"
            else:
                yield i


    for x in squares(10):
        print(x)