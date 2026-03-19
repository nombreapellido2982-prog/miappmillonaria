import streamlit as st
import openai

# 1. Configuración del "cerebro" (Llave de seguridad)
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# 2. Diseño de la página
st.set_page_config(page_title="ReputacionIA - Gestión de Reseñas", page_icon="🤖")

st.title("🤖 ReputacionIA: Asistente de Reseñas")
st.write("Responde a tus reseñas con inteligencia artificial de forma profesional.")

# 3. BARRA LATERAL CON EL PAGO REAL (19€)
st.sidebar.title("🚀 Plan Profesional")
st.sidebar.link_button("🔥 Activar Plan Pro (19€/mes)", "https://buy.stripe.com")
st.sidebar.divider()
st.sidebar.write("✅ Respuestas Inteligentes Reales")
st.sidebar.write("✅ Soporte 24/7")

# 4. CUADRO PARA PEGAR LA RESEÑA
resena_cliente = st.text_area("Pega aquí la reseña de tu cliente:", placeholder="Ejemplo: El hotel estaba muy limpio pero el parking era pequeño...")

if st.button("Generar Respuesta Profesional"):
    if resena_cliente:
        st.info("La IA está analizando la reseña...")
        # Aquí la IA crea la respuesta de verdad
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un experto en reputación hotelera. Responde de forma amable y profesional."},
                {"role": "user", "content": resena_cliente}
            ]
        )
        st.success(response.choices.message.content)
    else:
        st.warning("Por favor, pega una reseña para poder ayudarte.")
