from DTO.patient_DTO import PatientDTO
from factories.register_patient_factory import RegisterPatientFactory
from factories.save_patient_factory import SavePatientFactory
from factories.get_patient_by_id_factory import GetPatientByIdFactory
from factories.get_all_patient_factory import GetAllPatientFactory
from factories.get_patients_by_name_and_type_consult_factory import GetPatientsByNameAndTypeConsultFactory


class  PatientController:
  def __init__(self):
    self.registerPatient = RegisterPatientFactory.get_repository()
    self.savePatient = SavePatientFactory.get_repository()
    self.getPatientById = GetPatientByIdFactory.get_repository()
    self.getAllPatients = GetAllPatientFactory.get_repository()
    self.getPatientsByNameAndTypeConsult = GetPatientsByNameAndTypeConsultFactory.get_repository()
  
  
  def create_patient(self, new_patient: PatientDTO):
    self.validate_form_patient(new_patient)
    self.registerPatient.execute(new_patient)
  
  def get_all_patients(self):
    patients = self.getAllPatients.execute()
    return patients
    
    
  def get_patient(self, id):
    patient = self.getPatientById.execute(id)
    return patient
  

  def update_patient(self, id: str ,update_patient: PatientDTO ):
    self.validate_form_patient(update_patient)
    self.savePatient.execute(id, update_patient)
    
  def filter_patient(self, name, type_consult):
    patients = self.getPatientsByNameAndTypeConsult.execute(name, type_consult)
    return patients
    
  
  def validate_form_patient(self, new_patient: PatientDTO):
    if(len(new_patient.name) < 5):
      raise ValueError("Nome precisa ter mais de 5 caracteres.")
    
    if(len(new_patient.phone) != 11):
      raise ValueError("Telefone precisa ter 11 dígitos.")
    if(not new_patient.gender):
      raise ValueError("Genero precisa ser escolhido.")
    
    if(len(new_patient.address) < 10):
      raise ValueError("Endereço precisa ter mais de 10 caracteres.")
    
    if(not new_patient.type_consult):
      raise ValueError("Tipo de consulta precisa ser escolhido.")
    
    if(len(new_patient.email) < 8):
      raise ValueError("Email precisa ter mais de 8 caracteres.")
  