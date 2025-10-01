import matplotlib.pyplot as plt

# Datos de entrada: puntos de historia completados por sprint
historias_por_sprint = [5, 3, 8, 2, 6, 4]  # Ejemplo
puntos_restantes = 100  # Puntos de historia en el backlog
duracion_sprint_dias = 7  # Duración en días

# Calcular la velocidad promedio
velocidad = sum(historias_por_sprint) / len(historias_por_sprint)
print(f"Velocidad promedio: {velocidad:.2f} puntos de historia por sprint")

# Proyectar sprints requeridos
sprints_requeridos = puntos_restantes / velocidad
print(f"Sprints requeridos para completar {puntos_restantes} puntos: {sprints_requeridos:.1f}")

# Proyectar días totales
dias_totales = sprints_requeridos * duracion_sprint_dias
print(f"Días estimados: {dias_totales:.0f} días (~{dias_totales/7:.1f} semanas)")

# Generar datos para Burndown Chart
sprints = list(range(1, len(historias_por_sprint) + 1))
puntos_acumulados = [puntos_restantes - sum(historias_por_sprint[:i+1]) for i in range(len(historias_por_sprint))]
puntos_acumulados.insert(0, puntos_restantes)  # Sprint inicial
sprints.insert(0, 0)

# Crear Burndown Chart
plt.figure(figsize=(10, 6))
plt.plot(sprints, puntos_acumulados, marker='o', linestyle='-', color='b')
plt.title("Burndown Chart Simulado")
plt.xlabel("Número de Sprint")
plt.ylabel("Puntos de Historia Restantes")
plt.grid(True)
plt.savefig("burndown_chart.png")
plt.show()

print("\nGráfico guardado como 'burndown_chart.png'")
