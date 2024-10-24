import mysql.connector as mysqli
from mysql.connector import Error

connection = mysqli.connect(
  host = "localhost",
  username = "root",
  password = "",
  database = "puramas_api",
)

try:
  conn = connection.cursor()
except Error as e:
        print("Error while connecting to MySQL:", e)