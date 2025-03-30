# Representación del sistema de transporte como un grafo
grafo_transporte = {
    'Terminal paso del comercio': [('los Alcázares', 5), ('Salomia', 10)],
    'los Alcázares': [('Calima', 5), ('Chiminangos', 6)],
    'Calima': [('Flora Industrial', 8)],
    'Chiminangos': [('Popular', 5)],
    'Flora Industrial': [('Rio Cali', 10)],
    'Salomia': [('Manzanares', 8), ('Piloto', 5)],
    'Popular': [('Fátima', 12)],
    'Manzanares': [('Piloto', 8)],
    'Fátima': [('Rio Cali', 9)],
    'Rio Cali': [('San Nicolás', 7)],
    'Piloto': [('San Nicolás', 10)],
    'San Nicolás': []
}
def buscar_ruta(grafo, inicio, fin, ruta_actual=[], tiempo_actual=0):
    """
    Busca todas las rutas posibles usando DFS, considerando solo el tiempo.
    Devuelve una lista de rutas con sus tiempos.
    """
    ruta_actual = ruta_actual + [inicio]
    if inicio == fin:
        return [(ruta_actual, tiempo_actual)]
    if inicio not in grafo:
        return []
    rutas = []
    for vecino, tiempo in grafo[inicio]:
        if vecino not in ruta_actual:
            nuevas_rutas = buscar_ruta(
                grafo, vecino, fin, ruta_actual, tiempo_actual + tiempo
            )
            rutas.extend(nuevas_rutas)
    return rutas
