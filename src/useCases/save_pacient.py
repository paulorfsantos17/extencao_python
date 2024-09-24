from reposiories.patient_repository import PatientRepository
from entities.patient import Patient
from DTO.patient_DTO import PatientDTO

class SavePatient:
  def __init__(self,  patientRepository: PatientRepository):
    self.patientRepository = patientRepository
  def execute(self, id: str, patient:PatientDTO):
    update_patient = Patient(
            id=id,
            name=patient.name,
            email=patient.email,
            age=patient.age,
            phone=patient.phone,
            gender=patient.gender,
            address=patient.address,
            type_consult=patient.type_consult,
            medical_history=patient.medical_history
        )
    self.patientRepository.savePatient(update_patient)
    
    