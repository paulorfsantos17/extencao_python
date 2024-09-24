import tkinter as tk
from screens.register import Register 
from screens.list import List 

class App(tk.Tk):
    def __init__(self):
      super().__init__()
      
    
      self.title('Registro de pacientes')
      self.geometry('1200x680')
      
      self.frames = {}

        # Cria os frames e os adiciona ao dicionário
      for F in (Register, List):
          frame = F(self)
          self.frames[F] = frame
          frame.pack(fill="both", expand=True)
          frame.pack_forget()
      
      self.create_menu()
      self.show_frame(Register)
      

    
    
    def create_menu(self):  # Adicionada a função para criação do menu
        menu_frame = tk.Frame(self, bg="lightgray")
        menu_frame.pack(side="top", fill="x")
        

        btn_new = tk.Button(menu_frame, text="Registar", command=self.open_register)
        btn_new.pack(side="left", padx=5, pady=5)

        btn_open = tk.Button(menu_frame, text="Lista", command=self.open_list)
        btn_open.pack(side="left", padx=5, pady=5)
        
        
    def show_frame(self, frame_class):
      # Esconde todos os frames
      for frame in self.frames.values():
        frame.pack_forget()
        
      if hasattr(frame, 'update_table'):
        frame.update_table()
        
      # Mostra o frame desejado
      frame = self.frames[frame_class]
      frame.pack(fill="both", expand=True)
      
      
    def open_register(self):
      self.show_frame(Register)  # Mostra a tela de cadastro
    def open_list(self):
      self.show_frame(List)  # Mostra a tela de cadastro