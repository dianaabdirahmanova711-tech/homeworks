#1
class User:
    def __init__(self,_id:int,_name:str,_email:str):
        self._id=_id
        self._name=_name.strip().title()
        _email=_email.lower()
        self._email = _email
        if "@" not in _email:
            raise ValueError(f"Invalid email ")

    def __str__(self):
        return f"User(id={self._id},name='{self._name}',email='{self._email}')"
    def __del__(self):
        print(f"User {self._name} deleted")
U=User(1,"diana kim","diana.abd711@gmail.COM")
print(U)

#2
class User:
    def __init__(self,_id:int,_name:str,_email:str):
        self._id=_id
        self._name=_name
        self._email=_email
    def __str__(self):
        return f"User(id={self._id},name='{self._name}',email='{self._email}')"
    @classmethod
    def from_string(cls,data:str):
        parts=data.split(",")
        if len(parts) != 3:
            raise ValueError(f"Invalid Input format")
        _id=int(parts[0].strip())
        _name=parts[1].strip()
        _email=parts[2].strip()
        if "@" not in _email or "." not in _email:
            raise ValueError(f"Invalid Email")
        return cls(_id,_name,_email)
V=User.from_string("2,Dikosha Er,diana.abd711@gmail.COM")
print(V)


#3
class Product:
    def __init__(self,id:int,name:str,price:float,category:str):
        self.id=id
        self.name=name
        self.price=price
        self.category=category
    def __str__(self):
        return f"Product(id={self.id},name='{self.name}',price={self.price},category={self.category})"
    def __eq__(self,other):
        if not isinstance(other,Product):
            return False
        return self.id == other.id
    def __hash__(self):
        return hash(self.id)
    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "price":self.price,
            "category":self.category,
        }
p1 = Product(1, "Laptop", 1200.0, "Electronics")
p2 = Product(1, "Laptop Pro", 1500.0, "Electronics")

print(p1)

products = {p1, p2}
print(len(products))  # 1

print(p1.to_dict())

#4
class Inventory:
    def __init__(self):
        self._products = {}

    def add_product(self, product):
        if product.id not in self._products:
            self._products[product.id] = product
        else:
            print(f"Product with id {product.id} already exists.")

    def remove_product(self, product_id: int):
        self._products.pop(product_id, None)

    def get_product(self, product_id: int):
        return self._products.get(product_id)

    def get_all_products(self):
        return list(self._products.values())

    def unique_products(self):
        return set(self._products.values())

    def to_dict(self):
        return self._products.copy()

#5
class Product:
    def __init__(self, id: int, name: str, price: float, category: str):
        self.id = id
        self.name = name
        self.price = price
        self.category = category


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        if not any(p.id == product.id for p in self.products):
            self.products.append(product)

    def filter_by_price(self, min_price: float) -> list[Product]:
        """
        Используем lambda для условия и list comprehension для фильтрации.
        """
        is_expensive = lambda p: p.price >= min_price

        return [product for product in self.products if is_expensive(product)]


inv = Inventory()
inv.add_product(Product(1, "Laptop", 1200.0, "Electronics"))
inv.add_product(Product(2, "Mouse", 25.0, "Electronics"))

expensive = inv.filter_by_price(100.0)
print([p.name for p in expensive])


#6
import datetime

class Logger:
    @staticmethod
    def log_action(user, action: str, product, filename: str):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"{timestamp};{user._id};{action};{product.id}\n"
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(log_line)

    @staticmethod
    def read_logs(filename: str):
        logs = []
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                t, uid, act, pid = line.strip().split(';')
                logs.append({'timestamp': t, 'user_id': uid, 'action': act, 'product_id': pid})
        return logs

#7
class Order:
    def __init__(self, order_id: int, user: User, products: list = None):
        self.id = order_id
        self.user = user
        self.products = products if products else []

    def add_product(self, product: Product):
        self.products.append(product)

    def total_price(self):
        return sum(p.price for p in self.products)

    def __str__(self):
        return f"Order #{self.id} (Total: {self.total_price()})"


#8
    def most_expensive_products(self, n: int) -> list[Product]:
        return sorted(self.products, key=lambda x: x.price, reverse=True)[:n]

#9
def price_stream(products: list[Product]):
    for product in products:
        yield product.price

#10
class OrderIterator:
    def __init__(self, orders: list[Order]):
        self._orders = orders
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._orders):
            res = self._orders[self._index]
            self._index += 1
            return res
        raise StopIteration


#Block3
#21
def create_users_df(users):
    data = [{
        'id': u.id,
        'name': u.name,
        'email': u.email,
        'registration_date': getattr(u, 'registration_date', date.today())
    } for u in users]
    return pd.DataFrame(data)

#22
def create_products_df(products):
    data = [{
        'id': p.id,
        'name': p.name,
        'category': p.category,
        'price': p.price
    } for p in products]
    return pd.DataFrame(data)

#23
def merge_users_orders(users_df, orders_df):
    merged = pd.merge(users_df, orders_df, left_on='id', right_on='user_id')
    result = merged[['order_id', 'name', 'total']].rename(columns={'name': 'user_name'})
    return result

#24
def filter_high_total(df, threshold=100):
    return df[df['total'] > threshold]

#25
def get_user_total_sum(df):
    return df.groupby('user_name', as_index=False)['total'].sum().rename(columns={'total': 'total_sum'})


#26
def get_user_mean_total(df):
    return df.groupby('user_name', as_index=False)['total'].mean().rename(columns={'total': 'mean_total'})

#27
def get_user_orders_count(df):
    return df.groupby('user_name', as_index=False)['order_id'].count().rename(columns={'order_id': 'orders_count'})

#28
def get_category_mean_price(df):
    return df.groupby('category', as_index=False)['price'].mean().rename(columns={'price': 'mean_price'})

#29
def add_discount_column(df):
    df['discounted_price'] = df['price'] * 0.9
    return df

#30
def sort_products_by_price(df):
    return df.sort_values(by='price', ascending=False)



#Block4
import pandas as pd
data = {
    'user_name': ['John', 'John', 'Alice'],
    'order_id': [101, 103, 102],
    'product_name': ['Laptop', 'Shirt', 'Mouse'],
    'category': ['Electronics', 'Clothing', 'Clothing'],
    'price': [1200, 500, 25]
}

df = pd.DataFrame(data)

#  31
df['quantity'] = 1

#  32
df['total_price'] = df['price'] * df['quantity']

# 33
electronics = df[df['category'] == 'Electronics']

#  34
count_by_category = df.groupby('category').size().reset_index(name='count')

#  35
mean_price = df.groupby('category')['price'].mean().reset_index(name='mean_price')

# 36
sorted_orders = df.sort_values(by='total_price', ascending=False)

#  37
top3 = df.sort_values(by='total_price', ascending=False).head(3)

# 38
users = pd.DataFrame({
    'user_id': [1, 2],
    'user_name': ['John', 'Alice']
})

orders = pd.DataFrame({
    'order_id': [101, 102],
    'user_id': [1, 2],
    'total_price': [1200, 50]
})

merged = orders.merge(users, on='user_id')

# 39
mean_total = df.groupby('user_name')['total_price'].mean().reset_index(name='mean_total')

#  40
orders_count = df.groupby('user_name').size().reset_index(name='orders_count')

#  41
max_order = df.groupby('user_name')['total_price'].max().reset_index(name='max_order')

# 42
unique_categories = df.groupby('user_name')['category'].nunique().reset_index(name='unique_categories')

#  45
final = df.groupby('user_name').agg(
    total_orders=('order_id', 'count'),
    total_sum=('total_price', 'sum'),
    mean_total=('total_price', 'mean'),
    max_order=('total_price', 'max'),
    unique_categories=('category', 'nunique')
).reset_index()

#  43
final['VIP'] = final['total_sum'] > 1000

#  44
final_sorted = final.sort_values(by=['total_sum', 'mean_total'], ascending=[False, True])

# Вывод
print("FINAL RESULT:")
print(final_sorted)