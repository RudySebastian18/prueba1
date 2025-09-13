import streamlit as st

def calcular_funcion_lineal(funcion_str, x_val):
    try:
        # Definir la variable x en el contexto de eval
        x = x_val
        # Evaluar la función ingresada por el usuario
        resultado = eval(funcion_str)
        return resultado
    except Exception as e:
        return f"Error: {e}"

def main():
    st.title("Calculadora de Función Lineal")

    # Estado para guardar la función ingresada
    if "funcion" not in st.session_state:
        st.session_state.funcion = ""

    # Botón para ingresar función lineal
    if st.button("Ingresar función lineal"):
        funcion_input = st.text_input("Escribe la función en términos de x (ejemplo: 2*x + 3)")
        if funcion_input:
            st.session_state.funcion = funcion_input
            st.success(f"Función guardada: {st.session_state.funcion}")

    if st.session_state.funcion:
        st.write(f"Función actual: `{st.session_state.funcion}`")

        # Entrada para valor de x
        x_val = st.number_input("Ingresa el valor de x:", value=0.0)

        # Botón para calcular resultado
        if st.button("Calcular resultado"):
            resultado = calcular_funcion_lineal(st.session_state.funcion, x_val)
            st.write(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()
