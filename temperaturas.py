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

# Calcular y mostrar promedios de temperatura
for c, ciudad in enumerate(ciudades):
    for s in range(semanas):
        suma = 0
        for d in range(len(dias)):
            suma += temperaturas[c][d][s]
        promedio = suma / len(dias)
        print(f"Promedio semana {s+1} en {ciudad}: {promedio:.2f}°C")