from  .object_value.gender import Gender 
from  .object_value.type_consult import TypeConsult 
from typing import Optional

class Patient:
  def __init__(self,
      id: str,
      name: str,
      age: int,
      phone: str,
      gender: Gender,
      address: str,
      type_consult: TypeConsult,
      email: Optional[str] = None, 
      medical_history: Optional[str] = None
    ):
        self.id = id
        self.name = name
        self.age = age
        self.phone = phone
        self.gender = gender
        self.address = address
        self.type_consult = type_consult
        self.email = email
        self.medical_history = medical_history
      

    
  
  @classmethod
  def createdPatient(cls,
    name: str,
    age: int,
    phone: str,
    gender: Gender,
    address: str,
    type_consult: TypeConsult,
    email: Optional[str] = None,
    medical_history: Optional[str] = None
  ) -> 'Patient':
    return cls(
      id=None,
      name=name,
      email=email,
      age=age,
      phone=phone,
      gender=gender,
      address=address,
      type_consult=type_consult,
      medical_history=medical_history
    )
    