import bcrypt
import sqlite3
from sqlite3 import Error

class StoreCredentials():
    
    PATH = r'C:\Users\HP\Desktop\DSC\MailGui\MailerGui\Assets\App Data\credentials.db'


    def __init__(self):
        
        super(StoreCredentials, self).__init__()
        self.connection = self.get_connection()
        
    def __del__(self):
        self.connection.close()
    
    def check_valid_connection(self):
        if self.connection == None:
            return False
        else:
            return True   
    
    def get_connection(self):
        
        connection = None
        print(self.PATH)

        connection = sqlite3.connect(self.PATH)

        return connection

    def execute_query(self,query):
        
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"The error '{e}' occurred")
            
    def execute_select_query(self,query):
        
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")
            
    def create_table(self):
        
        query = """
        CREATE TABLE IF NOT EXISTS user_db(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT,
            mail_provider TEXT,
            provider_key TEXT,
            domain_name TEXT,
            from_email TEXT
        );
        """
        self.execute_query(query)
        
    def hash_credentials(self, password):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('útf-8'), salt)
        return hashed

    # def verify_credentials(self,password, hash):
    #     if bcrypt.checkpw(passwd, hashed):
    #         return True
    #     else:
    #         False

    def get_non_hash_value(self):
        pass

    def insert_credentials(self,*args):
        
        query = """
        INSERT INTO user_db (username)
        VALUES(admin);
        """.format('username', 'admin')
        self.execute_query(query)

    def update_credentials(self, *args):
        
        query = """
        UPDATE
            user_db
        SET
            {};
        """.format('username=admin1')
        
        self.execute_query(query)
    
        
    def get_credentials(self, *args):
        
        query = """
        select column_name from information_schema.columns where table_name='user_db';    
        """
        result = self.execute_select_query(query)
        print(result)