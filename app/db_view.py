# Import the database connection
from app.db_con import Database


# class Database:
#     def __init__(self, host, user, passwrd, my_database):
#         self.host = host
#         self.user = user
#         self.passwrd = passwrd
#         self.database = my_database

#     def create_connection(self):
#         try:
#             myd_database = mysql.connector.connect(
#                 host=self.host,  # change it with hostname your that your provider gave you
#                 user=self.user,  # change it with username your that your provider gave you
#                 passwd=self.passwrd,  # so on
#                 database=self.database  # change it with  your own database
#             )
#             # message for successfull connection
#             print("Si guul leh baabu kugu xirnay salka xogta.")
#             return myd_database
#         except Exception as e:
#             print(e)
#             return False

#     def my_cursor(self):
#         return self.create_connection().cursor()


# mydb = Database('localhost', 'root', 'Arabka', 'TEST')
# myDatabase = mydb.create_connection()

# mycursor = myDatabase.cursor()

# Registration class


def generate_roll_number(self, last_id):
    prefix = "STD00"
    return f"{prefix}{last_id}"

class students:

    def __init__(self):
        self.mydb = Database('localhost', 'root', 'Arabka', 'TEST')
        self.myDatabase = self.mydb.create_connection()
        self.mycursor = self.myDatabase.cursor()
    # insertion method
    def insert_record(self, name, email, address, std_class):
        try:
            query = """ 
                    INSERT INTO studentstb(name, email, address, std_class) VALUES(%s, %s, %s, %s)
                    """
            self.mycursor.execute(query, (name, email, address, std_class))
            self.myDatabase.commit()
            last_id = self.mycursor.lastrowid
            print(f"Student with roll number: {last_id} registered successfully")
            # last_id = self.mycursor.lastrowid
            # roll_number = self.generate_roll_number(last_id)

            # update_query = "UPDATE studentstb SET id = %s WHERE id = %s"
            # self.mycursor.execute(update_query, (id, last_id))
            # self.myDatabase.commit()

            # print(f"Student with roll number: {roll_number} registered successfully")
        except Exception as e:
            print(f"Error in insertion db {e}")

    def display_records(self):
        try:
            query = "SELECT * FROM studentstb"
            self.mycursor.execute(query)
            result = self.mycursor.fetchall()

            records = []
            for row in result:
                record = {
                    'id': row[0],
                    'name': row[1],
                    'email': row[2],
                    'address': row[3],
                    'std_class': row[4]
                }
                records.append(record)

            return records

        except Exception as e:
            print(f"Error in displaying data from db: {e}")
            return None

    # Function to update an existing record in the database

    def update_record(self, id, name, email, address, std_class):
        try:
            query = """
                    UPDATE studentstb SET name = %s, email = %s, address = %s, std_class = %s WHERE id = %s
                    """
            # Execute the query with the values
            self.mycursor.execute(query, (name, email, address, std_class, id))
            # Commit the changes to the database
            self.myDatabase.commit()

            # Print debug information
            print("Query executed successfully.")
            print(self.mycursor.rowcount, "record updated.")

        except Exception as e:
            print(f"Error in update database method: {e}")


    # Function to delete a record from the database
    def delete_record(self, id):

        try:
            query = "DELETE FROM studentstb WHERE id = %s"
            # Execute the query with the value
            self.mycursor.execute(query, (id,))
            # Commit the changes to the database
            self.myDatabase.commit()
            # Print debug information
            print("Query executed successfully.")
            # Print a success message
            print(self.mycursor.rowcount, "record deleted.")
        except Exception as e:
            print(f"Error in delete database method: {e}")
