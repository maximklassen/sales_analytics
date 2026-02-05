class Entity:
    def __init__(self, id_: str):
        if not id_ or not isinstance(id_, str):
            raise ValueError("ID kann nicht leer sein")
        self.id = id_

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id}>"


class Product(Entity):
    def __init__(self, id_: str, name: str, category: str, base_price: float):
        super().__init__(id_)

        if not name:
            raise ValueError("Der Name des Produkts kann nicht leer sein")
        if base_price < 0:
            raise ValueError("Der Preis muss größer als 0 sein.")

        self.name = name
        self.category = category
        self.base_price = float(base_price)

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.base_price:.2f}€"

class Customer(Entity):
    def __init__(self, id_: str, name: str, email: str):
        super().__init__(id_)

        if not name:
            raise ValueError("Der Kundenname kann nicht leer sein")
        if "@" not in email:
            raise ValueError("Falsche E-Mail-Address")

        self.name = name
        self.email = email
        self.lifetime_value = 0.0

    def __str__(self):
        return f"{self.name} ({self.email})"

class Order:
    def __init__(self, order_date, customer_id: str, amount: float, status: str):
        if amount < 0:
            raise ValueError("Der Bestellwert muss mindestens 0 betragen.")

        self.order_date = order_date
        self.customer_id = customer_id
        self.amount = float(amount)
        self.status = status
        
    def __str__(self):
        return f"Order from {self.customer_id}: {self.amount:.2f}€"

    def __repr__(self):
        return (
            f"<Order customer={self.customer_id} "
            f"amount={self.amount:.2f} status={self.status}>"
        )



