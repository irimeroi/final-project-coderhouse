# Crear un programa que permita el modelamiento de Clientes en una página de compras. Se debe utilizar el concepto de Programación Orientada a Objetos y lo aprendido en clase.
# Se evaluará el uso correcto de atributos y métodos.
# Utilizar los conceptos aprendidos en la clase 15 y crear un paquete redistribuible con el programa creado."

from paquete.cliente import Cliente, Mates

cliente1 = Cliente("Irina", "Meroi", 38123, "Lavalle 123", 1234567890)
mate1 = Mates("mate", 100, 15)
yerba1 = Mates("bombilla", 20, 50)

print(cliente1.pagar("credito"))
print(cliente1.comprar(True, mate1, 1))
print(cliente1.comprar(True, yerba1, 2))
print(yerba1.compra_realizada(0))