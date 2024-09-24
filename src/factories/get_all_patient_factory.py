from useCases.get_all_patients import GetAllPatients
from reposiories.sqlite.patient_repository import PatientRepositorySqlite

class GetAllPatientFactory:
    @staticmethod
    def get_repository():
        # Instancia o repositório específico
        repository = PatientRepositorySqlite()
        
        # Passa o repositório para a classe de caso de uso RegisterPatient
        register_patient = GetAllPatients(repository)
        
        # Retorna a instância do caso de uso
        return register_patient
