class ColaFIFO:
    def __init__(self, datos: list):
        self.datos = datos

    def encolar(self, dato):
            self.datos.append(dato)
        
    
    def desencolar(self, actual_order):
        if len(self.datos) != 0:
            actual_order.append(self.datos[0])
            return self.datos.pop(0)
        else:
            return "lista vacia!!!"
        
    def __len__(self):
         return len(self.datos)