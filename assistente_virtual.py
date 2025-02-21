import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import webbrowser
import wikipedia
from commands import execute_commands

class VirtualAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        wikipedia.set_lang('pt')

    def create_audio(self, text, lang='pt-br'):
        tts = gTTS(text=text, lang=lang)
        filename = "response.mp3"
        tts.save(filename)
        playsound(filename)
        os.remove(filename)

    def listen(self):
        with sr.Microphone() as source:
            print("Diga algo, estou te ouvindo...")
            # Adjust for ambient noise and timeout
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            self.recognizer.dynamic_energy_threshold = True
            
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
                print("Processando sua fala...")
                
                try:
                    text = self.recognizer.recognize_google(audio, language='pt-BR')
                    return text.lower()
                except sr.UnknownValueError:
                    self.create_audio("Desculpe, não entendi o que você disse.")
                    return None
                except sr.RequestError:
                    self.create_audio("Desculpe, houve um erro ao processar sua requisição.")
                    return None
                    
            except sr.WaitTimeoutError:
                self.create_audio("Não detectei nenhuma fala. Por favor, tente novamente.")
                return None

    def run(self):
        self.create_audio("Olá! Sou seu assistente virtual. Como posso ajudar?")
        
        while True:
            command = self.listen()
            if command:
                print(f"Você disse: {command}")
                execute_commands(command, self)

if __name__ == "__main__":
    assistant = VirtualAssistant()
    assistant.run()
