from art import *
tprint("Dikosha",font="bear")
tprint("Nazerke",font="cards")
tprint("cola",font="cola")
aprint("butterfly")
aprint("angry ")




import random

# =========================
# INITIAL STATS
# =========================
money = 50
health = 100
mood = 100

print("🎮 СИМУЛЯТОР ЖИЗНИ НАЧАЛСЯ!\n")

# =========================
# GAME LOOP
# =========================
for day in range(1, 11):
    print(f"\n📅 День {day}")
    print(f"💰 Деньги: {money} | ❤️ Здоровье: {health} | 😊 Настроение: {mood}")

    event = random.choice(["work", "illness", "find_money", "rest"])

    # =========================
    # EVENTS
    # =========================
    if event == "work":
        print("💼 Событие: Работа")
        money += 20
        mood -= 10
        print("Ты поработал и получил +20 денег, но устал 😓")

    elif event == "illness":
        print("🤒 Событие: Болезнь")
        health -= 20
        mood -= 15
        print("Ты заболел и потерял здоровье 😷")

    elif event == "find_money":
        print("💰 Событие: Находка денег")
        money += 30
        print("Ты нашёл деньги на улице 🤑")

    elif event == "rest":
        print("😌 Событие: Отдых")
        mood += 20
        health += 10
        print("Ты отдохнул и восстановился 💆")

    # =========================
    # PLAYER CHOICE
    # =========================
    print("\nЧто ты хочешь сделать?")
    print("1 - Работать (+деньги, -настроение)")
    print("2 - Отдыхать (+здоровье, +настроение)")
    print("3 - Рискнуть (рандом событие)")

    choice = input("Выбор (1/2/3): ")

    if choice == "1":
        money += 15
        mood -= 5
        print("Ты поработал 💼")

    elif choice == "2":
        health += 10
        mood += 10
        print("Ты отдохнул 😌")

    elif choice == "3":
        surprise = random.randint(-20, 30)
        money += surprise
        print(f"Риск дал результат: {surprise} 💥")

    else:
        print("Пропуск хода 😐")

    # =========================
    # LIMITS
    # =========================
    if health > 100:
        health = 100
    if mood > 100:
        mood = 100

    if health <= 0:
        print("\n💀 Ты умер от плохого здоровья...")
        break

# =========================
# RESULT
# =========================
print("\n🏁 ИГРА ЗАКОНЧЕНА!")
print(f"💰 Деньги: {money}")
print(f"❤️ Здоровье: {health}")
print(f"😊 Настроение: {mood}")

if money > 150:
    print("🏆 Ты богатый!")
elif health <= 0:
    print("☠️ Ты проиграл")
else:
    print("🙂 Ты просто выжил")