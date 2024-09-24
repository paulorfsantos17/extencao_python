from enum import Enum

class TypeConsult(Enum):
  PARTICULAR= "particular",
  AGREEMENT= "aggrement",
  @staticmethod
  def getNameTypeConsult( type_consult): 
    return "Convênio" if type_consult == TypeConsult.AGREEMENT  else "Particular"
    