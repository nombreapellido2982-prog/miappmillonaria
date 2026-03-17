import streamlit as st

# Configuración profesional de la página
st.set_page_config(page_title="ReputacionIA - Gestión de Reseñas", page_icon="🛡️")

# --- ESTILO PERSONALIZADO ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    </style>
    """, unsafe_allow_input_ those_tags=True)

# --- BARRA LATERAL (EL NEGOCIO) ---
st.sidebar.image("https://cdn-icons-png.flaticon.com", width=100)
st.sidebar.title("🛡️ ReputacionIA")
st.sidebar.write("Protege la imagen de tu negocio en Inca y toda España.")
st.sidebar.markdown("---")
# PEGA AQUÍ TU LINK DE STRIPE REAL
st.sidebar.link_button("🚀 Activar Plan Pro (19€/mes)", "https://buy.stripe.com")
st.sidebar.write("✅ Respuestas ilimitadas")
st.sidebar.write("✅ Optimización SEO local")

# --- CUERPO DE LA APP ---
st.title("🛡️ ReputacionIA: Asistente de Reseñas")
st.write("Convierte las quejas de tus clientes en oportunidades de fidelización en segundos.")

st.info("💡 **Consejo:** Copia la reseña negativa de Google Maps y pégala abajo.")

reseña = st.text_area("Texto de la reseña del cliente:", placeholder="Ej: Pésimo servicio, no volveré...")

if st.button("✨ Generar Respuesta Profesional"):
    if reseña:
        with st.spinner('La IA de ReputacionIA está redactando...'):
            st.markdown("---")
            st.subheader("✅ Respuesta sugerida para tu negocio:")
            # Aquí la lógica de la respuesta
            st.success(f"Estimado cliente, lamentamos que su experiencia respecto a '{reseña[:40]}...' no haya sido satisfactoria. En ReputacionIA valoramos su feedback y nos gustaría invitarle a contactarnos para solucionar cualquier inconveniente. ¡Esperamos verle pronto!")
            st.caption("⚠️ Esta es una respuesta de prueba. Suscríbete al Plan Pro para respuestas personalizadas con IA avanzada.")
    else:
        st.warning("⚠️ Por favor, introduce una reseña para analizar.")
