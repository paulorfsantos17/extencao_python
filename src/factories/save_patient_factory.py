from useCases.save_pacient import SavePatient
from reposiories.sqlite.patient_repository import PatientRepositorySqlite

class SavePatientFactory:
    @staticmethod
    def get_repository():
        # Instancia o repositório específico
        repository = PatientRepositorySqlite()
        
        # Passa o repositório para a classe de caso de uso RegisterPatient
        register_patient = SavePatient(repository)
        
        # Retorna a instância do caso de uso
        return register_patient

