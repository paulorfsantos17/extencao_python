from reposiories.patient_repository import PatientRepository
from entities.patient import Patient

class GetPatientById:
  def __init__(self, patientRepository: PatientRepository):
    self.patientRepository = patientRepository
  def execute(self, patientId: str):
    patient:Patient = self.patientRepository.getPatientById(patientId)
    
    return patient
    