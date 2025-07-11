
class MenuItem:
    def __init__(self,name: str, price: float, description: str = "", x: float = 0) :
        self.__name = name
        self.__price = price 
        self.__discount = x
        self.__description = description
        
    def get_name(self):
        return self.__name
        
    def get_price(self):
        return self.__price
    
    def get_discount(self):
        return self.__discount
    
    def set_discount(self, x):
        self.__discount = x
        pass
    
    def get_description(self):
        return self.__description
    

    def calculate_total_price(self)-> float:
        a = self.get_price() * (1 - self.get_discount()/100)
        self.set_discount(0) 
        return a
    
    def new_discount(self, tacaño)->float:
        if tacaño == 0:
            self.set_discount(0) 
        else:
            self.set_discount(self.get_discount() + tacaño)