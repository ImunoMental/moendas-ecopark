import streamlit as st
import pandas as pd
import os

# Configuração de Estética Premium
st.set_page_config(page_title="MOENDAS ECOPARK - VGV Intelligence", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #041221; color: white; }
    [data-testid="stSidebar"] { background-color: #061A2E; border-right: 2px solid #2ECC71; }
    .stButton > button {
        background-color: #2ECC71 !important;
        color: #041221 !important;
        font-weight: bold; border-radius: 8px; width: 100%; height: 3em;
    }
    .stButton > button:hover { background-color: #27AE60 !important; transform: scale(1.02); }
    h1, h2, h3 { color: white !important; text-align: center; }
    /* Card de Serviço */
    .service-card {
        background-color: #0A2239; padding: 20px; border-radius: 10px;
        border: 1px solid #2ECC71; margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Banco de Dados de Clientes (Simulado)
if 'db_clientes' not in st.session_state:
    st.session_state.db_clientes = pd.DataFrame([
        {"Nome": "Said Administrador", "CPF": "000.000.000-00", "Lote": "Q-A L-01", "Status": "Pago"},
        {"Nome": "Asclépio Consultor", "CPF": "111.222.333-44", "Lote": "Q-C L-15", "Status": "Parcelado"}
    ])

# Navegação Lateral - BOTÕES REINSERIDOS
with st.sidebar:
    st.markdown("## MOENDAS ECOPARK")
    st.markdown("---")
    if st.button("🏠 PÁGINA INICIAL"): st.session_state.page = "home"
    if st.button("📍 MAPA E VENDAS"): st.session_state.page = "mapa"
    if st.button("🔍 BUSCAR CLIENTES"): st.session_state.page = "busca"
    if st.button("🛠️ SERVIÇOS (LIMPEZA/CERCA)"): st.session_state.page = "servicos"
    if st.button("🤖 CONSULTORIA IA"): st.session_state.page = "ia"
    st.markdown("---")
    st.caption("Ecossistema v1.6 - Chapada Diamantina")

if 'page' not in st.session_state: st.session_state.page = "home"

# --- VIEW: HOME (Conceito) ---
if st.session_state.page == "home":
    st.markdown("<h1>Bem Vindo ao Paraíso da Chapada Diamantina</h1>", unsafe_allow_html=True)
    img_home = "moendas ecopark1.jpg"
    if os.path.exists(img_home):
        # Corrigido: use_column_width substituído por use_container_width
        st.image(img_home, use_container_width=True, caption="O Seu Novo Estilo de Vida Sustentável")
    else:
        st.error(f"⚠️ Imagem {img_home} não encontrada.")

# --- VIEW: MAPA E VENDAS ---
elif st.session_state.page == "mapa":
    st.markdown("<h1>Mapa Técnico e Disponibilidade</h1>", unsafe_allow_html=True)
    img_mapa = "moendas ecopark.jpg"
    if os.path.exists(img_mapa):
        st.image(img_mapa, use_container_width=True)
    
    st.write("### Reserva Rápida:")
    c1, c2 = st.columns(2)
    lote = c1.text_input("Número do Lote")
    if c2.button("GERAR PIX DE RESERVA"):
        st.success(f"Reserva para {lote} ativa!")
        st.image(f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=Moendas_{lote}")

# --- VIEW: SERVIÇOS (O Diferencial) ---
elif st.session_state.page == "servicos":
    st.markdown("<h1>Marketplace de Serviços Moendas</h1>", unsafe_allow_html=True)
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("<div class='service-card'><h3>🌿 Limpeza de Lote</h3><p>Manutenção mensal recorrente.</p><h4>R$ 180,00/mês</h4></div>", unsafe_allow_html=True)
        if st.button("CONTRATAR LIMPEZA"): st.balloons()
        
    with col_b:
        st.markdown("<div class='service-card'><h3>🚧 Cercamento</h3><p>Padrão Ecopark (Eucalipto).</p><h4>Sob Consulta</h4></div>", unsafe_allow_html=True)
        if st.button("SOLICITAR ORÇAMENTO"): st.info("Engenharia notificada!")

# --- VIEW: BUSCA E IA (Mantidos) ---
elif st.session_state.page == "busca":
    st.header("🔍 Busca de Clientes")
    busca = st.text_input("Nome, CPF ou Lote")
    if busca:
        res = st.session_state.db_clientes[st.session_state.db_clientes.apply(lambda r: r.astype(str).str.contains(busca, case=False).any(), axis=1)]
        st.dataframe(res, use_container_width=True)
    else:
        st.dataframe(st.session_state.db_clientes, use_container_width=True)

elif st.session_state.page == "ia":
    st.header("🤖 Moendas AI")
    prompt = st.chat_input("Analise meu VGV...")
    if prompt:
        with st.chat_message("assistant"):
            st.write("Análise Estratégica: O Moendas Ecopark apresenta 22% de valorização anual projetada.")
