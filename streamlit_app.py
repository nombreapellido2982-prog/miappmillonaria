import streamlit as st

# 1. Configuración profesional de la página
st.set_page_config(page_title="ReputacionIA - Gestión de Reseñas", page_icon="🤖")

# 2. Estilo personalizado (Fondo y Botones)
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    </style>
    """, unsafe_allow_html=True)

# 3. Barra Lateral (Sidebar) con el Pago Real
st.sidebar.title("🚀 Plan Profesional")
st.sidebar.write("Obtén acceso ilimitado a la IA para responder a tus clientes.")

# ESTE ES TU ENLACE REAL DE STRIPE (19€)
st.sidebar.link_button("🔥 Activar Plan Pro (19€/mes)", "https://buy.stripe.com")

st.sidebar.divider()
st.sidebar.write("✅ Respuestas ilimitadas")
st.sidebar.write("✅ Optimización SEO local")
st.sidebar.write("✅ Soporte 24/7")

# 4. Cuerpo de la APP
st.title("🤖 ReputacionIA: Asistente de Reseñas")
st.write("Convierte las quejas de tus clientes en oportunidades de fidelización en segundos.")

# Cuadro para pegar la reseña
resena_cliente = st.text_area("Pega aquí la reseña de tu cliente:", placeholder="Ejemplo: La comida estaba fría y el servicio fue lento...")

if st.button("Generar Respuesta Profesional"):
    if resena_cliente:
        st.info("Generando respuesta con Inteligencia Artificial...")
        # Aquí iría la lógica de la IA, por ahora mostramos un ejemplo
        st.success("**Respuesta sugerida:** ¡Hola! Lamentamos mucho tu experiencia. Estamos trabajando para mejorar y nos encantaría invitarte de nuevo para compensarte. ¡Un saludo!")
    else:
        st.warning("Por favor, pega una reseña para poder ayudarte.")
