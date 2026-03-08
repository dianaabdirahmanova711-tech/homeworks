
import csv

file = open("employeess.csv", "r")
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

high_employee = ""
high_salary = 0
for emp in employees:
    salary = int(emp["salary"])
    if salary > high_salary:
        high_salary = salary
        high_employee = emp["name"]

high_earners = []
for emp in employees:
    if int(emp["salary"]) > average:
        high_earners.append(emp)

print("орташа жалақы:"  + str(average))
print("бөлімдегі орташа жалақы:")
for dept in dept_averages:
    print("  " + dept + ": " + str(dept_averages[dept]))
print("үздік бөлім: " + best_dept)
print("үздік қызметкер: " + high_employee + " (" + str(high_salary) + ")")
print("орташадан жоңары алғандар (" + str(len(high_earners)) + "):")
for emp in high_earners:
    print("  " + emp["name"] + " - " + emp["salary"])

report = open("high_salaryy.csv", "w", encoding="utf-8")
for emp in high_earners:
    report.write(emp["name"] + "," + emp["department"] + "," + emp["salary"] + "\n")
report.close()


