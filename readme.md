# Práctica de Teoria de la complejidad

## 📌 Información General

- **Título:** Teoria de la Complejidad
- **Asignatura:** Estructura de Datos
- **Carrera:** Computación
- **Estudiantes:** Felipe Parra, Wellington Guzman
- **Fecha:** 08/05/2025
- **Profesor:** Ing. Pablo Torres

---

## 🛠️ Descripción
Genera diferentes arreglos de numeros con diferentes tamaños:
• 5.000
• 10.000
• 30.000
• 50.000
• 100.000

Este proyecto implementa y compara diferentes algoritmos de ordenamiento en Python, incluyendo:
- Método Burbuja
- Método Selección
- Método Inserción
- Método Burbuja Mejorado

Para ordenar cada arreglo.Ademas genera un grafico que muestra cual metodo de ordenamiento es el mas eficiente en ordenar  


---

## 🚀 Ejecución

Para ejecutar el proyecto:

1. Instala las dependencias (si es necesario):
   ```bash
   pip install -r requirements.txt

2. Ejecuta el programa principal:
    python app.py

## 🧑‍💻 Ejemplo de Salida

Tamaño: 100, Algoritmo: bubble, Tiempo: 0.0004 segundos
Tamaño: 100, Algoritmo: bubbleMejorado, Tiempo: 0.0005 segundos
Tamaño: 100, Algoritmo: seleccion, Tiempo: 0.0002 segundos
Tamaño: 100, Algoritmo: insercion, Tiempo: 0.0003 segundos
Tamaño: 100, Algoritmo: shell, Tiempo: 0.0000 segundos
Tamaño: 200, Algoritmo: bubble, Tiempo: 0.0014 segundos
Tamaño: 200, Algoritmo: bubbleMejorado, Tiempo: 0.0019 segundos
Tamaño: 200, Algoritmo: seleccion, Tiempo: 0.0009 segundos
Tamaño: 200, Algoritmo: insercion, Tiempo: 0.0010 segundos
Tamaño: 200, Algoritmo: shell, Tiempo: 0.0000 segundos
Tamaño: 300, Algoritmo: bubble, Tiempo: 0.0033 segundos
Tamaño: 300, Algoritmo: bubbleMejorado, Tiempo: 0.0042 segundos
Tamaño: 300, Algoritmo: seleccion, Tiempo: 0.0022 segundos
Tamaño: 300, Algoritmo: insercion, Tiempo: 0.0022 segundos
Tamaño: 300, Algoritmo: shell, Tiempo: 0.0000 segundos
Tamaño: 400, Algoritmo: bubble, Tiempo: 0.0063 segundos
Tamaño: 400, Algoritmo: bubbleMejorado, Tiempo: 0.0077 segundos
Tamaño: 400, Algoritmo: seleccion, Tiempo: 0.0043 segundos
Tamaño: 400, Algoritmo: insercion, Tiempo: 0.0039 segundos
Tamaño: 400, Algoritmo: shell, Tiempo: 0.0000 segundos
Tamaño: 500, Algoritmo: bubble, Tiempo: 0.0102 segundos
Tamaño: 500, Algoritmo: bubbleMejorado, Tiempo: 0.0129 segundos
Tamaño: 500, Algoritmo: seleccion, Tiempo: 0.0071 segundos
Tamaño: 500, Algoritmo: insercion, Tiempo: 0.0063 segundos
Tamaño: 500, Algoritmo: shell, Tiempo: 0.0001 segundos

---
## EJEMPLO DE ADICIÓN DE DATOS EN ESTE INFORME

![Comparación de métodos](./images/Comparacion-metodos.png)


##  CONCLUCIONES CON TERMINOLOGIA DE NOTACION 

## Conclusion Felipe Parra:
En esta práctica se evaluó el rendimiento de varios algoritmos de ordenamiento utilizando notación Big O para analizar su complejidad temporal. Los métodos Bubble Sort, Selección e Inserción presentaron un crecimiento cuadrático `O(n²)`, mostrando ineficiencia al aumentar el tamaño del arreglo. Aunque el algoritmo de Inserción puede alcanzar `O(n)` en su mejor caso, en entradas aleatorias su comportamiento sigue siendo `O(n²)`. En contraste, Shell Sort (o `sorted()` de Python) demostró una complejidad más eficiente `O(n log n)`, evidenciada por su bajo tiempo de ejecución incluso con arreglos grandes. Además, se garantizó que todos los algoritmos trabajaran sobre copias del mismo arreglo desordenado, evitando sesgos por arreglos previamente ordenados.

## Conclusion Wellington Guzman:
De esta actividad se logró concluir atreves de distintos métodos que el el más eficiente para ordenar grandes cantidades de números aleatorios es Shell sort, con una ejecución más rápida que destaca por sobre los demás métodos empleados. En cuanto a los métodos menos eficientes podemos encontrar a Buble sort, Seleccion e Inserccion mientras más aumenta el tamaño del arreglo. Para realizar las comprobaciones utilizamos arreglos de gran tamaño con números aleatorios, nos aseguramos de que el arreglo siempre este en desorden para que los métodos no tomen los números en orden y de esta manera comprobar su eficiencia.