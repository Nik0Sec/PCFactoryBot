# Script para comprar tarjetas gráficas via Pcfactory.cl
# Creado por Nik0
import colorama as colorama
from bs4 import BeautifulSoup
import requests
from time import sleep
import os
from progress.bar import Bar
from colorama import init, Fore, Back
import sys

init(autoreset=True)


# identificar SO corriendo para asi aplicar permisos correspondientes y que no hayan errores
def sistema():
    cool = os.uname()
    print(colorama.Fore.YELLOW + "Ejecutando este programa en un sistema operativo {} ".format(cool.sysname))
    sleep(0.07)


# Verificar si el usuario es root
def root():
    if os.getuid() != 0:
        print(colorama.Fore.RED + "No eres root, ejecuta sudo python3 PCFactoryBot.py")
        sys.exit(1)


# Se crea una variable con el link de la web y en conjunto se llama a request y soup para parsear el contenido
url = 'https://www.pcfactory.cl/tarjetas-graficas?categoria=334'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')


def banner():
    print("+" + "-" * 71 + "+")
    for map in range(20):
        print("|", end="")
        for map1 in range(20):
            if map1 == map:
                print("こごさざしじす", end="")
            else:
                print("   ", end="")
        print("|")

    print("+" + "-" * 71 + "+")
    print(colorama.Fore.BLUE + "Creado por: https://nik0sec.github.io")
    bar = Bar('Cargando', max=100)
    for i in range(100):
        sleep(0.03)
        bar.next(1)
    bar.finish()
    sleep(1)
    os.system("clear")


# Se llama a la clase del elemento (div), creando una variable "tarjetas" y se itera con un for para listar las tarjetas
def main():
    pregunta = input(colorama.Fore.BLUE + "¿Quieres saber que tarjetas graficas están en stock? SI/NO \n")
    if pregunta == "SI":
        os.system("clear")
        print("Estas tarjetas están disponibles actualmente en PCFactory")
        print(colorama.Fore.GREEN + "---------------------------------------------------------")
        tarjetas = soup.find_all('span', class_='nombre')
        for x in tarjetas:
            tarjetas = x.text
            print(tarjetas)
        print(colorama.Fore.GREEN + "---------------------------------------------------------")
    pregunta2 = input(colorama.Fore.BLUE + "¿Quieres que te avise si se agrega otro más? SI/NO \n")
    if pregunta2 == "SI":
        for y in tarjetas:
            while y in tarjetas:
                sleep(1)
                print(
                    colorama.Fore.RED + "Esperando a que agreguen otra tarjeta a la categoría... (No salir del programa!)")
            else:
                print(colorama.Fore.GREEN + "Se a añadido otra tarjeta!")
    else:
        print(colorama.Fore.RED + "Adiós")


if __name__ == "__main__":
    root()
    banner()
    sistema()
    main()
