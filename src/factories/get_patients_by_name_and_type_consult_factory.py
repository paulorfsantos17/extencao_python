from useCases.get_patients_by_name_and_type_consult import GetPatientsByNameAndTypeConsult
from reposiories.sqlite.patient_repository import PatientRepositorySqlite

class GetPatientsByNameAndTypeConsultFactory:
    @staticmethod
    def get_repository():
        # Instancia o repositório específico
        repository = PatientRepositorySqlite()
        
        # Passa o repositório para a classe de caso de uso RegisterPatient
        patients_get_partiens = GetPatientsByNameAndTypeConsult(repository)
        
        # Retorna a instância do caso de uso
        return patients_get_partiens
