from reposiories.patient_repository import PatientRepository
from entities.patient import Patient

class GetPatientsByNameAndTypeConsult:
  def __init__(self, patientRepository: PatientRepository):
    self.patientRepository = patientRepository
  def execute(self, name, type_consult):
    patient: Patient = self.patientRepository.getPatiensByNameAndTypeConsult(name, type_consult)
    
    return patient
    