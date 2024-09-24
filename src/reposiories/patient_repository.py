from abc import ABC, abstractmethod
from  entities.patient import Patient

class PatientRepository(ABC):
  @abstractmethod
  def addPatient(self, patient: Patient):
    pass
  @abstractmethod
  def getAllPatients(self):
    pass

  
  @abstractmethod
  def getPatientById(self, id):
    pass
  
  @abstractmethod
  def savePatient(self, patient: Patient):
    pass
  
  @abstractmethod
  def getPatiensByNameAndTypeConsult(self, name, type_consult):
    pass
