from reposiories.patient_repository import PatientRepository
from typing import List
from entities.patient import Patient 

class GetAllPatients():
  def __init__(self, patientRepository: PatientRepository):
    self.patientRepository = patientRepository
  def execute(self):
    patients: List[Patient] = self.patientRepository.getAllPatients()
    return patients
