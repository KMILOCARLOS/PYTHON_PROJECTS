from Nodo import node

class lista:
    def __init__(self):
        self.cabeza = None

    def menu_busqueda(self, pos):
        print("="*30)
        print("1. Eliminar nodo")
        print("2. Cambiar valor")
        print("3. Ninguna acción")
        print("="*30)

    def añadir_nodo(self, num):
        nodo_nuevo = node(num)
        if not self.cabeza:
            self.cabeza = nodo_nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodo_nuevo

    def mostrar_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.num)
            actual = actual.siguiente

    def mostrar_lista_inversa(self, nodo):
        if nodo is None:
            return
        self.mostrar_lista_inversa(nodo.siguiente)
        print(nodo.num)

    def eliminar_nodo(self, previo, actual):
        if previo is None:
            self.cabeza = actual.siguiente
        else:
            previo.siguiente = actual.siguiente
        print(f"El nodo con numero {actual.num} ha sido eliminado.\n\n")

    def editar_nodo(self, nuevo_num, actual):
        tem = actual.num
        actual.num = nuevo_num
        print(f"El nodo con numero {tem} ha sido modificado a {actual.num}.\n\n")

    #aqui



    def eliminar_lista_mismos_valores(self, valor):
        actual = self.cabeza
        previo = None
        while actual:
            if actual.num == valor:
                self.eliminar_nodo(previo, actual)
            previo = actual
            actual = actual.siguiente #correr

    def buscar_nodo(self, num):
        actual = self.cabeza
        previo = None
        cont = 1
        while actual:
            if cont == num:
                print(f"El número encontrado en la posición {num} es {actual.num}")
                
                while True:
                    self.menu_busqueda(num)

                    des = int(input("-> "))

                    if des == 1:
                        self.eliminar_nodo(previo, actual)
                    elif des == 2:
                        nuevo_num = int(input("Ingrese el nuevo numero para el nodo -> "))
                        self.editar_nodo(nuevo_num, actual)
                    elif des == 3:
                        break
                    else:
                        print("\nDato no valido\n")
                
                return
            previo = actual  
            actual = actual.siguiente
            cont += 1
        print(f"No se encontró ningún nodo en la posición {num}")
