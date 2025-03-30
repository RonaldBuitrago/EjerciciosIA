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
