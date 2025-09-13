import streamlit as st

def calcular_funcion_lineal(funcion_str, x_val):
    try:
        x = x_val
        resultado = eval(funcion_str)
        return resultado
    except Exception as e:
        return f"Error: {e}"

def main():
    st.title("Calculadora de Función Lineal")

    # Inicializamos la función en el estado si no existe
    if "funcion" not in st.session_state:
        st.session_state.funcion = ""

    # Botón para mostrar input para función lineal
    if st.button("Ingresar función lineal"):
        st.session_state.mostrar_input_funcion = True
    else:
        if "mostrar_input_funcion" not in st.session_state:
            st.session_state.mostrar_input_funcion = False

    # Mostrar input para la función solo si el botón fue presionado
    if st.session_state.mostrar_input_funcion:
        funcion_input = st.text_input("Escribe la función en términos de x (ejemplo: 2*x + 3)")
        if funcion_input:
            st.session_state.funcion = funcion_input
            st.success(f"Función guardada: `{st.session_state.funcion}`")

    if st.session_state.funcion:
        st.write(f"Función actual: `{st.session_state.funcion}`")

        x_val = st.number_input("Ingresa el valor de x:", value=0.0)

        # Botón para calcular resultado
        if st.button("Calcular resultado"):
            resultado = calcular_funcion_lineal(st.session_state.funcion, x_val)
            st.write(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()
