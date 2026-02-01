import streamlit as st
import pandas as pd
import os
import random
import google.generativeai as genai

# 1. CONFIGURAÇÃO INICIAL (DEVE SER A PRIMEIRA LINHA)
st.set_page_config(page_title="MOENDAS ECOPARK - O Paraíso da Chapada Diamantina", layout="wide")

# 2. CONFIGURAÇÃO DE ACESSO À API
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

# 3. BLINDAGEM CONTRA TRADUÇÃO AUTOMÁTICA
st.markdown("""<style>.notranslate { translate: no !important; }</style>""", unsafe_allow_html=True)

# 4. CSS PREMIUM (Design que o cliente aprovou)
st.markdown("""
    <style>
    .stApp { background-color: #041221; color: white; }
    [data-testid="stSidebar"] { background-color: #061A2E; border-right: 2px solid #2ECC71; }
    label, .stWidgetLabel p { color: #FFFFFF !important; font-size: 1.3rem !important; font-weight: 800 !important; text-shadow: 1px 1px 2px #000; }
    .stTextInput input, .stSelectbox select, .stDateInput input, .stTextArea textarea { background-color: #0A2239 !important; color: white !important; border: 2px solid #2ECC71 !important; }
    .stButton > button { background-color: #2ECC71 !important; color: #041221 !important; font-weight: bold; height: 3.5em; width: 100%; }
    .ia-response { color: #FFFFFF !important; font-size: 24px !important; font-weight: bold !important; padding: 20px; border-left: 5px solid #2ECC71; background-color: #0A2239; border-radius: 8px; }
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
    st.markdown("---")
    if perfil == "Administrador":
        if st.button("🏠 PÁGINA INICIAL"): st.session_state.page = "home"
        if st.button("🤖 CONSULTORIA IA"): st.session_state.page = "ia"
        if st.button("📍 MAPA E VENDAS"): st.session_state.page = "mapa"
        if st.button("👤 NOVO CADASTRO"): st.session_state.page = "cadastro"
        if st.button("📅 AGENDAR VISITA"): st.session_state.page = "agendamento"
        if st.button("🔍 BUSCAR CLIENTES"): st.session_state.page = "busca"
        if st.button("🛠️ SERVIÇOS"): st.session_state.page = "servicos"
        if st.button("🗺️ ROADMAP"): st.session_state.page = "roadmap"

# --- LÓGICA DE PÁGINAS ---
if st.session_state.page == "home":
    st.markdown("<h1 style='text-align:center;'>O Paraíso da Chapada Diamantina</h1>", unsafe_allow_html=True)
    if os.path.exists("moendas ecopark1.jpg"): st.image("moendas ecopark1.jpg", use_container_width=True)

elif st.session_state.page == "cadastro":
    st.header("👤 Dossiê Profissional de Investidor")
    with st.form("form_v2_completo"):
        c1, c2 = st.columns(2)
        nome = c1.text_input("NOME COMPLETO"); doc = c2.text_input("CPF ou CNPJ")
        rg = c1.text_input("RG"); nasc = c2.date_input("DATA DE NASCIMENTO")
        wa = c1.text_input("WHATSAPP"); mail = c2.text_input("E-MAIL")
        renda = st.number_input("RENDA MENSAL COMPROVADA", min_value=0.0)
        aceite = st.checkbox("CONCORDO COM OS TERMOS LGPD")
        if st.form_submit_button("FINALIZAR E GERAR CONTRATO"):
            if nome and doc and aceite: st.success(f"Dossiê de {nome} gerado!")

elif st.session_state.page == "ia":
    st.header("🤖 Consultoria Estratégica S.A.I.D.")
    st.write("S.A.I.D. System Analytical Intelligence Development")
    pergunta = st.text_input("DIGITE SUA DÚVIDA SOBRE O MOENDAS ECOPARK")
    if pergunta:
        with st.spinner("S.A.I.D. consultando base de dados da Chapada..."):
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                contexto_moendas = """Você é o IA S.A.I.D., consultor sênior do Moendas Ecopark.
                LOCALIZAÇÃO: Ituaçu (BA), Portal Sul da Chapada Diamantina, a 5 min do centro.
                PRODUTO: Lotes para chácaras a partir de 1.000m².
                LAZER (50.000m²): Piscina semiolímpica, campo de futebol, Haras, quiosques, salão de festas, academia e teatro de arena.
                NATUREZA: Próximo à Cachoeira das Moendas (72m de queda), Gruta da Mangabeira, Poço do Amor e Rio Salobra.
                INFRA: Segurança, energia, água, trilhas ecológicas, baia para cavalos e espaço pet.
                NEGOCIAÇÃO: Venda direta em até 100x sem burocracia.
                DIRETRIZ: Seja direto, honesto e analítico. Use sua psicologia sombria abordando problema e solução com base em saúde e bem estar para valorizar o projeto."""
                response = model.generate_content(f"{contexto_moendas}\n\nPergunta: {pergunta}")
                st.markdown(f"<div class='ia-response'>{response.text}</div>", unsafe_allow_html=True)
            except:
                st.error("O consultor está processando dados. Tente em instantes.")

elif st.session_state.page == "servicos":
    st.header("🛠️ Marketplace de Serviços")
    st.markdown("### Identifique o Local e a Data")
    lote_servico = st.text_input("NÚMERO DO LOTE (Ex: Q-C L-12)")
    data_servico = st.date_input("DATA PREVISTA PARA SERVIÇO", format="DD/MM/YYYY")
    st.markdown("---")
    st.markdown("<div class='service-card'><h3>🌿 Limpeza de Lote</h3><p>R$ 180,00/mês</p></div>", unsafe_allow_html=True)
    if st.button("CONTRATAR LIMPEZA"):
        if lote_servico: st.success(f"Solicitação enviada para Lote {lote_servico}!")

elif st.session_state.page == "agendamento":
    st.header("📅 Agendamento de Visita")
    st.date_input("DATA")
    if st.button("CONFIRMAR"): st.success("Visita agendada!")

elif st.session_state.page == "mapa":
    st.header("📍 Masterplan e Vendas")
    st.text_input("LOTE PARA RESERVA")
    st.button("GERAR PIX")

elif st.session_state.page == "busca":
    st.header("🔍 Central de Clientes")
    st.dataframe(st.session_state.db_clientes, use_container_width=True)

elif st.session_state.page == "roadmap":
    st.title("🗺️ Mapa Mental: Ecossistema S.A.I.D.")
    st.markdown("""
        ---
        ### 1. Dashboard Administrativo (Desktop)
        * **Controle Central:** Gestão de lotes, clientes e serviços.
        * **Inteligência S.A.I.D.:** IA treinada em dados locais de Ituaçu/BA.
        ### 2. Módulo Corretor (Mobile - App)
        * **Venda em Campo:** Cadastro de clientes e reservas via smartphone.
        ### 3. Portal do Cliente (Experiência e Bem-estar)
        * **Clima Real-Time:** Previsão meteorológica para Ituaçu e Chapada.
        * **Minutos de Magia:** Conteúdo diário de sabedoria e neurociência.
        ---
        > **Compromisso de Escalabilidade:** O S.A.I.D. é um organismo digital vivo. Toda nova infraestrutura será integrada conforme o empreendimento evoluir.
    """)
