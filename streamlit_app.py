import streamlit as st

st.set_page_config(page_title="Asistente de Reseñas IA", page_icon="🚀")

st.title("🚀 Generador de Respuestas Inteligentes")
st.subheader("Convierte quejas en clientes fieles gratis")

reseña = st.text_area("Pega aquí la reseña de tu cliente:")

if st.button("Generar Respuesta Profesional"):
    if reseña:
        st.info("💡 Respuesta sugerida para tu negocio:")
        st.write(f"Estimado cliente, gracias por su comentario. Valoramos mucho su feedback sobre: '{reseña[:50]}...'. Estamos trabajando para que su próxima visita sea excelente.")
        st.success("✅ ¡Copia esta respuesta y pégala en Google Maps!")
    else:
        st.warning("⚠️ Por favor, pega una reseña primero.")

st.sidebar.markdown("---")
st.sidebar.write("💰 **Plan Millonario:** Ofrece este servicio a 10 negocios locales por $20/mes.")
