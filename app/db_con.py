import mysql.connector

# My DB Connection

class Database:
    def __init__(self, host, user, passwrd, my_database):
        self.host = host
        self.user = user
        self.passwrd = passwrd
        self.database = my_database

    def create_connection(self):
        try:
            myd_database = mysql.connector.connect(
                host=self.host,  # change it with hostname your that your provider gave you
                user=self.user,  # change it with username your that your provider gave you
                passwd=self.passwrd,  # so on
                database=self.database  # change it with  your own database
            )
            print("Si guul leh baanu kugu xirnay salka xogta.")  # message for successfull connection
            return myd_database
        except Exception as e:
            print(f"Error in create_connection method: {e}")
            return False

    def my_cursor(self):
        return self.create_connection().cursor()
    