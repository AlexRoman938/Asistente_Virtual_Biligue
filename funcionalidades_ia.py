import pyttsx3
import speech_recognition as sr


class SpeechModule:

    def __init__(self, voice = 2, volume = 1, rate = 125):
        
        #Configurar el engine
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)

        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[voice].id)
    
    def talk(self, text):

        self.engine.say(text)
        self.engine.runAndWait()



class VoiceRecognitionModule:

    def __init__(self, key = None, name = ""):

        self.key = key #Por si tenemos una Key de google
        self.name = name
        self.r = sr.Recognizer()


    def recognize(self,):

        speech = SpeechModule()

        speech.talk("Te escucho")

        with sr.Microphone() as source:
            
            self.r.adjust_for_ambient_noise(source, duration=1)

            audio = self.r.listen(source, timeout= 4)

            try : 

                text = self.r.recognize_google(audio, key = self.key, language= "en")
                text = text.lower()
                
                if self.name in text:

                    text = text.replace(self.name, '')

                return text
            
            except:

                return None

