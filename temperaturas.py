# Registro de temperaturas diarias en ciudades de Los Ríos

# Lista de ciudades de Los Ríos
ciudades = ["Babahoyo", "Quevedo", "Ventanas"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 2  # Número de semanas a registrar

# Matriz 3D (ciudades x días x semanas) con temperaturas de ejemplo
temperaturas = [
    [   # Ciudad 0: Babahoyo
        [27, 29], [28, 30], [27, 31], [26, 29],
        [28, 30], [27, 28], [29, 31]
    ],
    [   # Ciudad 1: Quevedo
        [28, 30], [29, 31], [30, 32], [28, 29],
        [27, 30], [26, 28], [29, 32]
    ],
    [   # Ciudad 2: Ventanas
        [26, 28], [27, 29], [26, 30], [25, 28],
        [26, 29], [25, 27], [27, 29]
    ]
]

# Función para calcular el promedio de una ciudad
# -------------------------
def promedio_ciudad(ciudad_index, temperaturas):
    """
    Calcula el promedio de temperatura de una ciudad en todas sus semanas.
    ciudad_index: índice de la ciudad en la lista 'ciudades'
    temperaturas: lista 3D con temperaturas [ciudad][semana][día]
    """
    total = 0
    contador = 0
    for semana in temperaturas[ciudad_index]:
        total += sum(semana)
        contador += len(semana)
    return total / contador

# -------------------------
# Uso de la función
# -------------------------
for i, ciudad in enumerate(ciudades):
    promedio = promedio_ciudad(i, temperaturas)
    print(f"Promedio general en {ciudad}: {promedio:.2f}°C")