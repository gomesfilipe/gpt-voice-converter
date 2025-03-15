<p align="center"><h1 align="center">GPT-VOICE-CONVERTER</h1></p>

## Autores
<ul>
    <li>Christian Junji Litzinger State</li>
    <li>Filipe Gomes Arante de Souza</li>
</ul>

## Índice

- [Índice](#índice)
- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Como Começar](#como-começar)
  - [Pré-requisitos](#pré-requisitos)
  - [Instalação](#instalação)
  - [Uso](#uso)
    - [Geração de chave da API do Gemini](#geração-de-chave-da-api-do-gemini)
    - [Configuração da chave](#configuração-da-chave)
    - [Execução](#execução)
---

## Visão Geral

O GPT-Voice-Converter permite conversas naturais com um modelo de linguagem grande (como o Google Gemini) usando apenas sua voz. Converte sua fala em texto, envia para a IA e reproduz a resposta de forma contínua. Ideal para usuários que buscam uma forma acessível e intuitiva de interagir com a IA, simplificando interações complexas em experiências naturais orientadas por voz.

---

## Funcionalidades

|      | Funcionalidade   | Resumo |
| :--- | :---:            | :---   |
| ⚙️  | **Arquitetura**  | <ul><li>Design modular com módulos separados para processamento de áudio (`src/audio_text_converters/`), interação com APIs GPT (`src/gpt_apis/`) e gestão de conversas (`src/chats/`).</li><li>Usa abordagem em camadas: classes abstratas para conversores de áudio e APIs GPT, facilitando extensões e trocas de implementações.</li><li>Arquivo de configuração (`config.py`) centraliza chaves de API e configurações, carregando do arquivo `.env`.</li><li>Ponto de entrada principal é `main.py`.</li></ul> |
| 🔩 | **Qualidade do Código** | Código modular em Python com tratamento robusto de exceções personalizadas e utilização de enums para melhorar a legibilidade e manutenção. |
| 📄 | **Documentação** | Documentação básica disponível em Python, incluindo `requirements.txt` e comandos para instalação, uso e testes. |
| 🔌 | **Integrações** | Integrações com APIs como Gemini, bibliotecas como pydub, gtts, speechrecognition e scipy, além de gerenciamento seguro de variáveis de ambiente com python-dotenv. |

---

## Estrutura do Projeto

```sh
└── gpt-voice-converter/
    ├── README.md
    ├── audios
    │   └── .gitkeep
    ├── config.py
    ├── install-dependencies.sh
    ├── main.py
    ├── requirements.txt
    └── src
        ├── audio_text_converters
        ├── chats
        ├── enums
        ├── exceptions
        └── gpt_apis
```

---

## Como Começar

### Pré-requisitos
- **Linguagem de programação:** Python 3.10
- **Gerenciador de pacotes:** Pip

### Instalação

1. Clone o repositório:
```sh
❯ git clone https://github.com/gomesfilipe/gpt-voice-converter.git
```

1. Instale as dependências:

Para a execução do *script* de instalação a seguir, será necessária a permissão de administrador (*sudo*) para a instalação da biblioteca `python3-pyaudio`.

```sh
❯ ./install-dependencies.sh
```

A instalação das dependências pode ser feita automaticamente usando o script `./install_dependencies`. Esse script instalará os pacotes Python diretamente para o seu usuário do computador.

Alternativamente, se preferir trabalhar em um ambiente isolado, você pode criar uma Virtual Environment (venv) e instalar as dependências nela, já que o projeto possui o arquivo `requirements.txt`. Siga os passos abaixo para utilizar a venv:

```bash
python3 -m venv venv          # cria a virtual environment
source venv/bin/activate     # ativa a virtual environment (Linux/Mac)
pip3 install -r requirements.txt  # instala os pacotes na venv
```

Após isso, execute o seu código normalmente com a venv ativada, mas lembre-se de instalar a biblioteca `python3-pyaudio` em seu sistema Linux.

### Uso

#### Geração de chave da API do Gemini

Caso não possua uma chave para a API do Gemini, gere uma, seguindo os seguintes passos:

1. Acesse a página oficial do Gemini no Google AI Studio: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey).
2. Faça login com a sua conta Google (se ainda não estiver logado).
3. Após o login, clique em **"Criar chave de API"**.
4. Copie a chave gerada e guarde-a em local seguro, pois você precisará dela para acessar a API posteriormente.

Para mais detalhes, confira a documentação oficial da API do Gemini:  
[https://ai.google.dev/tutorials/setup](https://ai.google.dev/tutorials/setup)

#### Configuração da chave

1. **Crie um arquivo `.env` na raiz do repositório**  
   Caso ainda não exista, execute no terminal:
   ```bash
   touch .env
   ```

2. **Adicione sua chave ao arquivo `.env`**  
   Abra o arquivo `.env` em um editor de texto e adicione a seguinte linha:
   ```env
   GPT_API_KEY=sua_chave_api_aqui
   ```

   Substitua `sua_chave_api_aqui` pela chave gerada anteriormente.

#### Execução

Execute o programa com:
```sh
❯ python3 main.py
```