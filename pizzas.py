import ingredientes as ing

class Pizza:

    #Atributos de clase
    precio = '$10.000'
    tamano = 'familiar'

    #Definicion de metodos
    @staticmethod
    def validar (texto, casos_posibles):
        if texto in casos_posibles:
            return True
        else:
            return False

    def pedido(self):
        self.proteico = input('ingrese el ingrediente proteico: ')
        self.vegetal_uno = input('ingrese el primer vegetal: ')
        self.vegetal_dos = input('ingrese el segundo vegetal: ')
        self.masa = input('ingrese el tipo de masa: ')
        self.valido = Pizza.validar(self.proteico,ing.proteicos) and Pizza.validar(self.vegetal_uno,ing.vegetales) and Pizza.validar(self.vegetal_dos,ing.vegetales) and Pizza.validar(self.masa,ing.tipo_masa)
