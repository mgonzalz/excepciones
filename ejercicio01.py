'''
Enunciado: escriba un programa que simule la conexión de un usuario a un sitio web para el que ya se ha
registrado, solo con su dirección de correo electrónico (la gestión de una contraseña está fuera del
alcance de esta sección). Este programa debe ofrecer la posibilidad al usuario de introducir una dirección
de correo electrónico, y mostrará diferentes mensajes de error en función de la cadena introducida. El
programa debe continuar si el correo electrónico indicado tiene un formato incorrecto y finalizar si no se
reconoce el correo electrónico, ya que se podría tratar de un ciberataque. Importante: el método que
analiza la cadena de caracteres no debe devolver ningún valor.
'''

import re # El método re permite trabajar con expresiones regulares
import csv

#CÓDIGO
class Correo_Electronico:
    def __init__(self, correo, name):
        self.correo = str(correo)
        self.name = str(name)
    def get_correo(self):
        return self.correo
    def get_name(self):
        return self.name
    def __str__(self):
        return self.name + " " + self.correo

#EXCEPCIONES
class FormatoMalo(Exception): pass
class CiberAtaque(Exception): pass
class Clear(Exception):
    def __init__(self, message):
        self.message = message
    def get_error(self):
        return "'{}' es una entrada incorrecta. Introduzca una dirección de correo".format(self.message)


#CSV
def get_from_csv(filename):
    if not isinstance(filename, str):
        raise TypeError("El archivo debe ser una cadena de caracteres")
    lista = []
    try:
        with open(filename, newline='') as file:
            reader = csv.reader(file)
            for row in reader: # CONVERTIR EN CLASES
                correos = Correo_Electronico(str(row[0]), str(row[1]))
                lista.append(correos)
    except SyntaxError:
        print("Error de sintaxis")
    return lista


#FUNCIONES

def check_correo(correo, lista):
    if correo is None or len(correo) == 0: #CORREO VACIO
        raise Clear(correo)
    if re.search(".*@.*\..*", correo) is None: #CORREO MALO
        raise FormatoMalo
    if not correo in [i.get_correo() for i in lista]: #CORREO NO ENCONTRADO EN LA LISTA
        raise CiberAtaque

if __name__ == "__main__":
    lista = get_from_csv("data/correos_disponibles.csv")
    print("Bienvenido al sitio web" + "\n" + "Introduzca su dirección de correo electrónico")
    correo =input("->")
    if not isinstance(correo, str):
        raise TypeError("El correo debe ser una cadena de caracteres")
    else:
        try:
            check_correo(correo, lista)
        except Clear as c:
            c.get_error()
        except FormatoMalo:
            print("Una dirección de correo electrónico debe tener el formato xxx@xxx.xx")
        except CiberAtaque:
            print("Cuenta bloqueada a causa de un ataque")
            exit()
    for i in lista:
        if correo == i.get_correo():
            print("Bienvenido " + i.get_name())
            break
