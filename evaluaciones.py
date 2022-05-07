from pizzas import Pizza

#Evaluaciones

#a
print(Pizza.precio, Pizza.tamano)

#b
salsas = ['salsa de tomate', 'salsa bbq']

print(Pizza.validar('salsa de tomate', salsas))

#c
pedido_uno = Pizza()

pedido_uno.pedido()

#d
print(f'''los ingredientes seleccionados son:

{pedido_uno.proteico}
{pedido_uno.vegetal_uno}
{pedido_uno.vegetal_dos}
{pedido_uno.masa}

El pedido es {pedido_uno.valido}''')

#e
print(Pizza.pedido())