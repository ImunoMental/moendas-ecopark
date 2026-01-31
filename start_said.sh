#!/bin/bash
echo "🚀 S.A.I.D. - Iniciando Motor de Inteligência Analítica..."

# Navega para o diretório do projeto
cd ~/demo_loteadora

# Mata processos antigos na porta 8501 para evitar erro de 'Port busy'
fuser -k 8501/tcp

# Ativa o ambiente virtual
source venv/bin/activate

# Inicia o Streamlit em modo 'Headless' para economizar recursos do Xubuntu
# O nohup permite que ele continue rodando mesmo se o terminal oscilar
nohup streamlit run app.py --server.port 8501 --server.address 0.0.0.0 --server.headless true > /dev/null 2>&1 &

echo "✅ Sistema ONLINE localmente na porta 8501"
echo "🌐 Estabelecendo túnel seguro via Ngrok..."

# Abre o Ngrok (Este comando trava o terminal para você ver o link)
ngrok http 8501
