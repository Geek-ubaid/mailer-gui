from Store_credentials import StoreCredentials



creds = StoreCredentials()
creds.create_table()
creds.update_credentials(('username','admin'),[('password','ubaid124')])
creds.get_credentials(['username','password'])
