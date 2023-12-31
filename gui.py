import tkinter as tk


class First_Frame:

    def __init__(self, master, logica_asistente):

        self.master = master      
        self.logica_asistente = logica_asistente

        self.frame = tk.Frame(self.master, bg= "#4d6160")
        self.frame.pack()

        self.frame.config(width = '900', height = '500')

        #Title
        self.title = tk.Label(self.frame, text = "Asistente Virtual Inglés - Español", font= ("Arial", 25, "bold")
                              , bg = "#4d6160", fg = "white")
        self.title.place(x= 200 , y = 10)


        #Create button for press to listen

        self.button_press_to_listen = tk.Button(self.frame, text = 'Click! para escuchar', fg = "white", bg= "#292522",
                                            font= ("Arial", 14, "bold"), command = self.logica_asistente.run_asistente)

        self.button_press_to_listen.config(width= 20 , height= 5)
        
        self.button_press_to_listen.place(x= 320 , y = 350)

        #Image
        self.image = tk.PhotoImage(file = '.\img\ARIAS.png')
        
        self.logo = tk.Label(self.frame, image = self.image)
        self.logo.place(x= 250 , y = 80)

                        



    
    
    