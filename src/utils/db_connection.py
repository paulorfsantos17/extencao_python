import sqlite3

class DatabaseConnection:
    _connection = None
    
    @staticmethod
    def connect(db_name='meu_banco.db'):
        if DatabaseConnection._connection is None:
            DatabaseConnection._connection = sqlite3.connect(db_name)
            DatabaseConnection._create_tables(DatabaseConnection._connection)
        return DatabaseConnection._connection

    @staticmethod
    def _create_tables(conn):
        cursor = conn.cursor()
        
        # Criar a tabela de pacientes se não existir
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            phone TEXT NOT NULL,
            gender INTEGER NOT NULL,
            address TEXT NOT NULL,
            type_consult TEXT NOT NULL, 
            email TEXT,
            medical_history TEXT
        )
        ''')
        conn.commit()

    @staticmethod
    def close():
        if DatabaseConnection._connection is not None:
            DatabaseConnection._connection.close()
            DatabaseConnection._connection = None