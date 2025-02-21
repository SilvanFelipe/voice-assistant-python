# Assistente Virtual em Python

Um assistente virtual que responde a comandos de voz, utilizando processamento de linguagem natural.

## Funcionalidades

- Conversão de texto para fala (Text-to-Speech)
- Reconhecimento de fala (Speech-to-Text)
- Pesquisa na Wikipedia
- Abertura de vídeos no YouTube
- Localização de farmácias próximas

## Requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/SilvanFelipe/voice-assistant-python.git
```

2. Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Para usuários Windows que tiverem problemas com PyAudio:
```bash
pip install pipwin
pipwin install pyaudio
```

## Uso

Execute o assistente virtual:
```bash
python assistente_virtual.py
```

### Comandos Disponíveis

- "wikipédia [termo]" - Pesquisa informações na Wikipédia
- "youtube [termo]" - Pesquisa vídeos no YouTube
- "abrir youtube" - Abre o site do YouTube
- "farmácia" - Busca farmácias próximas no Google Maps
- "sair" - Encerra o assistente

## Estrutura do Projeto

```
projeto-assistente-virtual/
│
├── assistente_virtual.py    # Arquivo principal
├── commands.py             # Módulo de comandos
├── requirements.txt        # Dependências
└── README.md              # Documentação
```

## Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.
