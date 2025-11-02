
"""
002-E3-logica_de_primer_orden.py
--------------------------------
Este script introduce la lógica de primer orden (FOL – First-Order Logic):
- En modo DEMO, se presenta la sintaxis básica: constantes, variables, predicados y cuantificadores (∀, ∃).
- En modo INTERACTIVO, el usuario puede definir una base de hechos muy sencilla y hacer consultas sobre esos hechos.
Autor: Alejandro Aguirre Díaz
"""

def demo_sintaxis():
    print("\n--- DEMO: sintaxis de la lógica de primer orden ---")
    print("Constantes: a, b, c")
    print("Variables: x, y, z")
    print("Predicados: P(x), Q(x,y)")
    print("Ejemplo de fórmula: ∀x P(x) → ∃y Q(x,y)")
    print("Evaluación simbólica no implementada: solo demostración de forma.")

def modo_demo():
    print("\n--- MODO DEMO: lógica de primer orden ---")
    demo_sintaxis()

def modo_interactivo():
    print("\n--- MODO INTERACTIVO: lógica de primer orden ---")
    print("Definamos una base de hechos muy simple.")
    hechos = []
    print("Introduce hechos del tipo: P(a) o Q(a,b). Para terminar teclea 'fin'.")
    while True:
        h = input("Hecho = ").strip()
        if h.lower() == 'fin':
            break
        hechos.append(h)
    print("Hechos registrados:", hechos)
    consulta = input("Ahora escribe una consulta sencilla (ej: P(a), Q(a,b)) = ").strip()
    print("Nota: esta versión no hace inferencia automática, solo busca coincidencias exactas.")
    if consulta in hechos:
        print("La consulta es **verdadera** según la base de hechos.")
    else:
        print("La consulta **no está registrada** como verdadera en la base de hechos.")

def main():
    print("Seleccione modo de ejecución:")
    print("1) Modo DEMO")
    print("2) Modo INTERACTIVO\n")
    opcion = input("Ingrese 1 o 2: ").strip()
    if opcion == '2':
        modo_interactivo()
    else:
        modo_demo()

if __name__ == "__main__":
    main()
