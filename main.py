import tkinter as tk

from gui import First_Frame
from diccionario import Diccionario
from palabras import Palabra, Lista_Enlazada_Palabra
from funcionalidades_ia import SpeechModule, VoiceRecognitionModule
from logica_asistente import Logica_Asistente


#Interfaz gráfica
branch = tk.Tk()
branch.title('ASISTENTE BILINGÜE INGLÉS - ESPAÑOL')
branch.resizable(0,0)



if __name__ == '__main__':

    # Crear una lista enlazada principal
    lista_canciones = Lista_Enlazada_Palabra()

    palabra1 = Palabra("water", "Agua", "Para referirse al líquido transparente e incoloro esencial para la vida")
    palabra2 = Palabra("house", "Casa", "Para describir un lugar de residencia")
    palabra3 = Palabra("work", "Trabajo", "Para referirse a una actividad laboral")
    palabra4 = Palabra("time", "Tiempo", "Para hablar sobre la duración o momentos de las cosas")
        

    # Agregar nodos a la lista principal, cada uno con su propia lista enlazada
    lista_canciones.agregar_palabra(palabra1.palabra_en, palabra1.palabra_es, palabra1.palabra_informacion)
    lista_canciones.agregar_palabra(palabra2.palabra_en, palabra2.palabra_es, palabra2.palabra_informacion)
    lista_canciones.agregar_palabra(palabra3.palabra_en, palabra3.palabra_es, palabra3.palabra_informacion)
    lista_canciones.agregar_palabra(palabra4.palabra_en, palabra4.palabra_es, palabra4.palabra_informacion)

    #Funcionalidades IA
    
    speech_es, voice_recognition = SpeechModule(), VoiceRecognitionModule()
    
    #Reproductor
    diccionario = Diccionario(palabra1, lista_canciones, speech_es)

    #Logica Asistente
    logica_asistente = Logica_Asistente(voice_recognition, diccionario)

    #Frame Principal
    miFrame = First_Frame(branch, logica_asistente)

    branch.mainloop()