class Palabra:
    def __init__(self, palabra_en, palabra_es, palabra_informacion, siguiente=None, anterior = None):
        
        self.palabra_en = palabra_en
        self.palabra_es = palabra_es
        self.palabra_informacion = palabra_informacion
        self.siguiente = siguiente
        self.anterior = anterior


class Lista_Enlazada_Palabra:

    def __init__(self, ):

        self.inicio = None

        self.cantidad = 0

    def agregar_palabra(self, palabra_en, palabra_es, palabra_informacion,):

        nueva_palabra = Palabra(palabra_en, palabra_es, palabra_informacion,)

        if self.cantidad == 0:

            self.inicio = nueva_palabra
            self.cantidad +=1

        else:

            actual = self.inicio

            while actual.siguiente != None:

                actual = actual.siguiente
            
            
            actual.siguiente = nueva_palabra
            nueva_palabra.anterior = actual
            self.cantidad += 1                

        
    def buscar_palabra(self, palabra_en):

            actual = self.inicio

            if self.cantidad == 0:

                print("No hay lista enlazada")

            else:

                while actual:
                    
                    print(actual.palabra_en)
                    if actual.palabra_en == palabra_en:

                        print(f"Se encontró la palabra {actual.palabra_en}")

                        return actual

                    actual = actual.siguiente


                

    def siguiente_palabra(self, actual_palabra):
            
            actual = self.inicio

            if self.cantidad == 0:

                print("No hay lista enlazada")

            else:

                while actual:
                    
                    if actual.palabra_en == actual_palabra.palabra_en:

                        return actual.siguiente

                    actual = actual.siguiente

        


    def anterior_palabra(self, actual_palabra):
            
            actual = self.inicio


            if self.cantidad == 0:

                print("No hay lista enlazada")

            else:

                while actual:
                    
                    if actual.palabra_en == actual_palabra.palabra_en:

                        return actual.anterior

                    actual = actual.siguiente

  

    def imprimir_lista(self):

            actual = self.inicio

            if self.cantidad == 0:

                print("No hay lista enlazada")

            else:

                while actual:

                    print(f"{actual.palabra_en}", end = " <--> ")

                    actual = actual.siguiente
                



