from  entities.object_value.gender import Gender 
from  entities.object_value.type_consult import TypeConsult 
from typing import Optional

class PatientDTO:
  name: Optional[str]
  age: Optional[str]
  phone: Optional[str]
  gender: Optional[Gender]
  address: Optional[str]
  type_consult:  Optional[TypeConsult]
  email: Optional[str] = None 
  medical_history: Optional[str] = None

  def __init__(self,
      name: Optional[str],
      phone: Optional[str],
      gender: Optional[Gender],
      address: Optional[str],
      type_consult:  Optional[TypeConsult],
      email: Optional[str] = None, 
      medical_history: Optional[str] = None
    ):
        self.id = id
        self.name = name
        self.phone = phone
        self.gender = gender
        self.address = address
        self.type_consult = type_consult
        self.email = email
        self.medical_history = medical_history
        
  def setAgeInNumber(self, ageInNumber):
    try:
      self.age = int(ageInNumber)
    except ValueError:
      raise ValueError("A idade precisa ser um número inteiro.")