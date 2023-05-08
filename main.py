
lista = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

def hacer_grandioso(*miLista):
    nuevaLista = []
    for i in miLista[0]:
        nombre = "El gran " + i
        nuevaLista.append(nombre)
    return nuevaLista

def filtro_nombres(*miLista):
    listaMagos, listaCientif, listaOtros = [], [], []
    for i in miLista[0]:
        if i in ("Harry Houdini", "David Blaine", "Teller"):
            listaMagos.append(i)
        elif i in ("Newton", "Hawking", "Einstein"):
            listaCientif.append(i)
        else:
            listaOtros.append(i)
    print("Lista magos: ", listaMagos, "\nLista científicos: ", listaCientif, "\nLista otros: ", listaOtros)
    listaMagos = hacer_grandioso(listaMagos)
    return (listaMagos, listaCientif, listaOtros)

def imprimir_lista(*miLista):
    print("Lista original: ", miLista[0]) 

def imprimir_nombres(*miLista):
    for i in miLista[0]:
        print(i)

imprimir_lista(lista)
nuevaLista = filtro_nombres(lista)
print("Magos modificados: ", nuevaLista[0])