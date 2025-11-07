import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Mis Gustos Musicales 🎵",
    page_icon="❤️",
    layout="centered"
)

# CSS personalizado con temática de amor (negro y rojo)
st.markdown("""
    <style>
    /* Fondo general */
    .stApp {
        background: linear-gradient(135deg, #1a0000 0%, #000000 50%, #1a0000 100%);
    }
    
    /* Título principal */
    .title {
        text-align: center;
        color: #ff0000;
        font-size: 2.5em;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(255, 0, 0, 0.5);
        margin-bottom: 20px;
        font-family: 'Georgia', serif;
    }
    
    /* Mensaje romántico */
    .romantic-message {
        text-align: center;
        color: #ffcccc;
        font-size: 1.3em;
        line-height: 1.6;
        padding: 30px;
        margin: 30px 0;
        background: rgba(139, 0, 0, 0.3);
        border-radius: 15px;
        border: 2px solid #ff0000;
        box-shadow: 0 0 20px rgba(255, 0, 0, 0.3);
        font-family: 'Georgia', serif;
    }
    
    /* Container de cards */
    .cards-container {
        display: flex;
        justify-content: center;
        gap: 40px;
        margin-top: 40px;
        flex-wrap: wrap;
        padding: 0 20px;
    }
    
    /* Estilos de las cards */
    .music-card {
        background: linear-gradient(145deg, #1a0000, #330000);
        border: 3px solid #ff0000;
        border-radius: 20px;
        padding: 40px 30px;
        min-width: 280px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(255, 0, 0, 0.4);
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
    }
    
    .music-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255, 0, 0, 0.1) 0%, transparent 70%);
        opacity: 0;
        transition: opacity 0.4s ease;
    }
    
    .music-card:hover {
        transform: translateY(-15px) scale(1.05);
        box-shadow: 0 15px 40px rgba(255, 0, 0, 0.7);
        border-color: #ff3333;
    }
    
    .music-card:hover::before {
        opacity: 1;
    }
    
    .card-image-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 25px;
        padding: 20px;
        background: rgba(0, 0, 0, 0.3);
        border-radius: 15px;
        transition: all 0.3s ease;
    }
    
    .music-card:hover .card-image-container {
        background: rgba(255, 0, 0, 0.1);
        transform: scale(1.05);
    }
    
    /* Ocultar el container de streamlit */
    .stImage {
        display: flex !important;
        justify-content: center !important;
    }
    
    /* Botones */
    .stButton > button {
        background: linear-gradient(135deg, #ff0000 0%, #cc0000 100%);
        color: white;
        border: none;
        padding: 15px 30px;
        font-size: 1.1em;
        font-weight: bold;
        border-radius: 25px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255, 0, 0, 0.4);
        width: 100%;
        position: relative;
        z-index: 10;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #ff3333 0%, #ff0000 100%);
        box-shadow: 0 6px 25px rgba(255, 0, 0, 0.8);
        transform: scale(1.08);
    }
    
    /* Centrar columnas */
    .stColumn {
        display: flex;
        justify-content: center;
    }
    
    /* Ajustar imágenes */
    .stImage > img {
        border-radius: 10px;
        max-width: 200px;
        width: 100%;
        height: auto;
    }
    
    /* Corazones decorativos */
    .hearts {
        text-align: center;
        font-size: 2em;
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

# Contenedor de cards
st.markdown('<div class="cards-container">', unsafe_allow_html=True)

# Cards con botones
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown('<div class="music-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-image-container">', unsafe_allow_html=True)
    st.image("imagenes/logos/apple_music.jpg", width=200)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Botón para Apple Music
    if st.button("🎵 Escuchar en Apple Music", key="apple", use_container_width=True):
        # Aquí irá el link de Apple Music
        apple_music_link = "https://music.apple.com"  # Reemplazar con tu link
        st.markdown(f'<meta http-equiv="refresh" content="0;url={apple_music_link}">', unsafe_allow_html=True)
        st.success("Redirigiendo a Apple Music...")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="music-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-image-container">', unsafe_allow_html=True)
    st.image("imagenes/logos/spotify logo.png", width=200)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Botón para Spotify
    if st.button("🎵 Escuchar en Spotify", key="spotify", use_container_width=True):
        # Aquí irá el link de Spotify
        spotify_link = "https://open.spotify.com"  # Reemplazar con tu link
        st.markdown(f'<meta http-equiv="refresh" content="0;url={spotify_link}">', unsafe_allow_html=True)
        st.success("Redirigiendo a Spotify...")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Pie de página romántico
st.markdown('<div class="hearts">🖤</div>', unsafe_allow_html=True)
st.markdown("""
    <div style="text-align: center; color: #ff6666; margin-top: 40px; font-style: italic;">
        Con amor, para que siempre me recuerdes a través de la música 🎶
    </div>
""", unsafe_allow_html=True)

