import streamlit as st

# CSS personalizado para colores y estilo
st.markdown(
    """
    <style>
    /* Fondo relajante (verde agua suave) */
    .stApp {
        background: linear-gradient(135deg, #a8edea, #fed6e3);
        color: #222222;
        font-family: 'Poppins', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        padding: 2rem;
    }

    /* Títulos con fuente más llamativa y color vibrante */
    h1, h2, h3, h4, h5 {
        color: #1b4965; /* Azul oscuro */
        font-family: 'Poppins', sans-serif;
        font-weight: 800;
        text-shadow: 1px 1px 2px #cce3e6;
    }

    /* Texto normal */
    .stText {
        color: #264653; /* Azul moderado */
        font-family: 'Poppins', sans-serif;
        font-size: 1.1rem;
        line-height: 1.6;
    }

    /* Botones estilizados */
    div.stButton > button {
        background-color: #2a9d8f; /* Verde azulado */
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.6rem 1.8rem;
        font-size: 1.1rem;
        font-weight: 700;
        transition: background-color 0.3s ease;
        cursor: pointer;
        box-shadow: 0 4px 6px rgba(42, 157, 143, 0.4);
    }

    div.stButton > button:hover {
        background-color: #21867a; /* Verde azulado más oscuro */
        color: #e0f7f4;
    }

    /* Separadores */
    hr {
        border: 2px solid #2a9d8f;
        margin: 2rem 0;
    }
    </style>

    <!-- Fuente Poppins desde Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;700;800&display=swap" rel="stylesheet">
    """,
    unsafe_allow_html=True
)

def mostrar_historia():
    st.header("Historia de Richard Stallman")
    st.write("""
    Richard Matthew Stallman, conocido comúnmente como RMS, nació en 1953 en Nueva York.  
    Es un programador, activista y fundador del movimiento del software libre.  
    En 1983, frustrado por las restricciones que imponían las compañías de software propietario,  
    inició el **Proyecto GNU**, cuyo objetivo era crear un sistema operativo completamente libre que cualquiera pudiera usar, estudiar, modificar y compartir.  

    Stallman también fundó la **Free Software Foundation (FSF)** en 1985, para promover y proteger los derechos de los usuarios del software libre.  
    A lo largo de su vida, ha sido un defensor incansable de la ética del software libre, la privacidad y la libertad digital, influyendo profundamente en la cultura tecnológica mundial.

    Gracias a su trabajo, conceptos como la copyleft y licencias libres como la GNU GPL se convirtieron en pilares fundamentales del software libre.
    """)

def mostrar_libertades():
    st.header("Las 4 libertades esenciales del software libre")
    st.write("""
    Richard Stallman definió las **4 libertades esenciales** que debe garantizar un software para ser considerado libre:

    1. **Libertad 0: Usar el programa para cualquier propósito.**  
    Sin restricciones sobre cómo y para qué puedes utilizar el software.

    2. **Libertad 1: Estudiar cómo funciona el programa y modificarlo.**  
    Esto requiere acceso al código fuente, lo que permite adaptarlo a tus necesidades.

    3. **Libertad 2: Redistribuir copias para ayudar a otros.**  
    Puedes compartir el software con tus amigos, compañeros o la comunidad.

    4. **Libertad 3: Mejorar el programa y publicar tus mejoras.**  
    De esta manera, toda la comunidad se beneficia de las mejoras y avances realizados.

    Estas libertades buscan garantizar que el software respete la libertad del usuario y fomente la colaboración abierta.
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
        respuesta = st.radio("", opciones, key=f"pregunta_{i}")
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
    st.image("https://upload.wikimedia.org/wikipedia/commons/5/55/Richard_Stallman_photographed_by_Kilian_Mazzone.jpg", caption="Richard Stallman", use_column_width=True)

mostrar_historia()
    mostrar_historia()
    st.markdown("---")
    mostrar_libertades()
    st.markdown("---")
    quiz()

if __name__ == "__main__":
    main()
