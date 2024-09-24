from reposiories.patient_repository import PatientRepository
from entities.patient import Patient
from DTO.patient_DTO import PatientDTO

class RegisterPatient:
  def __init__(self, patientRepository: PatientRepository):
    self.patientRepository = patientRepository
  def execute(self, new_patient: PatientDTO):
    
    patient = Patient.createdPatient(
      name=new_patient.name, 
      age=new_patient.age,
      phone=new_patient.phone,
      gender=new_patient.gender,
      address=new_patient.address,
      type_consult=new_patient.type_consult,
      email=new_patient.email,
      medical_history=new_patient.medical_history
    )
    self.patientRepository.addPatient(patient)
    