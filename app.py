import streamlit as st
import pandas as pd
import os
import random
import google.generativeai as genai

# 1. CONFIGURAÇÃO INICIAL
st.set_page_config(page_title="MOENDAS ECOPARK - O Paraíso da Chapada Diamantina", layout="wide")

# 2. CONFIGURAÇÃO DE ACESSO À API
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

# 3. BLINDAGEM CONTRA TRADUÇÃO AUTOMÁTICA
st.markdown("""<style>.notranslate { translate: no !important; }</style>""", unsafe_allow_html=True)

# 4. CSS PREMIUM (Marca d'água e Design S.A.I.D.)
st.markdown("""
    <style>
    .stApp { background-color: #041221; color: white; }
    [data-testid="stSidebar"] { background-color: #061A2E; border-right: 2px solid #2ECC71; }
    label, .stWidgetLabel p { color: #FFFFFF !important; font-size: 1.3rem !important; font-weight: 800 !important; text-shadow: 1px 1px 2px #000; }
    .stTextInput input, .stSelectbox select, .stDateInput input, .stTextArea textarea { background-color: #0A2239 !important; color: white !important; border: 2px solid #2ECC71 !important; }
    .stButton > button { background-color: #2ECC71 !important; color: #041221 !important; font-weight: bold; height: 3.5em; width: 100%; border-radius: 5px; }
    .stApp::before {
        content: 'S.A.I.D. SYSTEM ANALYTICAL INTELLIGENCE DEVELOPMENT';
        position: fixed; bottom: 20px; right: 20px; opacity: 0.15; font-size: 1.2rem; color: white; z-index: 999; pointer-events: none; font-weight: bold; letter-spacing: 2px;
    }
    .ia-response { color: #FFFFFF !important; font-size: 20px !important; font-weight: bold !important; padding: 20px; border-left: 5px solid #2ECC71; background-color: #0A2239; border-radius: 8px; }
    .service-card { background-color: #0A2239; padding: 20px; border-radius: 10px; border: 1px solid #2ECC71; margin-bottom: 15px; }
    </style>
    """, unsafe_allow_html=True)

# 5. ESTADOS DE SESSÃO
if 'page' not in st.session_state: st.session_state.page = "home"
if 'db_clientes' not in st.session_state:
    st.session_state.db_clientes = pd.DataFrame([
        {"Nome": "Alex Dias de Souza", "CPF": "000.000.000-00", "Perfil": "Investidor"},
        {"Nome": "Said Admin", "CPF": "111.222.333-44", "Perfil": "Consultor"}
    ])

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='color: #2ECC71; text-align: center;' class='notranslate'>S.A.I.D.</h2>", unsafe_allow_html=True)
    perfil = st.selectbox("PERFIL DE ACESSO", ["Administrador", "Corretor (Mobile)", "Cliente (Portal)"])
    if perfil == "Administrador":
        if st.button("🏠 PÁGINA INICIAL"): st.session_state.page = "home"
        if st.button("🤖 CONSULTORIA IA"): st.session_state.page = "ia"
        if st.button("📍 MASTERPLAN"): st.session_state.page = "mapa"
        if st.button("👤 NOVO CADASTRO"): st.session_state.page = "cadastro"
        if st.button("📅 AGENDAMENTO"): st.session_state.page = "agendamento"
        if st.button("🔍 BUSCAR CLIENTES"): st.session_state.page = "busca"
        if st.button("🛠️ MARKETPLACE"): st.session_state.page = "servicos"
        if st.button("🗺️ ROADMAP"): st.session_state.page = "roadmap"

# --- LÓGICA DE PÁGINAS ---

if st.session_state.page == "home":
    st.markdown("<h1 style='text-align:center;'>O Paraíso da Chapada Diamantina</h1>", unsafe_allow_html=True)
    if os.path.exists("moendas ecopark1.jpg"): st.image("moendas ecopark1.jpg", use_container_width=True)

elif st.session_state.page == "cadastro":
    st.header("👤 Dossiê Profissional de Investidor")
    with st.form("form_v2_completo"):
        st.subheader("1. Identificação")
        c1, c2 = st.columns(2)
        nome = c1.text_input("NOME COMPLETO"); doc = c2.text_input("CPF ou CNPJ")
        rg = c1.text_input("RG"); nasc = c2.date_input("DATA DE NASCIMENTO")
        civil = st.selectbox("ESTADO CIVIL", ["Solteiro", "Casado", "Divorciado", "União Estável"])
        
        st.subheader("2. Contato")
        wa = c1.text_input("WHATSAPP"); mail = c2.text_input("E-MAIL")
        
        st.subheader("3. Profissional e Financeiro")
        renda = st.number_input("RENDA MENSAL COMPROVADA", min_value=0.0)
        banco = st.text_input("DADOS BANCÁRIOS")
        
        st.subheader("4. Interesse")
        tipo = st.selectbox("TIPO DE IMÓVEL", ["Terreno", "Casa", "Comercial"])
        orc = st.text_input("ORÇAMENTO DISPONÍVEL")
        
        st.subheader("5. Documentos e LGPD")
        st.file_uploader("ANEXAR RG/CPF/RENDA", accept_multiple_files=True)
        aceite = st.checkbox("CONCORDO COM OS TERMOS LGPD E CONSULTA SPC/SERASA")
        
        if st.form_submit_button("FINALIZAR E GERAR CONTRATO"):
            if nome and doc and aceite:
                st.balloons(); st.success(f"Dossiê de {nome} gerado com sucesso!")
            else:
                st.error("Preencha os campos obrigatórios e aceite os termos.")

elif st.session_state.page == "ia":
    st.header("🤖 Consultoria Estratégica S.A.I.D.")
    pergunta = st.text_input("DIGITE SUA DÚVIDA SOBRE O MOENDAS ECOPARK")
    if pergunta:
        with st.spinner("Analisando base de dados estratégica..."):
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                contexto = """Você é o IA S.A.I.D., consultor sênior do Moendas Ecopark em Ituaçu (BA). 
                Lotes 1.000m², Lazer 50.000m², Cachoeira das Moendas. Use psicologia sombria, 
                seja analítico, direto e honesto. Foco em saúde e bem-estar para valorizar o projeto."""
                response = model.generate_content(f"{contexto}\n\nPergunta: {pergunta}")
                st.markdown(f"<div class='ia-response'>{response.text}</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error("O consultor está processando um alto volume. Tente em instantes.")

elif st.session_state.page == "servicos":
    st.header("🛠️ Marketplace de Serviços")
    ls = st.text_input("NÚMERO DO LOTE"); ds = st.date_input("DATA PREVISTA")
    st.markdown("<div class='service-card'><h3>🌿 Limpeza de Lote</h3><p>R$ 180,00/mês</p></div>", unsafe_allow_html=True)
    if st.button("CONTRATAR LIMPEZA"): st.success(f"Limpeza agendada para Lote {ls}!")
    st.markdown("<div class='service-card'><h3>🚧 Cercamento Profissional</h3><p>Sob Consulta</p></div>", unsafe_allow_html=True)
    if st.button("SOLICITAR ORÇAMENTO CERCAMENTO"): st.info(f"Pedido enviado para Lote {ls}!")

elif st.session_state.page == "agendamento":
    st.header("📅 Agendamento de Visita")
    with st.form("f_ag"):
        nv = st.text_input("NOME"); dv = st.date_input("DIA")
        tv = st.selectbox("TURNO", ["Manhã (08h-12h)", "Tarde (13h-17h)"])
        if st.form_submit_button("CONFIRMAR"): st.success(f"Agendado para {dv}!")

elif st.session_state.page == "mapa":
    st.header("📍 Masterplan e Vendas")
    if os.path.exists("moendas ecopark.jpg"): st.image("moendas ecopark.jpg", use_container_width=True)
    l_reser = st.text_input("PESQUISAR LOTE"); st.button("RESERVAR E GERAR PIX")

elif st.session_state.page == "busca":
    st.header("🔍 Central de Clientes"); st.dataframe(st.session_state.db_clientes, use_container_width=True)

elif st.session_state.page == "roadmap":
    st.title("🗺️ Mapa Mental S.A.I.D."); st.markdown("""
        ### 1. Dashboard Admin | 2. Módulo Corretor | 3. Portal Cliente
        > O S.A.I.D. é um organismo digital vivo.
    """)
# Build: dom 01 fev 2026 06:51:15 -03
