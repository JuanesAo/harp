import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(
    page_title="Mis Gustos Musicales 🎵",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS personalizado con temática de amor (negro y rojo) - Optimizado para móviles
st.markdown("""
    <style>
    /* Fondo general */
    .stApp {
        background: linear-gradient(135deg, #1a0000 0%, #000000 50%, #1a0000 100%);
        padding: 10px;
    }
    
    /* Ocultar elementos de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Título principal - Responsive */
    .title {
        text-align: center;
        color: #ff0000;
        font-size: clamp(1.8em, 5vw, 2.5em);
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(255, 0, 0, 0.5);
        margin-bottom: 20px;
        font-family: 'Georgia', serif;
        padding: 10px;
    }
    
    /* Mensaje romántico - Responsive */
    .romantic-message {
        text-align: center;
        color: #ffcccc;
        font-size: clamp(1em, 3.5vw, 1.3em);
        line-height: 1.6;
        padding: clamp(15px, 5vw, 30px);
        margin: 20px auto;
        background: rgba(139, 0, 0, 0.3);
        border-radius: 15px;
        border: 2px solid #ff0000;
        box-shadow: 0 0 20px rgba(255, 0, 0, 0.3);
        font-family: 'Georgia', serif;
        max-width: 90%;
    }
    
    /* Botones - Optimizados para móviles */
    .stButton > button {
        background: linear-gradient(135deg, #ff0000 0%, #cc0000 100%);
        color: white !important;
        border: none;
        padding: 15px 20px;
        font-size: clamp(1em, 4vw, 1.2em);
        font-weight: bold;
        border-radius: 25px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255, 0, 0, 0.4);
        width: 100%;
        margin-top: 10px;
        min-height: 50px;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #cc0000 0%, #990000 100%);
        box-shadow: 0 6px 20px rgba(255, 0, 0, 0.6);
        transform: scale(1.02);
    }
    
    .stButton > button:active {
        transform: scale(0.98);
    }
    
    /* Corazones decorativos */
    .hearts {
        text-align: center;
        font-size: clamp(1.5em, 5vw, 2em);
        margin: 20px 0;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% {
            opacity: 1;
            transform: scale(1);
        }
        50% {
            opacity: 0.7;
            transform: scale(1.1);
        }
    }
    
    /* Cards - Responsive */
    .card-container {
        background: linear-gradient(145deg, #1a0000, #330000);
        border: 2px solid #ff0000;
        border-radius: 20px;
        padding: clamp(15px, 4vw, 25px);
        margin: 15px auto;
        text-align: center;
        box-shadow: 0 8px 25px rgba(255, 0, 0, 0.4);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        max-width: 400px;
    }
    
    .card-container:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 35px rgba(255, 0, 0, 0.6);
    }
    
    .card-title {
        color: #ff0000;
        font-size: clamp(1.2em, 4vw, 1.5em);
        font-weight: bold;
        margin: 15px 0;
        font-family: 'Arial', sans-serif;
    }
    
    /* Contenedor de columnas responsive */
    [data-testid="column"] {
        padding: 5px !important;
    }
    
    /* Footer romántico */
    .footer-message {
        text-align: center;
        color: #ff6666;
        font-size: clamp(0.9em, 3vw, 1.1em);
        margin-top: 30px;
        font-style: italic;
        padding: 10px;
    }
    
    /* Imágenes responsive */
    img {
        max-width: 100%;
        height: auto;
    }
    
    /* Media queries adicionales para móviles pequeños */
    @media (max-width: 640px) {
        .stApp {
            padding: 5px;
        }
        
        [data-testid="column"] {
            min-width: 100% !important;
            flex: 100% !important;
        }
        
        .card-container {
            margin: 10px 0;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Título
st.markdown('<div class="title">❤️ Para Ti ❤️</div>', unsafe_allow_html=True)

# Mensaje romántico
st.markdown("""
    <div class="romantic-message">
        Quiero que una parte de mí viva en ti...<br>
        Mis gustos musicales, mis canciones favoritas,<br>
        todo lo que me hace sentir vivo.<br>
        <br>
        Cada melodía es un pedazo de mi alma<br>
        que quiero compartir contigo 🎵❤️
    </div>
""", unsafe_allow_html=True)

# Corazones decorativos
st.markdown('<div class="hearts">❤️ 🖤 ❤️</div>', unsafe_allow_html=True)

# Cards con botones - Responsive para móviles
col1, col2 = st.columns(2, gap="medium")

# Card Apple Music
with col1:
    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    
    # Logo de Apple Music
    try:
        apple_logo = Image.open("imagenes/logos/apple_music.jpg")
        st.image(apple_logo, use_container_width=True)
    except:
        st.markdown('<div style="font-size: 3em; margin: 20px 0;">🍎</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="card-title">Apple Music</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Botón para Apple Music
    if st.button("🎵 Ir a Apple Music", key="apple", use_container_width=True):
        # Aquí irá el link de Apple Music
        apple_music_link = "https://music.apple.com"  # Reemplazar con tu link
        st.link_button("🎵 Abrir Apple Music", apple_music_link, use_container_width=True)
        st.success("¡Disfruta la música! 🎵")

# Card Spotify
with col2:
    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    
    # Logo de Spotify
    try:
        spotify_logo = Image.open("imagenes/logos/spotify logo.png")
        st.image(spotify_logo, use_container_width=True)
    except:
        st.markdown('<div style="font-size: 3em; margin: 20px 0;">🟢</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="card-title">Spotify</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Botón para Spotify
    if st.button("🎵 Ir a Spotify", key="spotify", use_container_width=True):
        # Aquí irá el link de Spotify
        spotify_link = "https://open.spotify.com"  # Reemplazar con tu link
        st.link_button("🎵 Abrir Spotify", spotify_link, use_container_width=True)
        st.success("¡Disfruta la música! 🎵")

# Pie de página romántico
st.markdown('<div class="hearts">🖤</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="footer-message">
        Con amor, para que siempre me recuerdes a través de la música 🎶
    </div>
""", unsafe_allow_html=True)

