from entities.patient import Patient
from typing import List

from utils.db_connection import DatabaseConnection


from reposiories.patient_repository import PatientRepository

class PatientRepositorySqlite(PatientRepository):
  def addPatient(self, patient):
    conn = DatabaseConnection.connect()
    cursor = conn.cursor()
    
    name = patient.name
    age = patient.age
    phone = patient.phone
    gender = patient.gender
    address = patient.address
    type_consult = patient.type_consult
    email = patient.email
    medical_history = patient.medical_history

    
    
    
    # Inserir dados na tabela
    cursor.execute('''
    INSERT INTO patients (
      name,
      age,
      phone,
      gender,
      address,
      type_consult,
      email,
      medical_history 
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', ( 
      name,
      age,
      phone,
      gender,
      address,
      type_consult,
      email,
      medical_history
    ))
    
    # Salvar (commit) as alterações
    conn.commit()
    
    # Fechar a conexão
    DatabaseConnection.close()
    
    
  def getAllPatients(self) -> List[Patient]:
    
    conn = DatabaseConnection.connect()
    cursor = conn.cursor()
    
    patients = []
    
    
    # Inserir dados na tabela
    cursor.execute('''
     SELECT * FROM patients
    ''')
    
    # Recuperar os resultados
    resultados = cursor.fetchall()
    
    for row in resultados:
      id,  name, age, phone, gender, address, type_consult, email, medical_history = row
      patient = Patient(id,
      name,
      age,
      phone,
      gender,
      address,
      type_consult,
      email,
      medical_history 
    )
      patients.append(patient)
    
    # Salvar (commit) as alterações
    conn.commit()
    
    # Fechar a conexão
    DatabaseConnection.close()
    
    
    return patients
  
  def getPatientById(self, id):
    
    conn = DatabaseConnection.connect()
    cursor = conn.cursor()
    
    # Inserir dados na tabela
    cursor.execute('''
     SELECT * FROM patients WHERE id = ?
    ''',(id,))
    
    # Recuperar os resultados
    result = cursor.fetchone()
    
    id,  name, age, phone, gender, address, type_consult, email, medical_history = result
    patient = Patient(id,
      name,
      age,
      phone,
      gender,
      address,
      type_consult,
      email,
      medical_history 
    )
    
    # Salvar (commit) as alterações
    conn.commit()
    
    # Fechar a conexão
    DatabaseConnection.close()
    
    
    return patient
  
  def savePatient(self, patient):
    conn = DatabaseConnection.connect()
    cursor = conn.cursor()
    
    name = patient.name
    age = patient.age
    phone = patient.phone
    gender = patient.gender
    address = patient.address
    type_consult = patient.type_consult
    email = patient.email
    medical_history = patient.medical_history
    id = patient.id
    
    
    # Inserir dados na tabela
    cursor.execute('''
    UPDATE patients SET 
      name = ?,
      age = ?,
      phone = ?,
      gender = ?,
      address = ?,
      type_consult = ?,
      email = ?,
      medical_history = ? 
      WHERE id =?
    ''', (      
      name,
      age,
      phone,
      gender,
      address,
      type_consult,
      email,
      medical_history,
      id
    ))
    
    # Salvar (commit) as alterações
    conn.commit()
    
    # Fechar a conexão
    DatabaseConnection.close()
    

  def getPatiensByNameAndTypeConsult(self, name, type_consult):
    conn = DatabaseConnection.connect()
    cursor = conn.cursor()
    patients = []

    # Construir a consulta SQL e parâmetros dinamicamente
    query = 'SELECT * FROM patients WHERE 1=1'
    params = []
    
    if name:
        query += ' AND name LIKE ?'
        params.append(f'%{name}%')
    
    if type_consult:
        query += ' AND type_consult = ?'
        params.append(type_consult)
    # Executar a consulta com parâmetros
    cursor.execute(query, params)
    
    


    # Recuperar os resultados
    resultados = cursor.fetchall()
    
    for row in resultados:
      id,  name, age, phone, gender, address, type_consult, email, medical_history = row
      patient = Patient(id,
      name,
      age,
      phone,
      gender,
      address,
      type_consult,
      email,
      medical_history 
    )
      patients.append(patient)

    
    # Salvar (commit) as alterações
    conn.commit()
    
    # Fechar a conexão
    DatabaseConnection.close()
    
    
    return patients
  
