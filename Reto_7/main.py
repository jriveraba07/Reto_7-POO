from panquetes.Menuss.Order import Order
from panquetes.recipes.MainCourse import MainCourse
from panquetes.recipes.Beverage import Beverage 
from panquetes.recipes.Dessert import Dessert
from panquetes.recipes.Appetizer import Appetizer 
from panquetes.Payments.Paymentss import CardPayment, CashPayment


if __name__ == '__main__':

    milhoja = Dessert("milhoja", 7500, True, "Postre con mil hojas")
    pollo_asado = MainCourse("pollito asado", 40000, "pollo","Un pollo asado de dudosa procedencia")
    bistec = MainCourse("bistec", 25000, "carne", "Hecho de las vacas de genetica en la nacional")
    natilla = Dessert("natilla", 5000, True, "Delicioso postre colombiano con leche de bufalo")
    changua = Appetizer("changua", 9500, 500,"leche con huevo (¿Quien creyo que era buena idea esto?)")
    cerveza_1 = Beverage("cerveza", 3500, "poker", "Cerveza que toma el rolo promedio")
    aguardiente = Beverage("aguardiente 1/2", 16000, "nectar", "Agua que pica pero rico")
    chunchullo = Appetizer("chunchullo", 12000, 200, "No preguntes de donde viene, solo disfrutalo")
    mojarra = MainCourse("mojarra", 40000, "pescado","OJO CON LAS ESPINAS")
    limonada = Beverage("limonada de coco", 3500, "frutiño", "Limonada hecha con agua de la llave")

    menu = [milhoja, pollo_asado, bistec, natilla, changua, cerveza_1, aguardiente, chunchullo, mojarra, limonada]
    cliente = Order(menu, tip = 0)

    card = CardPayment("15478935456215789", 666)
    cash = CashPayment(130000)

    cliente.see_menu()
    cliente.add_item(pollo_asado)
    cliente.add_item(chunchullo)
    cliente.add_item(bistec)
    print(cliente.see_order())
    print(cliente.calculate_bill_amount())

    print(cliente.calculate_bill_amount())
    cliente.see_order()
    print("")
    print(cliente.add_item(mojarra))
    print(cliente.add_item(milhoja))
    print(cliente.add_item(changua))

    cliente.see_order()
    cliente.calculate_bill_amount()
    cliente.see_order()

    print("                                  |CUENTA|")
    a = float(input(f"cuanto porcentaje de la cuenta quieres agregar: "))
    total = cliente.calculate_bill_amount() 
    cliente.tip = a
    if a == 0:
        print("tacaño resulto el señor!")

    total_plustip = total * (a / 100 + 1)
    print(f"Total a pagar: {total_plustip}, cuenta de {total} con propina de: {cliente.tip}%" )
    print("")
    print("$Pay the bill with cash$")
    print("")
    cash.pay(total_plustip)
    print("")
    print("$Pay the bill with card$")
    print("")
    card.pay(total_plustip)