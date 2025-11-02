
"""
001-E3-logica_proposicional.py
--------------------------------
Este script introduce la lógica proposicional:
- Permite que el usuario defina variables proposicionales y conectivos básicos (¬, ∧, ∨, →, ↔).
- En modo DEMO, se muestran tablas de verdad de ejemplos predefinidos.
- En modo INTERACTIVO, el usuario puede ingresar una expresión sencilla y se evalúa su tabla de verdad.
Autor: Alejandro Aguirre Díaz
"""

def generar_tabla_verdad(variables, expresion_func):
    """
    Genera la tabla de verdad para las variables dadas y una función que evalúa la expresión.
    :param variables: lista de nombres de variables (ej: ['p','q'])
    :param expresion_func: función que acepta un dict var->bool y devuelve bool
    :return: lista de filas: cada fila es (dict de valores, resultado)
    """
    n = len(variables)
    resultados = []
    for i in range(2**n):
        valores = {}
        for j,var in enumerate(variables):
            valores[var] = bool((i >> (n-1-j)) & 1)
        resultado = expresion_func(valores)
        resultados.append((valores.copy(), resultado))
    return resultados

def imprimir_tabla(variables, tabla):
    """
    Imprime la tabla de verdad por pantalla.
    """
    cabecera = " | ".join(variables) + " | Resultado"
    print(cabecera)
    print("-" * len(cabecera))
    for valores, res in tabla:
        linea = " | ".join('T' if valores[var] else 'F' for var in variables)
        linea += " | " + ('T' if res else 'F')
        print(linea)

def modo_demo():
    print("\n--- MODO DEMO: lógica proposicional ---")
    # Ejemplo 1: p → q
    variables = ['p','q']
    def expr(val): return (not val['p']) or val['q']
    print("Ejemplo: p → q")
    tabla = generar_tabla_verdad(variables, expr)
    imprimir_tabla(variables, tabla)
    # Ejemplo 2: (p ∨ q) ∧ ¬p
    def expr2(val): return (val['p'] or val['q']) and (not val['p'])
    print("\nEjemplo: (p ∨ q) ∧ ¬p")
    tabla2 = generar_tabla_verdad(variables, expr2)
    imprimir_tabla(variables, tabla2)

def modo_interactivo():
    print("\n--- MODO INTERACTIVO: lógica proposicional ---")
    vars_input = input("Introduce variables separadas por coma (ej: p,q): ").strip()
    variables = [v.strip() for v in vars_input.split(',') if v.strip()]
    print("Variables:", variables)
    print("Ahora define la expresión usando Python: por ejemplo 'not p or q' para p → q.")
    expr_input = input("Expresión = ").strip()
    def expr(val_map):
        return eval(expr_input, {}, val_map)
    try:
        tabla = generar_tabla_verdad(variables, expr)
        imprimir_tabla(variables, tabla)
    except Exception as e:
        print("Error al evaluar la expresión:", e)

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
