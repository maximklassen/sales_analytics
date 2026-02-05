class Sale:
    def __init__(self, id):
        if not id:
            raise ValueError("ID kann nicht leer sein")
        self.id = id

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id}>"

class Product(Sale):
    def __init__(self, id, name, category, base_price):
        super().__init__(id)
        if base_price < 0:
            raise ValueError("Preis muss >= 0 sein")

        self.name = name
        self.category = category
        self.base_price = float(base_price)

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.base_price:.2f}€"

class Customer(Sale):
    def __init__(self, id, name, email):
        super().__init__(id)
        self.name = name
        self.email = email
        self.lifetime_value = 0.0

class Order:
    def __init__(self, date, customer_id, amount, status):
        self.date = date
        self.customer_id = customer_id
        self.amount = float(amount)
        self.status = status


