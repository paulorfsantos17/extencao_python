import tkinter as tk
from DTO.patient_DTO import PatientDTO
from  controller.patient_controller import PatientController
from entities.object_value.gender import Gender
from entities.object_value.type_consult import TypeConsult
from tkinter import messagebox

class Register(tk.Frame):
  def __init__(self, parent):
    super().__init__(parent)
    
    label = tk.Label(self, text="Cadastro")
    label.grid(column=1, row= 0, padx=20, pady=20)
    self.patient_controller = PatientController()
    
    self.selected_gender = tk.StringVar(value='male')
    self.selected_type_consult =  tk.StringVar(value='particular')
    self.create_form()
    
  def create_form(self):
    label_name = tk.Label(self, text="Nome:")
    label_name.grid(column=0, row=1, padx=20, pady=20, sticky='w')
    self.entry_name = tk.Entry(self, width=50)
    self.entry_name.grid(column=1, row=1, padx=20, pady=20, sticky='w')
    

    
    label_age = tk.Label(self, text="Idade:")
    label_age.grid(column=2, row=1, padx=20, pady=20, sticky='w')
    self.entry_age = tk.Entry(self, width=20)
    self.entry_age.grid(column=3, row=1, padx=20, pady=20, sticky='w')
    
    label_phone = tk.Label(self, text="Telefone:",)
    label_phone.grid(column=0, row=2, padx=20, pady=20, sticky='w')
    self.entry_phone = tk.Entry(self)
    self.entry_phone.grid(column=1, row=2, padx=20, pady=20, sticky='w')
    
    label_gender = tk.Label(self, text="Genero:")
    label_gender.grid(column=2, row=2, padx=20, pady=20, sticky='w')
    self.create_radio_buttons_gender()
    
    label_address = tk.Label(self, text="Endereco:")
    label_address.grid(column=0, row=3, padx=20, pady=20, sticky='w')
    self.entry_address = tk.Entry(self, width=50)
    self.entry_address.grid(column=1, row=3, padx=20, pady=20, sticky='w')
    
    
    label_type_consult = tk.Label(self, text="Tipo de consulta:")
    label_type_consult .grid(column=2, row=3, padx=20, pady=20, sticky='w')
    self.create_radio_buttons_type_consult()
  
    
    label_email = tk.Label(self, text="Email:")
    label_email.grid(column=0, row=4, padx=20, pady=20, sticky='w')
    self.entry_email = tk.Entry(self, width=50)
    self.entry_email.grid(column=1, row=4, padx=20, pady=20, sticky='w')
    
    label_medical_history = tk.Label(self, text="Historico Médico:")
    label_medical_history.grid(column=0, row=5, padx=20, pady=20, sticky='w')
    self.entry_medical_history = tk.Text(self, wrap=tk.WORD,  height=10, width=100)
    self.entry_medical_history.grid(column=1, columnspan=3, row=5, padx=20, pady=20, sticky='w')
    
    self.button_cadastrar = tk.Button(self, text="Cadastrar" , command=self.register)
    self.button_cadastrar.grid(column=1, row=6, padx=20, pady=20)
    
    
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
      rb.grid(column=positionColumn, row=3,  pady=20, sticky='w')
      positionColumn = positionColumn +1
  def create_radio_buttons_gender(self):
    positionColumn = 3

    for gender in Gender:
      gender_text =  "Homem" if gender == Gender.MALE  else "Mulher"
      rb = tk.Radiobutton(
        self,
        text=gender_text,
        value=gender.value,
        variable=self.selected_gender
      )
      rb.grid(column=positionColumn, row=2,  pady=20, sticky='w')
      positionColumn = positionColumn +1

  
  def reset_entries(self):
    # Lista dos campos Entry
    entries = [
      self.entry_name,
      self.entry_age,
      self.entry_phone,
      self.entry_email,
      self.entry_address,
      ]
    
    self.entry_medical_history.delete("1.0", tk.END)
    
    # Itera sobre os campos e zera cada um deles
    for entry in entries:
        entry.delete(0, tk.END)
        
  def register(self):
    name = self.entry_name.get()
    age = self.entry_age.get()
    phone = self.entry_phone.get()
    gender = self.selected_gender.get()
    address = self.entry_address.get()
    type_consult = self.selected_type_consult.get()
    email = self.entry_email.get()
    
    medical_history = self.entry_medical_history.get("1.0", tk.END).strip()
    
    new_patient = PatientDTO(   
      name=name, 
      phone=phone,
      gender=gender,
      address=address,
      type_consult=type_consult,
      email=email,
      medical_history=medical_history
    )
    
    try:
      new_patient.setAgeInNumber(age)
      self.patient_controller.create_patient(new_patient)
    except Exception as e:
      messagebox.showerror("Erro", str(e))
    else:
      messagebox.showinfo("Sucesso", "Paciente cadastrado com sucesso!")
      self.reset_entries() # Reseta os campos para entrada de novos dados
    