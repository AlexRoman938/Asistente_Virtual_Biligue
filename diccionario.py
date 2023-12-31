class Diccionario():
    
    def __init__(self, palabra, lista_palabras, speech_es):


        self.palabra = palabra

        self.lista_palabras = lista_palabras

        self.speech_es = speech_es


    def informacion_palabra(self, palabra):

        try:

            self.speech_es.talk("Buscando la palabra")
            self.speech_es.talk(palabra)

            palabra_buscada = self.lista_palabras.buscar_palabra(palabra)

            self.palabra = palabra_buscada

            self.speech_es.talk(f"La palabra traducida al español es {self.palabra.palabra_es}")

            self.speech_es.talk(f"Esta palabra se usa {self.palabra.palabra_informacion}")

        except Exception:

            self.speech_es.talk(f"No existe la palabra {palabra} en el diccionario")




    def siguiente_palabra(self):

        try:

            next_palabra = self.lista_palabras.siguiente_palabra(self.palabra)
            self.palabra = next_palabra

            self.speech_es.talk("La siguiente palabra de la lista es")
            self.speech_es.talk(self.palabra.palabra_en)

            self.speech_es.talk(f"La palabra traducida al español es {self.palabra.palabra_es}")

            self.speech_es.talk(f"Esta palabra se usa {self.palabra.palabra_informacion}")

        except:

            self.speech_es.talk(f"No existe una siguiente palabra")







    def anterior_palabra(self,):

        
        try:
            
            previous_palabra = self.lista_palabras.anterior_palabra(self.palabra)
            self.palabra = previous_palabra

            self.speech_es.talk(f"La anterior palabra de la lista es")
            self.speech_es.talk(self.palabra.palabra_en)

            self.speech_es.talk(f"La palabra traducida al español es {self.palabra.palabra_es}")

            self.speech_es.talk(f"Esta palabra se usa {self.palabra.palabra_informacion}")

        except:

            self.speech_es.talk(f"No existe una anterior palabra")


    def mensajes_default(self,):

        return self.speech_es.talk("Lo siento no entendí")






        


    

 
    