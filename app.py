import streamlit as st
from PIL import Image

st.title(" Taylor Swift — Mi Primera App")

st.header("Este es un espacio para jugar con una app temática de las ERAS.")
st.write("Aquí conecto UI con vibes Swifties: misma estructura, nueva narrativa.")
image = Image.open('taylor_eras.png')

st.image(image, caption='The Eras Tour (versión app)')

texto = st.text_input('Escribe tu era favorita', "1989 (Taylor's Version)")
st.write('Tu elección fue:', texto)

st.subheader("Ahora usemos 2 Columnas")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Primera columna — Eras")
    st.write("Las interfaces multimodales también mejoran la experiencia de un concierto en streaming.")
    resp = st.checkbox('Soy Swiftie')
    if resp:
       st.write('¡Welcome to New York! 🎧')
  
with col2:
    st.subheader("Segunda columna — Modalidad principal")
    modo = st.radio("Que Modalidad es la principal en tu interfaz", ('Visual', 'auditiva', 'Táctil'))
    if modo == 'Visual':
       st.write('La puesta en escena brilla: vestuarios, luces y pantallas.')
    if modo == 'auditiva':
       st.write('Las letras y la producción llevan la emoción.')
    if modo == 'Táctil':
       st.write('El ritmo se siente: vibración y compases en el cuerpo.')
        
st.subheader("Uso de Botones")
if st.button('Presiona el botón'):
    st.write('¡Gracias por presionar! (Shake It Off 🕺)')
else:
    st.write('Aún no has presionado — Are you ready for it?')

st.subheader("Selectbox")
in_mod = st.selectbox(
    "Selecciona la modalidad",
    ("Audio", "Visual", "Háptico"),
)
if in_mod == "Audio":
    set_mod = "Reproducir un fragmento de 'Love Story'"
elif in_mod == "Visual":
    set_mod = "Mostrar un videoclip de la era 1989"
elif in_mod == "Háptico":
    set_mod = "Activar vibración al ritmo de 'Cruel Summer'"
st.write(" La acción es:" , set_mod)

with st.sidebar:
    st.subheader("Configura la modalidad")
    mod_radio = st.radio(
        "Escoge la modalidad a usar",
        ("Visual", "Auditiva","Háptica")
    )
