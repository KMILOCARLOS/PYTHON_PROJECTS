from Funciones import lista


numeros = lista()
for i in range(1, 11):
    numeros.añadir_nodo(i)


def menu():
    print("\n" + "="*30)
    print("         MENU PRINCIPAL          ")
    print("="*30)
    print("1. Mostrar lista")
    print("2. Buscar casilla")
    print("3. Mostrar lista inversa")
    print("4  Eliminar nodos con un mismo valor")
    print("5  Mostrar el numero mayor de la lista")
    print("6  Funciones especiales")
    print("0. Salir")
    print("="*30)

def menuFuncEsp():
    print("\n" + "="*30)                     
    print("      FUNCIONES ESPECIALES       ")
    print("="*30)
    print("1. Hacer push")
    print("2. Hacer pop")
    print("3. Hacer enqueue")
    print("4  Hacer dequeue")
    print("0. Salir")
    print("="*30)

def ejecutar():
    while True:
        menu()

        des = int(input("-> "))

        if des == 1:
            print()
            numeros.mostrar_lista()
            print("\n")
        elif des == 2:
            print()
            bus = int(input("\nInserte la posición a buscar -> "))
            numeros.buscar_nodo(bus)
            print("\n")
        elif des == 3:
            print()
            numeros.mostrar_lista_inversa(numeros.cabeza)
            print("\n")
        elif des == 4:
            print()
            valor = int(input("\nIngrese el numero para eliminar los nodos con este -> "))
            numeros.eliminar_lista_mismos_valores(valor)
            print("\n")
        elif des == 5:
            print()
            numeros.encontrar_valor_mayor()
            print("\n")
        elif des == 6:
            print()

            while True:
                menuFuncEsp()
                des = int(input("-> "))

                if des == 1:
                    num = int(input("Ingrese un numero para agregar en la lista -> "))
                    numeros.push_nodo(num)
                    print("\n")
                elif des == 2:
                    numeros.pop_nodo()
                    print("\n")
                elif des == 3:
                    print("\n")
                elif des == 4:
                    print("\n")
                elif des == 0:
                    break
                else:
                    print("\nDato no valido\n")

            print("\n")
        elif des == 0:
            break
        else:
            print("\nDato no valido\n")


if __name__ == "__main__":
    ejecutar()
