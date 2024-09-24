from useCases.register_patient import RegisterPatient
from reposiories.sqlite.patient_repository import PatientRepositorySqlite

class RegisterPatientFactory:
    @staticmethod
    def get_repository():
        # Instancia o repositório específico
        repository = PatientRepositorySqlite()
        
        # Passa o repositório para a classe de caso de uso RegisterPatient
        register_patient = RegisterPatient(repository)
        
        # Retorna a instância do caso de uso
        return register_patient

