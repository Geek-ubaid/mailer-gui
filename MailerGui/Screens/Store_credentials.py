import os
import bcrypt
import sqlite3
from sqlite3 import Error

class StoreCredentials():
    
    DB_DIR = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Assets','App Data'))
    DB_NAME = 'credentials.db'
    DB_PATH = os.path.join(DB_DIR,DB_NAME)

    def __init__(self):
        super(StoreCredentials, self).__init__()
        
    def check_for_creds_db(self):
        print(os.path.exists(self.DB_PATH))
        if os.path.exists(self.DB_PATH):
            # if self.check_if_any_table_exists():
            #     return True
            # else:
            return True
        else:
            return False
        
    def check_if_any_table_exists(self):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='user_db' ''')
        #if the count is 1, then table exists
        if c.fetchone()[0]==1 : 
            conn.close()
            return True
        else :
            conn.close()
            return False
                    
    def check_valid_connection(self, conn):
        if conn == None:
            return False
        else:
            return True   
    
    def get_connection(self):
        
        connection = None
        try:
            connection = sqlite3.connect(self.DB_PATH)
        except:
            pass
        return connection

    def execute_query(self,conn,query):
        
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            conn.commit()
            return 'Success'
        except Error as e:
            return 'Error'
            
    def execute_select_query(self,conn,query):
        
        cursor = conn.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except:
            return 'Error'
            
    def create_table(self,conn):
        
        query = """
        CREATE TABLE IF NOT EXISTS user_db(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT,
            mailprovider TEXT,
            providerkey TEXT,
            domainname TEXT,
            fromemail TEXT
        );
        """
        result =  self.execute_query(conn,query)
        return result
    
    def hash_credentials(self, password):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed

    def verify_credentials(self,password, hash):
        hashed_password = self.get_credentials(['password'])
        if hashed_password!='Error':
            if bcrypt.checkpw(passwd, hashed_password.encode('utf-8')):
                return True
            else:
                False
        else:
            return 'Not found'

    def get_non_hash_value(self, *args):
        pass

    def insert_credentials(self,conn,query_params):
        
        key = []
        value = []
        print(query_params)
        for i in query_params:
            print(i)
            if i[0] == 'password':
                hashed_password = self.hash_credentials(i[1]).decode('utf-8')
                value.append('"' + hashed_password + '"')
                key.append(i[0])
            else:
                key.append(i[0])
                value.append('"' + i[1] + '"')
            
        query = """
        INSERT INTO user_db ({})
        VALUES({});
        """.format(",".join(key), ",".join(value))
        result = self.execute_query(conn,query)
        return result
    
    def update_credentials(self, conn, filter_param ,query_params):
        
        update_params = []
           
        for i in query_params:
            if i[0] == 'password':
                if i[1]:
                    hashed_password = self.hash_credentials(i[1]).decode('utf-8')
                    update_params.append(i[0] + '=' + "'" + str(hashed_password) + "'")
                else:
                    pass
            else:
                update_params.append(i[0] + '=' + "'" + i[1] + "'")
            
        query = """
        UPDATE user_db
        SET {}
        WHERE {} = {};
        """.format(",".join(update_params),filter_param[0], "'" + filter_param[1] + "'" )
        
        print(query)
        result = self.execute_query(conn,query)
        return result
        
    def get_credentials(self,conn, query_params):
        
        select_params = []
        for i in query_params:
            select_params.append(i)
            
        query = """
        select {} from user_db;    
        """.format(",".join(select_params))
        result = self.execute_select_query(conn,query)
        print(result)
        return result