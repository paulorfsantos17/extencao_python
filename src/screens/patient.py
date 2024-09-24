import tkinter as tk
from DTO.patient_DTO import PatientDTO
from entities.patient import Patient
from controller.patient_controller import PatientController
from entities.object_value.gender import Gender
from entities.object_value.type_consult import TypeConsult
from tkinter import messagebox

class PaientView(tk.Frame):
  def __init__(self, parent, pacientInfo: Patient, updateList):
    super().__init__(parent)
    self.updateList = updateList
    
    self.patient_id = pacientInfo.id
    self.patient_name = tk.StringVar(value=pacientInfo.name)
    self.patient_age = tk.StringVar(value=pacientInfo.age)
    self.patient_phone = tk.StringVar(value=pacientInfo.phone)
    self.selected_gender = tk.StringVar(value=pacientInfo.gender)
    self.patient_address = tk.StringVar(value=pacientInfo.address)
    self.selected_type_consult =  tk.StringVar(value=pacientInfo.type_consult)
    self.patient_email = tk.StringVar(value=pacientInfo.email)
    self.patient_medical_history = pacientInfo.medical_history
    
    

    
    label = tk.Label(self, text="Paciente")
    label.grid(column=1, row= 0, padx=20, pady=20)
    self.patient_controller: PatientController = PatientController()
    
    self.create_form()
    
  def create_form(self):
    label_name = tk.Label(self, text="Nome:")
    label_name.grid(column=0, row=1, padx=20, pady=20, sticky='w')
    self.entry_name = tk.Entry(self, 
      textvariable=self.patient_name, state="disabled", width=50
    )
    self.entry_name.grid(column=1, row=1, padx=20, pady=20, sticky='w')
    

    
    label_age = tk.Label(self, text="Idade:")
    label_age.grid(column=2, row=1, padx=20, pady=20, sticky='w')
    self.entry_age = tk.Entry(self, 
      textvariable=self.patient_age, state="disabled"
    )
    self.entry_age.grid(column=3, row=1, padx=20, pady=20,  sticky='w')
    
    label_phone = tk.Label(self, text="Telefone:")
    label_phone.grid(column=0, row=2, padx=20, pady=20, sticky='w')
    self.entry_phone = tk.Entry(self,
      textvariable=self.patient_phone, state="disabled"                      
    )
    self.entry_phone.grid(column=1, row=2, padx=20, pady=20, sticky='w')
    
    label_gender = tk.Label(self, text="Genero:")
    label_gender.grid(column=2, row=2, padx=20, pady=20, sticky='w')
    self.create_radio_buttons_gender()
    
    label_address = tk.Label(self, text="Endereco:")
    label_address.grid(column=0, row=3, padx=20, pady=20, sticky='w')
    self.entry_address = tk.Entry(self,
      textvariable=self.patient_address, state="disabled", width=50
    )
    self.entry_address.grid(column=1, row=3, padx=20, pady=20, sticky='w')
    
    
    label_type_consult = tk.Label(self, text="Tipo de consulta:")
    label_type_consult .grid(column=2, row=3, padx=20, pady=20, sticky='w')
    self.create_radio_buttons_type_consult()
  
    
    label_email = tk.Label(self, text="Email:")
    label_email.grid(column=0, row=4, padx=20, pady=20, sticky='w')
    self.entry_email = tk.Entry(self,
      textvariable=self.patient_email, state="disabled", width=50
    )
    self.entry_email.grid(column=1, row=4, padx=20, pady=20, sticky='w')
    
    label_medical_history = tk.Label(self, text="Historico Médico:")
    label_medical_history.grid(column=0, row=5, padx=20, pady=20, sticky='w')
    self.entry_medical_history = tk.Text(self,
      wrap=tk.WORD,
      height=10,
      width=100,
    )
    self.entry_medical_history.insert(tk.END, self.patient_medical_history)
    self.entry_medical_history.config(state=tk.DISABLED)
    self.entry_medical_history.grid(column=1, columnspan=3, row=5, padx=20, pady=20, sticky='w')
    
    self.button_cadastrar = tk.Button(self, text="Atualizar" , command=self.activeUpdate)
    self.button_cadastrar.grid(column=1, row=6, padx=20, pady=20)
    
    self.button_save = tk.Button(self, text="Salvar" , command=self.updatePatient, state='disabled' )
    self.button_save.grid(column=2, row=6, padx=20, pady=20)
    
  def create_radio_buttons_type_consult(self):
      self.rb_type_consult_agreement = tk.Radiobutton(
        self,
        text="Convênio",
        value=TypeConsult.AGREEMENT.value,
        variable=self.selected_type_consult,
        state='disabled'
      )
      self.rb_type_consult_agreement.grid(column=3, row=3,  pady=20, sticky='w')
      self.rb_type_consult_particular = tk.Radiobutton(
        self,
        text="Particular",
        value=TypeConsult.PARTICULAR.value,
        variable=self.selected_type_consult,
        state='disabled'
      )
      self.rb_type_consult_particular.grid(column=4, row=3,  pady=20, sticky='w')
  
  def create_radio_buttons_gender(self):
      self.rb_gender_male = tk.Radiobutton(
        self,
        text="Homem",
        value=Gender.MALE.value,
        variable=self.selected_gender,
        state="disabled"
      )
      self.rb_gender_male.grid(column=3, row=2,  pady=20, sticky='w')
      
      self.rb_gender_female = tk.Radiobutton(
        self,
        text="Mulher",
        value=Gender.FEMALE.value,
        variable=self.selected_gender,
        state="disabled"
      )
      self.rb_gender_female.grid(column=4, row=2,  pady=20, sticky='w')
  def activeUpdate(self):
    self.entry_name.config(state='normal')
    self.entry_age.config(state='normal')
    self.entry_phone.config(state='normal')
    self.entry_address.config(state='normal')
    self.rb_gender_male.config(state='active')
    self.rb_gender_female.config(state='active')
    self.entry_address.config(state='normal')
    self.rb_type_consult_agreement.config(state='active')
    self.rb_type_consult_particular.config(state='active')
    self.entry_email.config(state='normal')
    self.entry_medical_history.config(state='normal')

    self.button_save.config(state='normal')
    self.button_cadastrar.config(state='disabled')
    
  def disableUpdate(self):
    self.entry_name.config(state='readonly')
    self.entry_age.config(state='readonly')
    self.entry_phone.config(state='readonly')
    self.entry_address.config(state='readonly')
    self.rb_gender_male.config(state='disabled')
    self.rb_gender_female.config(state='disabled')
    self.entry_address.config(state='readonly')
    self.rb_type_consult_agreement.config(state='disabled')
    self.rb_type_consult_particular.config(state='disabled')
    self.entry_email.config(state='readonly')
    self.entry_medical_history.config(state='disabled')
    
    self.button_save.config(state='disabled')
    self.button_cadastrar.config(state='normal')
    
  def updatePatient(self):
    id = self.patient_id
    name = self.entry_name.get()
    age = int(self.entry_age.get())
    phone = self.entry_phone.get()
    gender = self.selected_gender.get()
    address = self.entry_address.get()
    type_consult = self.selected_type_consult.get()
    email = self.entry_email.get()
    
    medical_history = self.entry_medical_history.get("1.0", tk.END).strip()
    update_patient = PatientDTO(
      name=name, 
      phone=phone,
      gender=gender,
      address=address,
      type_consult=type_consult,
      email=email,
      medical_history=medical_history
    )
    
    try:
      update_patient.setAgeInNumber(age)
      self.patient_controller.update_patient(id, update_patient)
    except Exception as e:
      messagebox.showerror("Erro", str(e))
    else:
      messagebox.showinfo("Sucesso", "Paciente Atualizado com sucesso!")

    
    self.updateList ()
    
    self.disableUpdate()

    
    