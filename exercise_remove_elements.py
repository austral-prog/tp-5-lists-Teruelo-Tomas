# Ejercicio 4: Remover elementos en posiciones específicas

def remove_elements(lista):
    """
    Remueve el primer, quinto y sexto elemento de la lista.
    La función debe funcionar con listas de cualquier tamaño.

    Args:
        lista: Una lista de elementos

    Returns:
        La lista después de remover los elementos indicados
    """
    indice = len(lista)
    if indice >= 6:
        del lista[5]
        del lista[4]
        del lista[0]
        return lista
    elif indice >= 5:
        del lista[4]
        del lista[0]
        return lista
    elif indice >= 1:
        del lista[0]
        return lista
    elif indice == 0:
        return lista


