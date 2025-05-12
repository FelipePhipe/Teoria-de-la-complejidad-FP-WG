from benchmarking import Benchmarking
from metodos_ordenamiento import MetodosOrdenamiento
import matplotlib.pyplot as plt
from datetime import datetime

if __name__ == "__main__":
    bench = Benchmarking()
    metodosO = MetodosOrdenamiento()

    tamanios = [5000, 10000, 30000, 50000, 100000]
    resultados = []

    metodos_dic = {
        "bubble": metodosO.metodo_sort_bubble,
        "bubbleMejorado": metodosO.metodo_sort_bubble_mejorado,
        "seleccion": metodosO.metodo_sort_seleccion,
        "insercion": metodosO.metodo_sort_insercion,
        "shell": sorted
    }

    arreglo_completo = bench.build_arreglo(100000)
    subconjuntos = {
        5000: arreglo_completo[:5000],
        10000: arreglo_completo[:10000],
        30000: arreglo_completo[:30000],
        50000: arreglo_completo[:50000],
        100000: arreglo_completo
    }

    for tam in tamanios:
        arreglo_original = subconjuntos[tam]
    for nombre, metodo in metodos_dic.items():
        arreglo_clonado = arreglo_original.copy()  
        tiempo = bench.medir_tiempo(metodo, arreglo_clonado)
        resultados.append((tam, nombre, tiempo))
        print(f"Tamaño: {tam}, Algoritmo: {nombre}, Tiempo: {tiempo:.4f} segundos")


    tiempos_by_metodo = {nombre: [] for nombre in metodos_dic}
    for tam, nombre, tiempo in resultados:
        tiempos_by_metodo[nombre].append(tiempo)

    plt.figure(figsize=(12, 6))
    now = datetime.now()
    plt.suptitle(f"FELIPE PARRA -WELLINGTON GUZMÁN - {now.strftime('%d/%m/%Y %H:%M:%S')}", fontsize=12, weight='bold')

    ax1 = plt.subplot(1, 2, 1)
    colores = {
        "bubble": "blue",
        "bubbleMejorado": "orange",
        "seleccion": "green",
        "insercion": "purple",
        "shell": "red"
    }

    for nombre, tiempos in tiempos_by_metodo.items():
        ax1.plot(tamanios, tiempos, label=nombre, marker="o", color=colores[nombre])

    ax1.set_title("Comparación de Tiempos de Ejecución de Algoritmos de Ordenamiento")
    ax1.set_xlabel("Tamaño del arreglo")
    ax1.set_ylabel("Tiempo de ejecución (segundos)")
    ax1.grid(True)
    ax1.legend()

    ax2 = plt.subplot(1, 2, 2)
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    ax2.plot(x, y, label="Línea 1", color="blue")
    ax2.set_title("Gráfico de Ejemplo con Matplotlib")
    ax2.set_xlabel("Eje X")
    ax2.set_ylabel("Eje Y")
    ax2.grid(True)
    ax2.legend()

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()
