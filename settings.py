class Settings:
    TOKEN = {'Authorization': 'Bearer keyIA3e2zB5jiDiEi', 'Content-Type': 'application/json'}
    TABLE_NAME = 'Cars'
    BASE_ID = 'appIdlQ6YQ7pKEp8m'
    URL = '?maxRecords=3&view=Grid%20view'
    BODY_TYPE = 'hatchback, minivan, coupe, sedan, pickup, universal, suv'
    FILE_NAME = 'db.json'


    def get_url(self):
        return f'https://api.airtable.com/v0/{self.BASE_ID}/{self.TABLE_NAME}/'


settings = Settings()



