import streamlit as st
import base64
import os
import glob
from PIL import Image
import io

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
    
    /* Estilos de las cards personalizadas */
    .music-card {
        background: linear-gradient(145deg, #1a0000, #330000);
        border: 3px solid #ff0000;
        border-radius: 20px;
        padding: 40px 30px;
        min-width: 280px;
        max-width: 320px;
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
    
    /* Contenedor de imágenes dentro de cards */
    .card-image-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 30px;
        padding: 20px;
        background: rgba(0, 0, 0, 0.3);
        border-radius: 15px;
        transition: all 0.3s ease;
    }
    
    .music-card:hover .card-image-container {
        background: rgba(255, 0, 0, 0.1);
        transform: scale(1.05);
    }
    
    .card-image-container img {
        border-radius: 10px;
        width: 200px;
        height: auto;
    }
    
    /* Botón dentro de card */
    .card-button {
        display: inline-block;
        background: linear-gradient(135deg, #ff0000 0%, #cc0000 100%);
        color: white;
        text-decoration: none;
        padding: 15px 30px;
        font-size: 1.1em;
        font-weight: bold;
        border-radius: 25px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255, 0, 0, 0.4);
        width: 100%;
        text-align: center;
        position: relative;
        z-index: 10;
    }
    
    .card-button:hover {
        background: linear-gradient(135deg, #ff3333 0%, #ff0000 100%);
        box-shadow: 0 6px 25px rgba(255, 0, 0, 0.8);
        transform: scale(1.08);
        text-decoration: none;
        color: white;
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
    
    /* Responsive para móviles */
    @media (max-width: 768px) {
        .title {
            font-size: 1.8em;
        }
        .romantic-message {
            font-size: 1em;
            padding: 20px;
        }
        .music-card {
            min-width: 100%;
            max-width: 100%;
            padding: 30px 20px;
        }
        .card-image-container img {
            width: 150px;
        }
        .card-button {
            font-size: 1em;
            padding: 12px 20px;
        }
    }
    @media (max-width: 480px) {
        .title {
            font-size: 1.5em;
        }
        .romantic-message {
            font-size: 0.9em;
            padding: 15px;
        }
        .card-image-container img {
            width: 120px;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Título
st.markdown('<div class="title">🌹 Para Harp / Manu 🌹</div>', unsafe_allow_html=True)

# Mensaje romántico
st.markdown("""
    <div class="romantic-message">
        Mis sentimientos fueron tan grandes<br>
        que logré partirlos en 189 pedacitos,<br>
        y a cada uno le di forma de canción.<br>
        <br>
        No sé si esta playlist es tristeza, amor o memoria.<br>
        Solo sé que cada melodía guarda algo mío que alguna vez fue tuyo.<br>
        <br>
        Y si alguna vez la escuchas,<br>
        que sepas que ahí sigo,<br>
        en cada verso que quema, en cada acorde que sana,<br>
        esperando que el eco de mi alma aún te encuentre.
    </div>
""", unsafe_allow_html=True)

# Corazones decorativos
st.markdown('<div class="hearts">❤️ 🖤 ❤️</div>', unsafe_allow_html=True)

# Cards con botones usando HTML y cargando imágenes con base64
# Función para convertir imagen a base64
def get_image_base64(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

# Función optimizada para carrusel (redimensiona y comprime)
def get_optimized_image_base64(image_path, max_size=300, quality=60):
    try:
        img = Image.open(image_path)
        # Convertir RGBA a RGB si es necesario
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        # Redimensionar manteniendo proporción
        img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
        # Guardar en buffer con compresión
        buffer = io.BytesIO()
        img.save(buffer, format="JPEG", quality=quality, optimize=True)
        buffer.seek(0)
        return base64.b64encode(buffer.read()).decode()
    except:
        return None

# Cargar imágenes
apple_music_b64 = get_image_base64("imagenes/logos/apple_music.jpg")
spotify_b64 = get_image_base64("imagenes/logos/spotify_logo.png")

# Crear cards usando columnas
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown(f"""
        <div class="music-card">
            <div class="card-image-container">
                <img src="data:image/jpeg;base64,{apple_music_b64}" alt="Apple Music">
            </div>
            <a href="https://music.apple.com/co/playlist/harper/pl.u-KVXBkA6TLXoqzeo?l=en" target="_blank" class="card-button">
                🎵 Escuchar en Apple Music
            </a>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="music-card">
            <div class="card-image-container">
                <img src="data:image/png;base64,{spotify_b64}" alt="Spotify">
            </div>
            <a href="https://open.spotify.com/playlist/5C5F0yGMSrLe6SimZoNYui?si=Aqm5xGgDRLuTZ5OpmrfIxg&pi=7cZG02ciTnOUx" target="_blank" class="card-button">
                🎵 Escuchar en Spotify
            </a>
        </div>
    """, unsafe_allow_html=True)

# Carrusel de fotos
# Obtener todas las fotos
fotos_path = "imagenes/fotos/*.jpeg"
fotos = sorted(glob.glob(fotos_path))  # Ordenar para consistencia

# Convertir fotos a base64 (optimizadas)
fotos_b64 = []
for foto in fotos:
    foto_b64 = get_optimized_image_base64(foto, max_size=300, quality=70)
    if foto_b64:
        fotos_b64.append(foto_b64)

# Crear HTML del carrusel
if fotos_b64:
    st.markdown('<div style="margin-top: 60px;"><h2 style="text-align: center; color: #ff0000; font-family: Georgia, serif; margin-bottom: 30px;">📸 Lindas fotos, scrolear a la derecha →</h2></div>', unsafe_allow_html=True)
    
    # CSS para el slider horizontal
    st.markdown("""
        <style>
        .photo-slider {
            overflow-x: auto;
            overflow-y: hidden;
            width: 100%;
            margin: 40px 0;
            background: rgba(0, 0, 0, 0.2);
            padding: 30px 20px;
            border-radius: 15px;
            -webkit-overflow-scrolling: touch;
            scroll-behavior: smooth;
        }
        .photo-slider::-webkit-scrollbar {
            height: 12px;
        }
        .photo-slider::-webkit-scrollbar-track {
            background: rgba(0, 0, 0, 0.3);
            border-radius: 10px;
        }
        .photo-slider::-webkit-scrollbar-thumb {
            background: linear-gradient(135deg, #ff0000 0%, #cc0000 100%);
            border-radius: 10px;
        }
        .photo-slider::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(135deg, #ff3333 0%, #ff0000 100%);
        }
        .photo-track {
            display: flex;
            gap: 20px;
            padding: 10px 0;
        }
        .photo-item {
            min-width: 300px;
            height: 300px;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 8px 25px rgba(255, 0, 0, 0.4);
            transition: transform 0.3s ease;
            border: 3px solid #ff0000;
            flex-shrink: 0;
            cursor: pointer;
        }
        .photo-item:hover {
            transform: scale(1.05);
            box-shadow: 0 15px 40px rgba(255, 0, 0, 0.7);
        }
        .photo-item img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        /* Responsive para móviles */
        @media (max-width: 768px) {
            .photo-item {
                min-width: 200px;
                height: 200px;
            }
            .photo-slider {
                padding: 20px 15px;
            }
            .photo-track {
                gap: 15px;
            }
        }
        @media (max-width: 480px) {
            .photo-item {
                min-width: 150px;
                height: 150px;
            }
            .photo-track {
                gap: 10px;
            }
            .photo-slider::-webkit-scrollbar {
                height: 8px;
            }
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Crear el HTML de las fotos
    fotos_html = ""
    for foto_b64 in fotos_b64:
        fotos_html += f'<div class="photo-item"><img src="data:image/jpeg;base64,{foto_b64}" alt="Foto"></div>'
    
    slider_html = f"""
        <div class="photo-slider">
            <div class="photo-track">
                {fotos_html}
            </div>
        </div>
    """
    
    st.markdown(slider_html, unsafe_allow_html=True)

# Pie de página romántico
st.markdown('<div class="hearts">🖤</div>', unsafe_allow_html=True)
st.markdown("""
    <div style="text-align: center; color: #ff6666; margin-top: 40px; font-style: italic;">
        Con amor, sentimiento mas puro que mi corazón alberga ahora transformado en canciones 🎶
    </div>
""", unsafe_allow_html=True)

