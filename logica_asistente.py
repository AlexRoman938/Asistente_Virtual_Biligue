
class Logica_Asistente():

    def __init__(self, voice_recognition, diccionario,):
          
          self.voice_recognition = voice_recognition
          self.diccionario = diccionario

    def run_asistente(self,):


        while True:

                texto = self.voice_recognition.recognize()

                if texto:

                        if 'busca' in texto:
                                
                                texto = texto.replace("busca ", "")

                                print(len(texto))
                                
                                self.diccionario.informacion_palabra(texto)


                        
                        elif 'anterior' in texto:
                                

                                self.diccionario.anterior_palabra()
                        

                        elif 'adelante' in texto:
                                

                                self.diccionario.siguiente_palabra()

                        elif 'apaga':
                               
                               break
                        
                        else:
                        
                                self.diccionario.mensajes_default()
