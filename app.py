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
        gap: 30px;
        margin-top: 40px;
        flex-wrap: wrap;
    }
    
    /* Estilos de las cards */
    .card {
        background: linear-gradient(145deg, #1a0000, #330000);
        border: 2px solid #ff0000;
        border-radius: 20px;
        padding: 30px;
        width: 250px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(255, 0, 0, 0.4);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-10px);
        box-shadow: 0 12px 35px rgba(255, 0, 0, 0.6);
    }
    
    .card-icon {
        font-size: 4em;
        margin-bottom: 15px;
    }
    
    .card-title {
        color: #ff0000;
        font-size: 1.5em;
        font-weight: bold;
        margin-bottom: 20px;
        font-family: 'Arial', sans-serif;
    }
    
    /* Botones */
    .stButton > button {
        background: linear-gradient(135deg, #ff0000 0%, #cc0000 100%);
        color: white;
        border: none;
        padding: 12px 30px;
        font-size: 1.1em;
        font-weight: bold;
        border-radius: 25px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255, 0, 0, 0.4);
        width: 100%;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #cc0000 0%, #990000 100%);
        box-shadow: 0 6px 20px rgba(255, 0, 0, 0.6);
        transform: scale(1.05);
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

# Cards con botones
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div style="text-align: center; margin-bottom: 20px;">', unsafe_allow_html=True)
    st.image("imagenes/logos/apple_music.jpg", width=200)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Botón para Apple Music
    if st.button("🎵 Escuchar en Apple Music", key="apple"):
        # Aquí irá el link de Apple Music
        apple_music_link = "https://music.apple.com"  # Reemplazar con tu link
        st.markdown(f'<meta http-equiv="refresh" content="0;url={apple_music_link}">', unsafe_allow_html=True)
        st.success("Redirigiendo a Apple Music...")

with col2:
    st.markdown('<div style="text-align: center; margin-bottom: 20px;">', unsafe_allow_html=True)
    st.image("imagenes/logos/spotify logo.png", width=200)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Botón para Spotify
    if st.button("🎵 Escuchar en Spotify", key="spotify"):
        # Aquí irá el link de Spotify
        spotify_link = "https://open.spotify.com"  # Reemplazar con tu link
        st.markdown(f'<meta http-equiv="refresh" content="0;url={spotify_link}">', unsafe_allow_html=True)
        st.success("Redirigiendo a Spotify...")

# Pie de página romántico
st.markdown('<div class="hearts">🖤</div>', unsafe_allow_html=True)
st.markdown("""
    <div style="text-align: center; color: #ff6666; margin-top: 40px; font-style: italic;">
        Con amor, para que siempre me recuerdes a través de la música 🎶
    </div>
""", unsafe_allow_html=True)

