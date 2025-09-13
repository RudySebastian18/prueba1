import streamlit as st

def mostrar_historia():
    st.header("Historia de Richard Stallman")
    st.write("""
    Richard Stallman (nacido en 1953) es un programador y activista estadounidense 
    conocido por su trabajo en el movimiento del software libre.  
    En 1983, Stallman inició el proyecto GNU con la idea de crear un sistema operativo completamente libre.  
    Además, fundó la Free Software Foundation en 1985 para apoyar el desarrollo y la defensa del software libre.
    """)

def mostrar_libertades():
    st.header("Las 4 libertades del software libre")
    st.write("""
    Las 4 libertades definidas por Richard Stallman que caracterizan el software libre son:

    1. **Libertad 0:** La libertad de usar el programa, con cualquier propósito.
    2. **Libertad 1:** La libertad de estudiar cómo funciona el programa y adaptarlo a tus necesidades (acceso al código fuente).
    3. **Libertad 2:** La libertad de distribuir copias para ayudar a otros.
    4. **Libertad 3:** La libertad de mejorar el programa y publicar esas mejoras al público, para que toda la comunidad se beneficie.
    """)

def quiz():
    st.header("Quiz: ¿Qué tanto sabes sobre Richard Stallman y las libertades del software libre?")
    
    preguntas = [
        {
            "pregunta": "¿En qué año Richard Stallman inició el proyecto GNU?",
            "opciones": ["1980", "1983", "1990", "1985"],
            "respuesta": "1983"
        },
        {
            "pregunta": "¿Cuál organización fundó Stallman para apoyar el software libre?",
            "opciones": ["Free Software Foundation", "Linux Foundation", "Apache Foundation", "Mozilla Foundation"],
            "respuesta": "Free Software Foundation"
        },
        {
            "pregunta": "¿Qué libertad permite estudiar y modificar el código fuente?",
            "opciones": [
                "Libertad 0", 
                "Libertad 1", 
                "Libertad 2", 
                "Libertad 3"
            ],
            "respuesta": "Libertad 1"
        },
        {
            "pregunta": "¿Cuál libertad permite distribuir copias del software?",
            "opciones": [
                "Libertad 0",
                "Libertad 1",
                "Libertad 2",
                "Libertad 3"
            ],
            "respuesta": "Libertad 2"
        },
        {
            "pregunta": "¿Qué libertad permite publicar mejoras para beneficio de la comunidad?",
            "opciones": [
                "Libertad 0",
                "Libertad 1",
                "Libertad 2",
                "Libertad 3"
            ],
            "respuesta": "Libertad 3"
        }
    ]

    respuestas_usuario = []

    for i, q in enumerate(preguntas):
        st.subheader(f"Pregunta {i+1}")
        st.write(q["pregunta"])
        opciones = q["opciones"]
        respuesta = st.radio("Selecciona una opción:", opciones, key=f"pregunta_{i}")
        respuestas_usuario.append(respuesta)

    if st.button("Enviar respuestas"):
        puntaje = 0
        for i, q in enumerate(preguntas):
            if respuestas_usuario[i] == q["respuesta"]:
                puntaje += 1
        st.success(f"Tu puntaje es {puntaje} de {len(preguntas)}")
        if puntaje == len(preguntas):
            st.balloons()

def main():
    st.title("Historia de Richard Stallman y las 4 libertades del software libre")

    mostrar_historia()
    st.markdown("---")
    mostrar_libertades()
    st.markdown("---")
    quiz()

if __name__ == "__main__":
    main()
