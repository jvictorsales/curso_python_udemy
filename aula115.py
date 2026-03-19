"""
Ambientes virtuais em Python (venv)

Um ambiente virtual é uma forma de criar uma instalação isolada do Python
dentro de uma pasta do projeto. Isso permite que cada projeto tenha suas
próprias dependências, evitando conflitos entre versões de bibliotecas e
mantendo o ambiente global do sistema limpo.

-------------------------------------------------------------------------------
📌 Conceito

Ao criar um ambiente virtual, o Python cria uma estrutura de diretórios que
contém:
- Um interpretador Python isolado
- O gerenciador de pacotes (pip)
- Um espaço próprio para instalação de bibliotecas

Quando o ambiente é ativado, o terminal passa a utilizar esse Python isolado
em vez do Python global do sistema.

-------------------------------------------------------------------------------
📁 Nomes comuns para ambientes virtuais

Você pode usar qualquer nome, mas os mais comuns são:
- venv
- env
- .venv
- .env

-------------------------------------------------------------------------------
⚙️ Criação do ambiente virtual

    python -m venv venv

-------------------------------------------------------------------------------
▶️ Ativação do ambiente virtual

Windows (PowerShell):
    .\venv\Scripts\activate

Linux / macOS:
    .venv/bin/activate
    ou
    source venv/bin/activate

-------------------------------------------------------------------------------
⛔ Desativação do ambiente virtual

    deactivate

-------------------------------------------------------------------------------
🔍 Verificar qual Python está em uso

Windows (PowerShell):
    gcm python
    gcm python -Syntax

Linux / macOS:
    which python

-------------------------------------------------------------------------------
📦 Gerenciamento de pacotes (pip)

Repositório oficial:
    https://pypi.org/

Atualizar o pip:
    python -m pip install --upgrade pip

Instalar pacotes:
    python -m pip install pymysql
    pip install pymysql

Desinstalar pacotes:
    pip uninstall pymysql
    pip uninstall pymysql -y

Listar pacotes instalados:
    pip freeze

Ver versões disponíveis:
    pip index versions pymysql

Instalar versão específica:
    pip install pymysql==1.0.1

Atualizar pacote:
    pip install pymysql --upgrade

-------------------------------------------------------------------------------
📄 Gerenciamento de dependências

Salvar dependências do projeto:
    pip freeze > requirements.txt

Instalar dependências a partir de um arquivo:
    pip install -r requirements.txt

-------------------------------------------------------------------------------
🧠 Como funciona internamente

Ao ativar o ambiente virtual, o sistema altera a variável de ambiente PATH,
fazendo com que os comandos `python` e `pip` apontem para os executáveis
dentro do ambiente virtual, e não para a instalação global.

Antes de ativar:
    python → Python global
    pip    → instala globalmente

Depois de ativar:
    python → Python do ambiente virtual
    pip    → instala dentro do ambiente virtual

-------------------------------------------------------------------------------
🧪 Estrutura básica de um ambiente virtual

    venv/
    │
    ├── Scripts/ (Windows) ou bin/ (Linux/macOS)
    │   └── executáveis (python, pip)
    ├── Lib/
    │   └── bibliotecas instaladas
    └── pyvenv.cfg
        └── configurações do ambiente

-------------------------------------------------------------------------------
🚨 Problema que o venv resolve

Sem ambiente virtual:
    Projetos diferentes podem exigir versões diferentes da mesma biblioteca,
    causando conflitos no ambiente global.

Com ambiente virtual:
    Cada projeto possui seu próprio conjunto de dependências isoladas.

Exemplo:
    Projeto A → pymysql==1.0.1
    Projeto B → pymysql==2.0.0

-------------------------------------------------------------------------------
🧠 Regra de ouro

Sempre ative o ambiente virtual antes de instalar qualquer pacote.

-------------------------------------------------------------------------------
🧩 Resumo

Ambientes virtuais são essenciais para:
- Isolar dependências
- Evitar conflitos de versão
- Organizar projetos
- Garantir reprodutibilidade do ambiente

-------------------------------------------------------------------------------
"""
