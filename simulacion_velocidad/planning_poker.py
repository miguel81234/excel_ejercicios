import random
import numpy as np
import matplotlib.pyplot as plt

# Lista de valores Planning Poker (Fibonacci clásico)
planning_poker_values = [1, 2, 3, 5, 8, 13, 21]

# Miembros del equipo (puedes agregar más)
equipo = ["Ana", "Pedro", "Luis", "Marta"]

# Simular rondas de votación
def simular_estimacion(tareas):
    estimaciones = {}
    for tarea in tareas:
        votos = {miembro: random.choice(planning_poker_values) for miembro in equipo}
        promedio = np.mean(list(votos.values()))
        estimaciones[tarea] = {
            "votos": votos,
            "promedio": round(promedio, 2)
        }
    return estimaciones

# Tareas de ejemplo
tareas = ["Login", "Carrito de compras", "Checkout", "Dashboard"]

# Ejecutar simulación
resultados = simular_estimacion(tareas)

# Mostrar en consola
for tarea, datos in resultados.items():
    print(f"Tarea: {tarea}")
    print(f"Votos: {datos['votos']}")
    print(f"Promedio estimado: {datos['promedio']}\n")

# Gráfico comparativo
plt.bar(resultados.keys(), [datos["promedio"] for datos in resultados.values()])
plt.title("Estimaciones de Story Points por Tarea")
plt.ylabel("Promedio Story Points")
plt.show()
