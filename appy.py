import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def calcular_funcion_lineal(funcion_str, x_val):
    try:
        x = x_val
        resultado = eval(funcion_str)
        return resultado
    except Exception as e:
        return f"Error: {e}"

def graficar_funcion(funcion_str, x_val, y_val):
    try:
        x_vals = np.linspace(x_val - 10, x_val + 10, 400)
        y_vals = []
        for val in x_vals:
            x = val
            y_vals.append(eval(funcion_str))
        y_vals = np.array(y_vals)

        plt.figure(figsize=(8,5))
        plt.plot(x_vals, y_vals, label=f"f(x) = {funcion_str}")
        plt.scatter([x_val], [y_val], color='red', zorder=5, label=f"Punto ({x_val}, {y_val})")
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.title("Gráfica de la función lineal")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.legend()
        plt.grid(True)
        st.pyplot(plt)
        plt.close()
    except Exception as e:
        st.error(f"Error al graficar: {e}")

def main():
    st.title("Calculadora de Función Lineal")

    if "funcion" not in st.session_state:
        st.session_state.funcion = ""
    if "mostrar_input_funcion" not in st.session_state:
        st.session_state.mostrar_input_funcion = False
    if "resultado" not in st.session_state:
        st.session_state.resultado = None
    if "x_val" not in st.session_state:
        st.session_state.x_val = 0.0

    if st.button("Ingresar función lineal"):
        st.session_state.mostrar_input_funcion = True

    if st.session_state.mostrar_input_funcion:
        funcion_input = st.text_input("Escribe la función en términos de x (ejemplo: 2*x + 3)", value=st.session_state.funcion)
        if funcion_input:
            st.session_state.funcion = funcion_input
            st.success(f"Función guardada: `{st.session_state.funcion}`")

    if st.session_state.funcion:
        st.write(f"Función actual: `{st.session_state.funcion}`")

        st.session_state.x_val = st.number_input("Ingresa el valor de x:", value=st.session_state.x_val)

        if st.button("Calcular resultado"):
            st.session_state.resultado = calcular_funcion_lineal(st.session_state.funcion, st.session_state.x_val)
            st.write(f"Resultado: {st.session_state.resultado}")

        if st.button("Graficar función"):
            if st.session_state.resultado is not None and not isinstance(st.session_state.resultado, str):
                graficar_funcion(st.session_state.funcion, st.session_state.x_val, st.session_state.resultado)
            else:
                st.warning("Primero calcula el resultado para poder graficar el punto.")

if __name__ == "__main__":
    main()
