<p align="center"><h1 align="center">GPT-VOICE-CONVERTER</h1></p>
<p align="center">
    <em>Fale com a IA, escute sua voz.</em>
</p>

## Índice

- [Índice](#índice)
- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Como Começar](#como-começar)
  - [Pré-requisitos](#pré-requisitos)
  - [Instalação](#instalação)
  - [Uso](#uso)
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
- **Linguagem de programação:** Python3
- **Gerenciador de pacotes:** Pip

### Instalação

1. Clone o repositório:
```sh
❯ git clone https://github.com/gomesfilipe/gpt-voice-converter.git
```

1. Instale as dependências:
```sh
❯ ./install-dependencies.sh
```

### Uso

Execute o programa com:
```sh
❯ python3 main.py
```