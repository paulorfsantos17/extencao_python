import tkinter as tk
from tkinter import ttk
from screens.patient import PaientView
from  entities.object_value.type_consult import TypeConsult

from controller.patient_controller import PatientController

class List(tk.Frame):
  def __init__(self, parent):
    super().__init__(parent)
    self.rowconfigure(0,weight=1)
    self.rowconfigure(1,weight=1)
    self.rowconfigure(2,weight=10)
    self.columnconfigure(0, weight= 1)
    self.columnconfigure(1, weight= 2)
    self.columnconfigure(2, weight= 1)
    self.columnconfigure(3, weight= 1)
    self.columnconfigure(4, weight= 1)
    self.columnconfigure(5, weight= 1)

    
    self.selected_type_consult =  tk.StringVar(value='')

    self.create_table()
    
    self.patient_controller = PatientController()




  def update_table(self):
    # Limpar a tabela existente
    self.tree.delete(*self.tree.get_children())

    self.fetchAllPatients()
    self.tree.bind("<ButtonRelease-1>", self.on_click)
    
  def form_search(self):
    label_name = tk.Label(self, text="Nome:", width=5  )
    label_name.grid(row=1, column=0,  pady=20 )
    self.entry_name = tk.Entry(self, width=50)
    self.entry_name.grid(row=1, column=1,pady=20,)
    label_type_consult = tk.Label(self, text="Tipo de consulta:")
    label_type_consult.grid(row=1, column=2, padx=20, pady=20 )
    self.create_radio_buttons_type_consult()
    button_search  = tk.Button(self, text="Pesquisar", command=self.filterPatient)
    button_search.grid(row=1, column=5, padx=20, pady=20)
    
  
  def create_table(self):	
    label = tk.Label(self, text="Lista")
    label.grid(row=0, column=2, padx=20, pady=20)
    self.form_search()
    
    # Criar o Treeview (tabela)
    self.tree = ttk.Treeview(self, columns=("id", "nome", "email","tipo de consulta"), show="headings")
    self.tree.heading("id", text="ID")
    self.tree.heading("nome", text="Nome")
    self.tree.heading("email", text="Email")
    self.tree.heading("tipo de consulta", text="Tipo de consulta")
    
    # Adicionar as colunas
    self.tree.column("id", width=100)
    self.tree.column("nome", width=150)
    self.tree.column("email", width=150)
    self.tree.column("tipo de consulta", width=100)
    
    # Adicionar o Treeview à interface
    self.tree.grid(row=2, column=0, columnspan=6, padx=20, pady=20, sticky="nsew")
    
    self.grid_rowconfigure(1, weight=1)
    self.grid_columnconfigure(0, weight=1)

  # Função para lidar com o clique, com parâmetros passados
  def on_item_click(self,item):
      values = self.tree.item(item, 'values')  # Obtém os valores do item clicado
      self.getPatient(values[0])

  # Função de callback para o clique do botão
  def on_click(self,event):
      item = self.tree.identify_row(event.y)  # Identifica o item com base na posição do clique
      if item:  # Verifica se um item foi clicado
          self.on_item_click(item)
  
  
  def create_radio_buttons_type_consult(self):
    positionColumn = 3

    for type_consult in TypeConsult:
      gender_text =  "Convênio" if type_consult == TypeConsult.AGREEMENT  else "Particular"
      rb = tk.Radiobutton(
        self,
        text=gender_text,
        value=type_consult.value,
        variable=self.selected_type_consult
      )
      rb.grid(column=positionColumn, row=1,  pady=20)
      positionColumn = positionColumn +1

    
  def open_Pacient_info(self, patient):
    new_window = tk.Toplevel(self)
    new_window.geometry("1280x720")
    new_window.title("Paciente")
    
    frame = PaientView(new_window, patient, self.update_table)
    frame.pack(fill="both", expand=True)
    
  def getPatient(self, id):
    patient = self.patient_controller.get_patient(id)

    self.open_Pacient_info(patient)
    
  
  def fetchAllPatients(self):
    patients = self.patient_controller.get_all_patients()
    self.intertDataInTable(patients)

  def filterPatient(self):
    name = self.entry_name.get()
    type_consult = self.selected_type_consult.get()
    
    patients = self.patient_controller.filter_patient(name, type_consult)
    
    self.tree.delete(*self.tree.get_children())
    
    self.intertDataInTable(patients)
    
    self.entry_name.delete(0, tk.END), 
    self.selected_type_consult.set('')
    
  def intertDataInTable(self, patients):
    for patient in patients:
      self.tree.insert("", tk.END, values=(
        patient.id,
        patient.name,
        patient.email,
        TypeConsult.getNameTypeConsult(patient.type_consult)
      ))
    