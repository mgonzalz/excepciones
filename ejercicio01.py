'''
Enunciado: escriba un programa que simule la conexión de un usuario a un sitio web para el que ya se ha registrado, solo con su dirección de correo electrónico (la gestión de una contraseña está fuera del alcance de esta sección). Este programa debe ofrecer la posibilidad al usuario de introducir una dirección de correo electrónico, y mostrará diferentes mensajes de error en función de la cadena introducida. El programa debe continuar si el correo electrónico indicado tiene un formato incorrecto y finalizar si no se reconoce el correo electrónico, ya que se podría tratar de un ciberataque. Importante: el método que analiza la cadena de caracteres no debe devolver ningún valor.

'''

import re # El método re permite trabajar con expresiones regulares
import csv

#CÓDIGO
class Correo_Electronico:
    def __init__(self, correo, name):
        self.correo = correo
        self.name = name
    def get_correo(self):
        return self.correo
    def get_name(self):
        return self.name
    def __str__(self):
        return self.name + " " + self.correo

def get_from_csv(filename):
    lista = []
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        for row in reader: # CONVERTIR EN CLASES
            correos = Correo_Electronico(row[0], row[1])
            lista.append(correos)
    return lista

def main():
    lista = get_from_csv("data/correos_disponibles.csv")
    print("Bienvenido al sitio web")
    try:
        correo = input("--> ")
    except re.search(". * @. * \ .. *", correo):
        print("Una dirección de correo electrónico debe tener el formato xxx@xxx.xx")
    else:
        for i in lista:
            if correo == i.get_correo():
                print(f"Bienvenido {i.get_name()}")
                break
        else:
            print("Cuenta bloqueada a causa de un ataque")


if __name__ == '__main__':
    main()
