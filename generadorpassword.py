import random
import string
import argparse


class GeneradorPassword:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-c", type=int, help="Cantidad de caracteres ")
        args = parser.parse_args()
        if args.c:
            self.generar_pass(args.c, True, True, True)
        else:
            self.prompt()

    def prompt(self):
        cant_caracteres = int(input("Ingrese candidad de caracteres: "))
        incluyemayus = input("Incluir mayusculas? (s/n) ")
        if incluyemayus.lower() == 's':
            caps = True
        elif incluyemayus.lower() == 'n':
            caps = False
        incluyecharesp = input("Incluir caracteres especiales? (s/n) ")
        if incluyecharesp.lower() == 's':
            char_esp = True
        elif incluyecharesp.lower() == 'n':
            char_esp = False
        incluyenum = input("Incluir numeros? (s/n) ")
        if incluyenum.lower() == 's':
            nums = True
        elif incluyenum.lower() == 'n':
            nums = False
        self.generar_pass(cant_caracteres, caps, char_esp, nums)

    def generar_pass(self, nro_char, caps, char_esp, nums):
        listachar = []
        for i in string.ascii_lowercase:
            listachar.append(i)
        if caps == True:
            for i in string.ascii_uppercase:
                listachar.append(i)
        if char_esp == True:
            listespchar = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*',
                           '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '/', ':', ';', ',', '<', '>', '.', '?']
            listachar = listachar+listespchar
        if nums == True:
            numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
            for i in numeros:
                listachar.append(str(i))
        contrasena = []
        i = 0
        while i < nro_char:
            contrasena.append(random.choice(listachar))
            i += 1
        # szcontrasena=""
        szcontrasena = ''.join(contrasena)
        print(szcontrasena)


a = GeneradorPassword()
