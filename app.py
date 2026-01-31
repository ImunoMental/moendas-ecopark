import streamlit as st
import pandas as pd
import os
import random
from google import genai  # Nova biblioteca 2026

# CONFIGURAÇÃO S.A.I.D. 2026
# Inicialização S.A.I.D. de Próxima Geração
client = genai.Client(api_key="AIzaSyCXT46T5oL3zjxPkJTs0x6hjpFLIEIRGto")
# Configuração de Estética Premium e Blindagem
st.set_page_config(page_title="MOENDAS ECOPARK - O Paraíso da Chapada Diamantina", layout="wide")
# Configuração de Estética Premium e Blindagem
st.set_page_config(page_title="MOENDAS ECOPARK - O Paraíso da Chapada Diamantina", layout="wide")

# CSS BLINDADO: Legibilidade, Marca d'água e Design Premium
st.markdown("""
    <style>
    /* Configuração Geral */
    .stApp { background-color: #041221; color: white; }
    [data-testid="stSidebar"] { background-color: #061A2E; border-right: 2px solid #2ECC71; }
    
    /* Legendas e Textos Brancos */
    label, .stWidgetLabel p, [data-testid="stWidgetLabel"] {
        color: #FFFFFF !important;
        font-size: 1.3rem !important;
        font-weight: 800 !important;
        text-shadow: 1px 1px 2px #000;
    }
    
    /* Inputs Estilizados */
    .stTextInput input, .stSelectbox select, .stDateInput input, .stTextArea textarea {
        background-color: #0A2239 !important;
        color: white !important;
        border: 2px solid #2ECC71 !important;
    }

    /* Botões Premium */
    .stButton > button {
        background-color: #2ECC71 !important;
        color: #041221 !important;
        font-weight: bold;
        height: 3.5em;
    }

    /* Marca d'água SAID */
    .stApp::before {
        content: 'S.A.I.D. SYSTEM ANALYTICAL INTELLIGENCE DEVELOPMENT';
        position: fixed;
        bottom: 20px;
        right: 20px;
        opacity: 0.15;
        font-size: 1.2rem;
        color: white;
        z-index: 999;
        pointer-events: none;
        font-weight: bold;
        letter-spacing: 2px;
    }

    /* Resposta da IA */
    .ia-response {
        color: #FFFFFF !important; font-size: 24px !important; font-weight: bold !important;
        padding: 20px; border-left: 5px solid #2ECC71; background-color: #0A2239; border-radius: 8px;
    }

    /* Cards de Serviço */
    .service-card {
        background-color: #0A2239; padding: 20px; border-radius: 10px;
        border: 1px solid #2ECC71; margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# Estados de Sessão
if 'page' not in st.session_state: st.session_state.page = "home"
if 'db_clientes' not in st.session_state:
    st.session_state.db_clientes = pd.DataFrame([
        {"Nome": "Alex Dias de Souza", "CPF": "000.000.000-00", "Perfil": "Investidor"},
        {"Nome": "Said Admin", "CPF": "111.222.333-44", "Perfil": "Consultor"}
    ])

# --- SIDEBAR E SISTEMA DE ACESSO S.A.I.D. ---
with st.sidebar:
    st.markdown(f"""
        <div style='text-align: center;'>
            <h2 style='color: #2ECC71;'>S.A.I.D.</h2>
            <small>Analytical Intelligence Development</small><br>
            <strong>MOENDAS ECOPARK</strong>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")

    # Simulador de Nível de Acesso (Diferencial Competitivo)
    perfil = st.selectbox(
        "PERFIL DE ACESSO",
        ["Administrador", "Corretor (Mobile)", "Cliente (Portal)"],
        help="Selecione o nível de acesso para visualizar as funcionalidades futuras."
    )

    st.markdown("---")

    if perfil == "Administrador":
        st.markdown("### MENU ADMIN")
        if st.button("🏠 PÁGINA INICIAL"): st.session_state.page = "home"
        if st.button("🤖 CONSULTORIA IA"): st.session_state.page = "ia"
        if st.button("📍 MAPA E VENDAS"): st.session_state.page = "mapa"
        if st.button("👤 NOVO CADASTRO"): st.session_state.page = "cadastro"
        if st.button("📅 AGENDAR VISITA"): st.session_state.page = "agendamento"
        if st.button("🔍 BUSCAR CLIENTES"): st.session_state.page = "busca"
        if st.button("🛠️ SERVIÇOS"): st.session_state.page = "servicos"
        if st.button("🗺️ MAPA MENTAL SISTEMA"): st.session_state.page = "roadmap"

    elif perfil == "Corretor (Mobile)":
        st.warning("Módulo Mobile em desenvolvimento.")
        st.info("Acesso exclusivo para corretores credenciados realizarem vendas em campo via App.")
        if st.button("⬅️ VOLTAR AO ADMIN"): st.session_state.page = "home"

    elif perfil == "Cliente (Portal)":
        st.info("Portal do Morador em desenvolvimento.")
        st.markdown("* Previsão do Tempo (Ituaçu)\n* Minutos de Magia\n* Suporte Financeiro")
        if st.button("⬅️ VOLTAR AO ADMIN"): st.session_state.page = "home"

    st.markdown("---")
    st.success(f"🔥 {random.randint(5, 15)} investidores analisando o Moendas.")

# --- LÓGICA DE PÁGINAS ---

if st.session_state.page == "home":
    st.markdown("<h1 style='text-align:center;'>O Paraíso da Chapada Diamantina</h1>", unsafe_allow_html=True)
    if os.path.exists("moendas ecopark1.jpg"):
        st.image("moendas ecopark1.jpg", use_container_width=True)
    if st.button("📅 AGENDE UMA VISITA AQUI"):
        st.session_state.page = "agendamento"
        st.rerun()

elif st.session_state.page == "cadastro":
    st.header("👤 Dossiê Profissional de Investidor")
    with st.form("form_v2_completo"):
        st.subheader("1. Identificação")
        c1, c2 = st.columns(2)
        nome = c1.text_input("NOME COMPLETO")
        doc = c2.text_input("CPF ou CNPJ")
        rg = c1.text_input("RG")
        nasc = c2.date_input("DATA DE NASCIMENTO")
        civil = st.selectbox("ESTADO CIVIL", ["Solteiro", "Casado", "Divorciado", "União Estável"])

        st.subheader("2. Contato")
        c3, c4 = st.columns(2)
        wa = c3.text_input("WHATSAPP")
        mail = c4.text_input("E-MAIL")

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
                st.balloons()
                st.success(f"Dossiê de {nome} gerado com sucesso!")
                txt_contrato = f"CONTRATO MOENDAS ECOPARK\n\nTitular: {nome}\nCPF: {doc}\nPerfil: {tipo}\nData: {nasc}\n\nDocumento homologado."
                st.download_button("📄 BAIXAR CONTRATO EM PDF (TXT)", txt_contrato, f"Contrato_{nome}.txt", "text/plain")
            else:
                st.error("Preencha Nome, CPF e aceite os termos.")

elif st.session_state.page == "agendamento":
    st.header("📅 Agendamento de Visita Presencial")
    with st.form("ag_form"):
        nv = st.text_input("NOME DO INTERESSADO")
        dv = st.date_input("DIA DA VISITA")
        tv = st.selectbox("TURNO", ["Manhã (08h-12h)", "Tarde (13h-17h)"])
        if st.form_submit_button("CONFIRMAR AGENDAMENTO"):
            st.success(f"Visita agendada para {dv} no turno da {tv}!")

elif st.session_state.page == "mapa":
    st.header("📍 Masterplan e Vendas")
    if os.path.exists("moendas ecopark.jpg"):
        st.image("moendas ecopark.jpg", use_container_width=True)
    lote = st.text_input("LOTE PARA RESERVA (NÚMERO LOTE)")
    if st.button("GERAR PIX"):
        st.image(f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=Reserva_{lote}")

elif st.session_state.page == "busca":
    st.header("🔍 Central de Clientes")
    st.dataframe(st.session_state.db_clientes, use_container_width=True)

elif st.session_state.page == "ia":
        st.header("🤖 Consultoria Estratégica S.A.I.D.")
        st.write("S.A.I.D. System Analytical Intelligence Development")
        
        pergunta = st.text_input("DIGITE SUA DÚVIDA SOBRE O MOENDAS ECOPARK")
        
        if pergunta:
            with st.spinner("S.A.I.D. consultando base de dados da Chapada..."):
                try:
                    # CONTEXTO ESTRATÉGICO INJETADO
                    contexto_moendas = """
                    Você é o IA S.A.I.D., consultor sênior do Moendas Ecopark.
                    LOCALIZAÇÃO: Ituaçu (BA), Portal Sul da Chapada Diamantina, a 5 min do centro.
                    PRODUTO: Lotes para chácaras a partir de 1.000m².
                    LAZER (50.000m²): Piscina semiolímpica, campo de futebol, Haras,  quiosques, salão de festas, academia e teatro de arena.
                    NATUREZA: Próximo à Cachoeira das Moendas (72m de queda), Gruta da Mangabeira, Poço do Amor e Rio Salobra.
                    INFRA: Segurança, energia, água, trilhas ecológicas, baia para cavalos e espaço pet.
                    NEGOCIAÇÃO: Venda direta em até 100x sem burocracia.
                    DIRETRIZ: Seja direto, honesto e analítico. Use sua psicologia sombria abordando problema e solução com base em saúde e bem estar para valorizar o projeto.
                    """
                    
                    response = client.models.generate_content(
                        model="gemini-3-flash-preview", 
                        contents=f"{contexto_moendas}\n\nPergunta do cliente: {pergunta}"
                    )
                    
                    if response.text:
                        st.markdown(f"""
                            <div class='ia-response'>
                                <small style='color: #2ECC71;'>S.A.I.D. Intelligence - Base Ituaçu Ativa</small><br><br>
                                {response.text}
                            </div>
                        """, unsafe_allow_html=True)
                except Exception as e:
               
                    st.error("O consultor S.A.I.D. está processando um alto volume de dados. Por favor, repita sua dúvida em instantes.")

elif st.session_state.page == "servicos":
    st.header("🛠️ Marketplace de Serviços")
    st.markdown("### Identifique o Local e a Data")
    lote_servico = st.text_input("NÚMERO DO LOTE (Ex: Q-C L-12)")
    data_servico = st.date_input("DATA PREVISTA PARA SERVIÇO", format="DD/MM/YYYY")
    st.markdown("---")
    
    st.markdown("<div class='service-card'><h3>🌿 Limpeza de Lote</h3><p>R$ 180,00/mês</p></div>", unsafe_allow_html=True)
    if st.button("CONTRATAR LIMPEZA"):
        if lote_servico:
            st.success(f"Solicitação de limpeza para o Lote {lote_servico} agendada para {data_servico.strftime('%d/%m/%Y')}!")
        else:
            st.error("Por favor, informe o número do lote acima.")

    st.markdown("---")
    st.markdown("<div class='service-card'><h3>🚧 Cercamento</h3><p>Sob Consulta</p></div>", unsafe_allow_html=True)
    if st.button("SOLICITAR ORÇAMENTO"):
        if lote_servico:
            st.info(f"Pedido de orçamento de cercamento enviado para o Lote {lote_servico}. Data pretendida: {data_servico.strftime('%d/%m/%Y')}.")
        else:
            st.error("Por favor, informe o número do lote acima.")

elif st.session_state.page == "roadmap":
        st.title("🗺️ Mapa Mental: Ecossistema S.A.I.D.")
        st.write("Visão Geral de Funcionalidades e Expansão")
        
        st.markdown("""
        ---
        ### 1. Dashboard Administrativo (Desktop)
        * **Controle Central:** Gestão de lotes, clientes e serviços.
        * **Inteligência S.A.I.D.:** IA baseada em Gemini 3 treinada em dados locais de Ituaçu/BA.
        
        ### 2. Módulo Corretor (Mobile - App)
        * **Venda em Campo:** Cadastro de clientes e reservas de lotes via smartphone.
        * **Login Administrativo:** Ferramentas específicas para fechamento de contrato.
        
        ### 3. Portal do Cliente (Experiência e Bem-estar)
        * **Clima Real-Time:** Previsão meteorológica para Ituaçu e Chapada Diamantina.
        * **Minutos de Magia:** Conteúdo diário de sabedoria e neurociência para fidelização do morador.
        
        ---
        > **Compromisso de Escalabilidade:** O S.A.I.D. é um organismo digital vivo. Toda nova infraestrutura do Moendas Ecopark será integrada conforme o empreendimento evoluir.
        """)
