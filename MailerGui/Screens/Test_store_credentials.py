from Store_credentials import StoreCredentials

creds = StoreCredentials()
creds.create_table()
creds.insert_credentials(['asdas','asdasd'])
creds.get_credentials(['asd','sada'])
