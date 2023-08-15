import mysql.connector
import json

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
            print("Si guul leh baabu kugu xirnay salka xogta.")  # message for successfull connection
            return myd_database
        except Exception as e:
            print(e)
            return False

    def my_cursor(self):
        return self.create_connection().cursor()


mydb = Database('localhost', 'root', 'Arabka', 'CRUD')
myDatabase = mydb.create_connection()

mycursor = myDatabase.cursor()

# Registration class


class Registration:
    # insertion method
    def insert_record(self, user_name, email, user_pass):
        try:
            mydb = Database('localhost', 'root', 'Arabka', 'TEST')
            myDatabase = mydb.create_connection()

            mycursor = myDatabase.cursor()

            query = """ 
                    INSERT INTO users(user_name, email, user_pass) VALUES(%s, %s, %s)
                    """
            mycursor.execute(query, (user_name, email, user_pass))
            myDatabase.commit()
            print(mycursor.rowcount, "record inserted.")
        except Exception as e:
            print(f"Error in insertion db {e}")

    def display_records(self):
        try:
            mydb = Database('localhost', 'root', 'Arabka', 'TEST')
            myDatabase = mydb.create_connection()

            mycursor = myDatabase.cursor()

            query = "SELECT * FROM users"
            mycursor.execute(query)
            result = mycursor.fetchall()

            records = []
            for row in result:
                record = {
                    'user_id': row[0],
                    'user_name': row[1],
                    'email': row[2],
                    'user_pass': row[3]
                }
                records.append(record)
            
            return records

        except Exception as e:
            print(f"Error in displaying data from db: {e}")
            return None





    # Function to update an existing record in the database
    def update_record(self, user_id, user_name, email, user_pass):
        try:
            mydb = Database('localhost', 'root', 'Arabka', 'TEST')
            myDatabase = mydb.create_connection()

            mycursor = myDatabase.cursor()
            # Prepare the SQL query
            query = """
                    UPDATE users SET user_name = %s, email = %s, user_pass = %s WHERE user_id = %s
                    """
            # Execute the query with the values
            mycursor.execute(query, (user_id, user_name, email, user_pass))
            # Commit the changes to the database
            myDatabase.commit()
            # Print a success message
            print(mycursor.rowcount, "record updated.")

        except Exception as e:
            print(f"Error in update database: {e}")

    # Function to delete a record from the database
    def delete_record(name, user_id):
        # Prepare the SQL query
        query = "DELETE FROM users WHERE user_id = %s"
        # Execute the query with the value
        mycursor.execute(query, (user_id))
        # Commit the changes to the database
        myDatabase.commit()
        # Print a success message
        print(mycursor.rowcount, "record deleted.")