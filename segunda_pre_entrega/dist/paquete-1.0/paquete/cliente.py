class Cliente():
    def __init__(self, nombre, apellido, id, direccion, tarjeta):
        self.nombre = nombre
        self.apellido = apellido
        self.__id = id
        self.__direccion = direccion
        self.__tarjeta = tarjeta
        self.objeto = None

    def comprar(self, compra, mates, cantidad):
        self.objeto = mates.compra_realizada(cantidad)
        if compra == True:
            return f"El cliente {self.nombre} {self.apellido} cuyo id es {self.__id} realizó la compra de {cantidad} {mates.nombre}(s)."
        else:
            return f"El cliente {self.nombre} {self.apellido} canceló la compra."
        
    def pagar(self, metodo_de_pago):
        if metodo_de_pago == "efectivo":
            return f"El cliente {self.nombre} {self.apellido} pagó en efectivo."
        elif metodo_de_pago == "debito":
            return f"El cliente {self.nombre} {self.apellido} pagó con tarjeta de débito. El número de tarjeta es {self.__tarjeta}"
        elif metodo_de_pago == "credito":
            return f"El cliente {self.nombre} {self.apellido} pagó con tarjeta de crédito. El número de tarjeta es {self.__tarjeta}"
        elif metodo_de_pago == "MP":
            return f"El cliente {self.nombre} {self.apellido} pagó con Mercado Pago."
    
    def __str__(self):
        return f"El nombre del cliente es {self.nombre}"


class Mates():
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def compra_realizada(self, cantidad):
        self.stock -= cantidad
        return f"Hay {self.stock} {self.nombre}(s) en stock"