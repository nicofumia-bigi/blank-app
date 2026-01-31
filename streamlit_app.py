import streamlit as st
import time

# --- CONFIGURACIÓN DE PÁGINA (ESTILO SAAS) ---
st.set_page_config(
    page_title="Calculadora de Margen | Nico Fumia",
    page_icon="💸",
    layout="centered"
)

# Ocultar elementos propios de Streamlit para look profesional
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stButton>button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
        padding: 0.5rem;
        border-radius: 10px;
    }
    .big-font {
        font-size:20px !important;
        color: #31333F;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ENCABEZADO ---
st.markdown("🍽️ **NICOLÁS FUMÍA** Consultoría Gastronómica")
st.title("💸 Fuga de Capital")
st.markdown("### ¿Cuánto te cuesta realmente tu 'socio' de Delivery?")
st.write("Esta herramienta calcula el dinero exacto que cedes a las Apps y proyecta cuánto podrías recuperar gestionando tu propio territorio.")
st.divider()

# --- INPUTS (DATOS DEL USUARIO) ---
col1, col2 = st.columns(2)

with col1:
    ventas = st.number_input("Facturación Mensual en Apps ($)", 
                             min_value=0, 
                             value=300000, 
                             step=10000,
                             help="Lo que vendes bruto a través de PedidosYa/Rappi")

with col2:
    comision = st.slider("Tu Comisión Promedio (%)", 
                         min_value=10, 
                         max_value=40, 
                         value=27,
                         help="El % que te cobra la app por pedido + logística")

# --- BOTÓN DE ACCIÓN ---
st.write("") # Espacio
if st.button('CALCULAR MI PÉRDIDA 🚀'):
    
    # Simulación de "Procesando..." para efecto visual
    with st.spinner('Analizando tus márgenes...'):
        time.sleep(1.5)
    
    # Cálculos
    perdida_mensual = ventas * (comision / 100)
    perdida_anual = perdida_mensual * 12
    # Hipótesis: Con estrategia propia recuperas el 35% de esa fuga (margen que ya no pagas)
    recupero_potencial = perdida_anual * 0.35 

    # --- RESULTADOS ---
    st.success("Cálculo completado")
    
    st.markdown("#### 📉 Estás cediendo:")
    m1, m2 = st.columns(2)
    m1.metric("Por Mes", f"${perdida_mensual:,.0f}")
    m2.metric("Al Año (Proyección)", f"${perdida_anual:,.0f}", delta="- Dinero perdido", delta_color="inverse")
    
    st.warning(f"⚠️ **Atención:** Esos ${perdida_anual:,.0f} anuales equivalen a **{int(perdida_anual/40000)} sueldos mínimos** que pagas a la App y no a tu equipo.")

    st.divider()
    
    # --- LA PROPUESTA DE VALOR (HOOK) ---
    st.markdown("### 🛡️ Recupera tu Territorio")
    st.markdown(f"""
    Si aplicaras la estrategia **'Caballo de Troya'** (convertir clientes de App a Directos), 
    podrías inyectar **${recupero_potencial:,.0f} extra** de ganancia limpia a tu bolsillo este año.
    """)
    
    with st.expander("📥 Recibir la Estrategia Paso a Paso (Gratis)"):
        with st.form("lead_capture"):
            st.write("Te envío el PDF con el método para bajar esa comisión.")
            email = st.text_input("Tu Email", placeholder="tucorreo@restaurante.com")
            submitted = st.form_submit_button("Enviar Guía Ahora")
            if submitted and email:
                st.balloons()
                st.success(f"¡Listo! Enviado a {email}. Revisa tu bandeja en 2 minutos.")
                # Aquí es donde más adelante conectaremos con Google Sheets para guardar el mail
