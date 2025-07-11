from panquetes.Menuss.Menu_Base import MenuItem

class Order:
    def __init__(self, menu: list, tip: float = 0):
        self.menu = menu
        self.tip = tip
        self.order = []
        self.limit = 0
    
    def see_menu(self):
        n = len(self.menu)
        for i in range(n):
            print(str(i + 1) + ".", self.menu[i])
        return f"{n}. {self.menu[n - 1]}"

    def see_order(self):
        print("")
        n = len(self.order)
        print("lo que has pedido:")
        print("")
        for i in range(n):
            print(f"[{self.order[i].get_name()} - con un descuento de {self.order[i].get_discount()}%]")
        return ""
    
    def add_item(self, food :"MenuItem")-> list:
        self.limit = 0
        for i in self.order:
            i.new_discount(0)
        self.order.append(food)
        return f"se añidio {food.get_name()} (se reiniciaron todos los descuentos)"

    def calculate_bill_amount(self):
        print("")
        amount = 0
        for i in self.order:
            amount += i.calculate_total_price()
        return amount

