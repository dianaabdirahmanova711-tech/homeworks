#1
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4

app = FastAPI(title="Game API", description="Тапсырма 1, 2, 3", version="1.0")


# Тапсырма 1 және 2:
class Player:
    def __init__(self, player_id: int, name: str, hp: int):
        self._id = player_id
        self._name = name.strip().title()
        self._hp = max(0, hp)

    @classmethod
    def from_string(cls, data: str):
        parts = [part.strip() for part in data.split(',')]
        if len(parts) != 3:
            raise ValueError("Неверный формат. Ожидается: id,name,hp")
        try:
            player_id = int(parts[0])
            name = parts[1]
            hp = int(parts[2])
            return cls(player_id, name, hp)
        except ValueError:
            raise ValueError("id и hp должны быть числами")

    def __str__(self):
        return f"Player(id={self._id}, name='{self._name}', hp={self._hp})"

    def __del__(self):
        print(f"Player {self._name} удалён")


# Тапсырма 3:
class Item:
    def __init__(self, item_id: int, name: str, power: int):
        self.id = item_id
        self.name = name.strip().title()
        self.power = power

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        if not isinstance(other, Item):
            return False
        return self.id == other.id

    def __str__(self):
        return f"Item(id={self.id}, name='{self.name}', power={self.power})"



class PlayerResponse(BaseModel):
    id: int
    name: str
    hp: int


class ItemResponse(BaseModel):
    id: int
    name: str
    power: int


players_db = []
items_db = []




# Тапсырма 1: Жаңа ойыншы қосу
@app.post("/players", response_model=PlayerResponse, status_code=201)
def create_player(player_id: int, name: str, hp: int):
    new_player = Player(player_id, name, hp)
    players_db.append(new_player)
    return {"id": new_player._id, "name": new_player._name, "hp": new_player._hp}


# 2
@app.post("/players/from_string")
def create_player_from_string(data: str):
    try:
        player = Player.from_string(data)
        players_db.append(player)
        return {"message": "Player created", "player": str(player)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


#3
@app.get("/players", response_model=List[PlayerResponse])
def get_players():
    return [{"id": p._id, "name": p._name, "hp": p._hp} for p in players_db]



@app.post("/items", response_model=ItemResponse, status_code=201)
def create_item(item_id: int, name: str, power: int):
    new_item = Item(item_id, name, power)
    items_db.append(new_item)
    return {"id": new_item.id, "name": new_item.name, "power": new_item.power}



@app.get("/items", response_model=List[ItemResponse])
def get_items():
    return [{"id": i.id, "name": i.name, "power": i.power} for i in items_db]



@app.get("/")
def root():
    return {
        "message": "Тапсырма 1, 2, 3 орындалды",
        "endpoints": {
            "POST /players": "Жаңа ойыншы қосу (id, name, hp)",
            "POST /players/from_string": "Жолдан ойыншы қосу (мысалы: '1,John,100')",
            "GET /players": "Барлық ойыншыларды көру",
            "POST /items": "Жаңа предмет қосу (id, name, power)",
            "GET /items": "Барлық предметтерді көру"
        }
    }


#4


class Inventory:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        if not any(i.id == item.id for i in self._items):
            self._items.append(item)

    def remove_item(self, item_id):
        self._items = [i for i in self._items if i.id != item_id]

    def get_items(self):
        return self._items.copy()

    def unique_items(self):
        return set(self._items)

    def to_dict(self):
        return {item.id: item for item in self._items}


# Тест
inv = Inventory()
inv.add_item(Item(1, "Sword", 50))
inv.add_item(Item(2, "Shield", 30))
print([str(i) for i in inv.get_items()])
print(inv.to_dict())


#5
class Inventory:


    def get_strong_items(self, min_power: int):
        return [item for item in self._items if item.power >= min_power]


# Тест
inv = Inventory()
inv.add_item(Item(1, "Sword", 50))
inv.add_item(Item(2, "Dagger", 20))
inv.add_item(Item(3, "Axe", 40))

strong = inv.get_strong_items(30)
for item in strong:
    print(item)


#6
from datetime import datetime


class Event:
    def __init__(self, event_type: str, data: dict):
        self.type = event_type
        self.data = data
        self.timestamp = datetime.now()

    def __str__(self):
        return f"Event(type='{self.type}', data={self.data}, timestamp='{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}')"


# Тест
e = Event("ATTACK", {"damage": 20})
print(e)

#7
class Player:
    def __init__(self, player_id: int, name: str, hp: int):
        self._id = player_id
        self._name = name.strip().title()
        self._hp = max(0, hp)
        self._inventory = None

    def set_inventory(self, inventory):
        self._inventory = inventory

    def handle_event(self, event):
        if event.type == "ATTACK":
            self._hp -= event.data.get("damage", 0)
            if self._hp < 0:
                self._hp = 0
        elif event.type == "HEAL":
            self._hp += event.data.get("heal", 0)
        elif event.type == "LOOT":
            item = event.data.get("item")
            if item and self._inventory:
                self._inventory.add_item(item)

    def __str__(self):
        return f"Player(id={self._id}, name='{self._name}', hp={self._hp})"


class Warrior(Player):
    def handle_event(self, event):
        if event.type == "ATTACK":
            damage = event.data.get("damage", 0)
            event.data["damage"] = int(damage * 0.9)
        super().handle_event(event)


class Mage(Player):
    def handle_event(self, event):
        if event.type == "LOOT":
            item = event.data.get("item")
            if item:
                item.power = int(item.power * 1.1)
        super().handle_event(event)


# Тест
inv = Inventory()
inv.add_item(Item(1, "Sword", 50))

w = Warrior(1, "Aragorn", 100)
w.set_inventory(inv)

e = Event("ATTACK", {"damage": 50})
w.handle_event(e)
print(w)

#8
import json

class Logger:
    @staticmethod
    def log(event: Event, player: Player, filename: str):
        with open(filename, 'a', encoding='utf-8') as f:
            line = f"{event.timestamp};{player._id};{event.type};{json.dumps(event.data)}\n"
            f.write(line)


# Тест
logger = Logger()
logger.log(e, w, "test_log.txt")
print("Лог записан")


#9
class Logger:
    @staticmethod
    def read_logs(filename: str):
        events = []
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                for line in f:
                    parts = line.strip().split(';')
                    if len(parts) == 4:
                        ts, pid, etype, data_str = parts
                        data = json.loads(data_str)
                        ev = Event(etype, data)
                        ev.timestamp = datetime.strptime(ts, '%Y-%m-%d %H:%M:%S.%f')
                        events.append(ev)
        except FileNotFoundError:
            pass
        return events


# Тест
events = Logger.read_logs("test_log.txt")
for ev in events:
    print(ev)


#10
class EventIterator:
    def __init__(self, events):
        self._events = events
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._events):
            raise StopIteration
        event = self._events[self._index]
        self._index += 1
        return event


# Тест
events = [Event("ATTACK", {"damage": 10}), Event("HEAL", {"heal": 20})]
for ev in EventIterator(events):
    print(ev)

#11
def damage_stream(events):
    for event in events:
        if event.type == "ATTACK":
            yield event.data.get("damage", 0)


# Тест
events = [Event("ATTACK", {"damage": 15}), Event("HEAL", {"heal": 10})]
for dmg in damage_stream(events):
    print(dmg)


#12
import random

def generate_events(players, items, n):
    event_types = ["ATTACK", "HEAL", "LOOT"]
    events = []
    for _ in range(n):
        player = random.choice(players)
        etype = random.choice(event_types)
        if etype == "ATTACK":
            data = {"damage": random.randint(10, 50)}
        elif etype == "HEAL":
            data = {"heal": random.randint(10, 30)}
        else:
            data = {"item": random.choice(items) if items else None}
        events.append(Event(etype, data))
    return events


# Тест
p1 = Player(1, "Hero", 100)
itm = [Item(1, "Sword", 50)]
evs = generate_events([p1], itm, 5)
for ev in evs:
    print(ev)


#13
def analyze_logs(events):
    total_damage = 0
    event_counts = {}

    for ev in events:
        if ev.type == "ATTACK":
            total_damage += ev.data.get("damage", 0)
        event_counts[ev.type] = event_counts.get(ev.type, 0) + 1

    most_common = max(event_counts.items(), key=lambda x: x[1])[0] if event_counts else None

    return {
        "total_damage": total_damage,
        "most_common_event": most_common
    }


# Тест
events = [Event("ATTACK", {"damage": 20}), Event("ATTACK", {"damage": 30}), Event("HEAL", {"heal": 10})]
stats = analyze_logs(events)
print(stats)



#14
decide_action = lambda player, inventory: (
    "HEAL" if player._hp < 30 else
    "LOOT" if inventory and len(inventory.get_items()) < 3 else
    "ATTACK"
)


# Тест
p = Player(1, "Hero", 25)
inv = Inventory()
print(decide_action(p, inv))


#18
class Inventory:
    # ... предыдущий код ...

    def __iter__(self):
        return iter(self._items)


# Тест
inv = Inventory()
inv.add_item(Item(1, "Sword", 50))
inv.add_item(Item(2, "Shield", 30))

for item in inv:
    print(item)

# Comprehension
strong = [item for item in inv if item.power >= 40]
print([str(i) for i in strong])

#19
def analyze_inventory(inventories):
    all_items = []
    for inv in inventories:
        all_items.extend(inv.get_items())

    unique_items = set(all_items)

    if all_items:
        top_power = max(all_items, key=lambda x: x.power)
    else:
        top_power = None

    return {
        "unique_items": unique_items,
        "top_power": top_power
    }


# Тест
inv1 = Inventory()
inv1.add_item(Item(1, "Sword", 50))
inv1.add_item(Item(2, "Dagger", 20))

inv2 = Inventory()
inv2.add_item(Item(1, "Sword", 50))
inv2.add_item(Item(3, "Axe", 40))

result = analyze_inventory([inv1, inv2])
print("Unique:", [str(i) for i in result["unique_items"]])
print("Top:", result["top_power"])


#20
def main():
    # Создание игроков
    p1 = Warrior(1, "Aragorn", 120)
    p2 = Mage(2, "Gandalf", 90)
    p3 = Player(3, "Legolas", 100)

    # Создание инвентарей
    inv1, inv2, inv3 = Inventory(), Inventory(), Inventory()
    p1.set_inventory(inv1)
    p2.set_inventory(inv2)
    p3.set_inventory(inv3)

    # Создание предметов
    items = [
        Item(1, "Sword", 50),
        Item(2, "Staff", 40),
        Item(3, "Bow", 30),
        Item(4, "Potion", 10)
    ]

    for item in items[:2]:
        inv1.add_item(item)
    inv2.add_item(items[2])
    inv3.add_item(items[3])

    # Генерация событий
    players = [p1, p2, p3]
    events = generate_events(players, items, 20)

    # Обработка событий и логирование
    logger = Logger()
    for event in events:
        for player in players:
            player.handle_event(event)
            logger.log(event, player, "game_log.txt")

    # Аналитика
    logs = Logger.read_logs("game_log.txt")
    stats = analyze_logs(logs)

    print("=== ФИНАЛЬНЫЕ РЕЗУЛЬТАТЫ ===")
    for p in players:
        print(f"{p._name}: HP={p._hp}, предметов={len(p._inventory.get_items())}")

    print(f"\nСтатистика: {stats}")
    print("✅ Симуляция завершена!")


if __name__ == "__main__":
    main()
