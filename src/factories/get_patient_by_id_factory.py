from useCases.get_patient_by_id import GetPatientById
from reposiories.sqlite.patient_repository import PatientRepositorySqlite

class GetPatientByIdFactory:
    @staticmethod
    def get_repository():
        # Instancia o repositório específico
        repository = PatientRepositorySqlite()
        
        # Passa o repositório para a classe de caso de uso RegisterPatient
        register_patient = GetPatientById(repository)
        
        # Retorna a instância do caso de uso
        return register_patient
