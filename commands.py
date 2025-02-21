import webbrowser
import wikipedia
import sys

def execute_commands(command, assistant):
    if 'sair' in command:
        assistant.create_audio("Até logo!")
        sys.exit()
        
    elif 'wikipédia' in command:
        search_term = command.replace('wikipédia', '').strip()
        try:
            result = wikipedia.summary(search_term, sentences=2)
            assistant.create_audio(result)
        except:
            assistant.create_audio("Desculpe, não encontrei informações sobre isso.")
            
    elif 'youtube' in command:
        if 'abrir' in command:
            webbrowser.open('https://youtube.com')
        else:
            search_term = command.replace('youtube', '').strip()
            webbrowser.open(f'https://www.youtube.com/results?search_query={search_term}')
            
    elif 'farmácia' in command:
        webbrowser.open('https://www.google.com/maps/search/farmacia+proxima')
        assistant.create_audio("Buscando farmácias próximas no Google Maps")
        
    else:
        assistant.create_audio("Desculpe, não entendi o comando.")
