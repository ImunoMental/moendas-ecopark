# =====================================================
# S.A.I.D. — SYSTEM ANALYTICAL INTELLIGENCE DEVELOPMENT
# MOENDAS ECOPARK | DEMO EXECUTIVA
# =====================================================

import streamlit as st
import pandas as pd
import os
import random
from datetime import date

# =====================================================
# CONFIGURAÇÃO DA PÁGINA
# =====================================================
st.set_page_config(
    page_title="MOENDAS ECOPARK - O Paraíso da Chapada Diamantina",
    layout="wide"
)

# =====================================================
# CSS + BLINDAGEM DE TRADUÇÃO + MARCA D'ÁGUA
# =====================================================
st.markdown("""
<style>
.notranslate { translate: no !important; }

.stApp { background-color: #041221; color: white; }

[data-testid="stSidebar"] {
    background-color: #061A2E;
    border-right: 2px solid #2ECC71;
}

label, .stWidgetLabel p, h1, h2, h3, h4 {
    color: #FFFFFF !important;
    font-weight: 700;
}

.stTextInput input,
.stSelectbox select,
.stDateInput input,
.stTextArea textarea {
    background-color: #0A2239 !important;
    color: white !important;
    border: 2px solid #2ECC71 !important;
}

.stButton > button {
    background-color: #2ECC71 !important;
    color: #041221 !important;
    font-weight: bold;
    height: 3.2em;
}

.ia-response {
    background-color: #0A2239;
    border-left: 5px solid #2ECC71;
    padding: 20px;
    border-radius: 8px;
    font-size: 1.1rem;
}

.service-card {
    background-color: #0A2239;
    padding: 20px;
    border-radius: 10px;
    border: 1px solid #2ECC71;
    margin-bottom: 15px;
}

.stApp::before {
    content: "S.A.I.D. • SYSTEM ANALYTICAL INTELLIGENCE DEVELOPMENT";
    position: fixed;
    bottom: 20px;
    right: 20px;
    opacity: 0.15;
    font-size: 0.9rem;
    color: white;
    z-index: 9999;
    pointer-events: none;
    letter-spacing: 2px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# ESTADO INICIAL
# =====================================================
if "page" not in st.session_state:
    st.session_state.page = "home"

if "db_clientes" not in st.session_state:
    st.session_state.db_clientes = pd.DataFrame([
        {"Nome": "Alex Dias de Souza", "CPF": "000.000.000-00", "Perfil": "Investidor"},
        {"Nome": "S.A.I.D. Admin", "CPF": "111.222.333-44", "Perfil": "Consultor"}
    ])

# =====================================================
# SIDEBAR — PERFIL DE ACESSO
# =====================================================
with st.sidebar:
    st.markdown("""
    <div style='text-align:center' class='notranslate'>
        <h2 style='color:#2ECC71;margin-bottom:0;'>S.A.I.D.</h2>
        <p style='font-size:0.8em;color:#7f8c8d;margin-top:0;'>
            Analytical Intelligence Development
        </p>
        <strong>MOENDAS ECOPARK</strong>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    perfil = st.selectbox(
        "PERFIL DE ACESSO",
        ["Administrador", "Corretor (Mobile)", "Cliente (Portal)"]
    )

    st.markdown("---")

    if perfil == "Administrador":
        if st.button("🏠 Página Inicial"):
            st.session_state.page = "home"
        if st.button("🤖 Consultoria IA"):
            st.session_state.page = "ia"
        if st.button("📅 Agendar Visita"):
            st.session_state.page = "agendamento"
        if st.button("👤 Novo Cadastro"):
            st.session_state.page = "cadastro"
        if st.button("🔍 Buscar Clientes"):
            st.session_state.page = "busca"
        if st.button("🛠️ Serviços"):
            st.session_state.page = "servicos"
        if st.button("🗺️ Roadmap"):
            st.session_state.page = "roadmap"

    elif perfil == "Corretor (Mobile)":
        st.info("Módulo Mobile em desenvolvimento.")

    else:
        st.info("Portal do Cliente em desenvolvimento.")

    st.markdown("---")
    st.success(f"🔥 {random.randint(5,15)} investidores online")

# =====================================================
# PÁGINAS
# =====================================================
def page_home():
    st.markdown("<h1 style='text-align:center;'>O Paraíso da Chapada Diamantina</h1>", unsafe_allow_html=True)
    if os.path.exists("moendas ecopark1.jpg"):
        st.image("moendas ecopark1.jpg", use_container_width=True)

def page_agendamento():
    st.header("📅 Agendamento de Visita Presencial")

    with st.form("agendamento_form"):
        nome = st.text_input("NOME DO INTERESSADO")
        data = st.date_input("DATA DA VISITA")
        turno = st.selectbox(
            "TURNO",
            ["Manhã (08h–12h)", "Tarde (13h–17h)"]
        )

        confirmar = st.form_submit_button("CONFIRMAR AGENDAMENTO")

    if confirmar:
        if nome:
            st.success(
                f"Visita agendada para {data.strftime('%d/%m/%Y')} "
                f"no turno da {turno}."
            )
        else:
            st.error("Informe o nome do interessado.")

def page_cadastro():
    st.header("👤 Dossiê Profissional de Investidor")

    with st.form("form_v2_completo"):
        # 1. Identificação
        st.subheader("1. Identificação")
        c1, c2 = st.columns(2)
        nome = c1.text_input("NOME COMPLETO")
        doc = c2.text_input("CPF ou CNPJ")
        rg = c1.text_input("RG")
        nasc = c2.date_input("DATA DE NASCIMENTO")
        civil = st.selectbox(
            "ESTADO CIVIL",
            ["Solteiro", "Casado", "Divorciado", "União Estável"]
        )

        # 2. Contato
        st.subheader("2. Contato")
        c3, c4 = st.columns(2)
        wa = c3.text_input("WHATSAPP")
        mail = c4.text_input("E-MAIL")

        # 3. Profissional e Financeiro
        st.subheader("3. Profissional e Financeiro")
        renda = st.number_input(
            "RENDA MENSAL COMPROVADA",
            min_value=0.0,
            step=100.0
        )
        banco = st.text_input("DADOS BANCÁRIOS")

        # 4. Interesse
        st.subheader("4. Interesse")
        tipo = st.selectbox(
            "TIPO DE IMÓVEL",
            ["Terreno", "Casa", "Comercial"]
        )
        orc = st.text_input("ORÇAMENTO DISPONÍVEL")

        # 5. Documentos e LGPD
        st.subheader("5. Documentos e LGPD")
        st.file_uploader(
            "ANEXAR RG / CPF / COMPROVANTE DE RENDA",
            accept_multiple_files=True
        )
        aceite = st.checkbox(
            "CONCORDO COM OS TERMOS LGPD E CONSULTA SPC/SERASA"
        )

        submitted = st.form_submit_button(
            "FINALIZAR E GERAR CONTRATO"
        )

    # ===== PROCESSAMENTO (FORA DO FORM) =====
    if submitted:
        if nome and doc and aceite:
            st.balloons()
            st.success(f"Dossiê de {nome} gerado com sucesso!")

            # Salva no banco de clientes (demo)
            novo_cliente = {
                "Nome": nome,
                "CPF": doc,
                "Perfil": tipo
            }

            st.session_state.db_clientes = pd.concat(
                [st.session_state.db_clientes, pd.DataFrame([novo_cliente])],
                ignore_index=True
            )

            # Geração de contrato (demo)
            txt_contrato = f"""
CONTRATO MOENDAS ECOPARK

Titular: {nome}
Documento: {doc}
RG: {rg}
Data de Nascimento: {nasc}
Estado Civil: {civil}

Perfil de Interesse: {tipo}
Orçamento: {orc}
Renda Declarada: R$ {renda:,.2f}

Documento homologado para fins de demonstração.
            """

            st.download_button(
                "📄 BAIXAR CONTRATO (TXT)",
                txt_contrato,
                file_name=f"Contrato_{nome}.txt",
                mime="text/plain"
            )
        else:
            st.error(
                "Preencha Nome, CPF/CNPJ e aceite os termos LGPD."
            )

def page_servicos():
    st.header("🛠️ Marketplace de Serviços")
    st.markdown("Serviços exclusivos para proprietários do Moendas Ecopark.")

    c1, c2 = st.columns(2)
    lote = c1.text_input("NÚMERO DO LOTE")
    data = c2.date_input("DATA PREVISTA")

    st.markdown("---")

    st.markdown("""
    <div class='service-card'>
        <h3>🌿 Limpeza de Lote</h3>
        <p>Manutenção periódica do terreno.</p>
        <strong>R$ 180,00 / mês</strong>
    </div>
    """, unsafe_allow_html=True)

    if st.button("CONTRATAR LIMPEZA", key="limpeza"):
        if lote:
            st.success(f"Limpeza registrada para o lote {lote}.")
        else:
            st.error("Informe o lote.")

    st.markdown("---")

    st.markdown("""
    <div class='service-card'>
        <h3>🚧 Cercamento</h3>
        <p>Valor sob consulta.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("SOLICITAR ORÇAMENTO", key="cerca"):
        if lote:
            st.info(f"Orçamento solicitado para o lote {lote}.")
        else:
            st.error("Informe o lote.")

def page_busca():
    st.header("🔍 Central de Clientes")

    busca = st.text_input("Buscar por nome ou CPF")

    df = st.session_state.db_clientes

    if busca:
        df = df[
            df["Nome"].str.contains(busca, case=False, na=False) |
            df["CPF"].str.contains(busca, case=False, na=False)
        ]

    st.dataframe(df, use_container_width=True)

def page_ia():
    st.header("🤖 Consultoria Estratégica S.A.I.D.")
    pergunta = st.text_input("Digite sua dúvida sobre o Moendas Ecopark")

    if pergunta:
        st.markdown("""
        <div class='ia-response'>
        O módulo de Inteligência Estratégica do S.A.I.D. está em fase final de ativação
        para uso público. Toda a lógica e arquitetura já estão consolidadas.
        </div>
        """, unsafe_allow_html=True)

def page_roadmap():
    st.header("🗺️ Roadmap do Sistema S.A.I.D.")
    st.markdown("""
    • Dashboard Administrativo  
    • App do Corretor  
    • Portal do Cliente  
    • Integrações Financeiras  
    """)

# =====================================================
# ROTEADOR FINAL (NÃO MEXER)
# =====================================================
if st.session_state.page == "home":
    page_home()

elif st.session_state.page == "ia":
    page_ia()

elif st.session_state.page == "agendamento":
    page_agendamento()

elif st.session_state.page == "cadastro":
    page_cadastro()

elif st.session_state.page == "busca":
    page_busca()

elif st.session_state.page == "servicos":
    page_servicos()

elif st.session_state.page == "roadmap":
    page_roadmap()
