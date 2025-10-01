import pandas as pd

# Nombre del archivo de Excel
archivo_excel = 'presupuesto_proyecto_v1.xlsx'

print(f"--- Leyendo el archivo: {archivo_excel} ---")

try:
    # Mostrar las hojas disponibles
    xls = pd.ExcelFile(archivo_excel)
    print("Hojas disponibles en el archivo:", xls.sheet_names)

    # Escoger la primera hoja automáticamente
    nombre_hoja = xls.sheet_names[0]

    # Leer el archivo Excel usando la hoja detectada
    df_costos = pd.read_excel(archivo_excel, sheet_name=nombre_hoja)

    # Mostrar los datos leídos
    print("\nDatos leídos desde Excel:")
    print(df_costos)

    # Calcular la columna 'Costo Total (COP)'
    df_costos['Costo Total (COP)'] = df_costos['Horas Estimadas'] * df_costos['Tarifa por Hora (COP)']

    # Calcular el costo total del proyecto
    costo_total_proyecto = df_costos['Costo Total (COP)'].sum()

    # Mostrar los resultados
    print("\n--- Presupuesto Calculado ---")
    print("\nDetalle de costos por tarea:")
    print(df_costos)

    print("\n-----------------------------------------------------")
    print(f"Costo Total Directo del Proyecto: ${costo_total_proyecto:,.2f} COP")
    print("-----------------------------------------------------")

except FileNotFoundError:
    print(f"\n¡ERROR! No se encontró el archivo '{archivo_excel}'.")
    print("Asegúrate de que el archivo esté en la misma carpeta que el script.")
