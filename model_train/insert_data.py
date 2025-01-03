import psycopg2
import csv

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="bank_admin_backend_db",
    user="postgres",
    password="bank@2024",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Open the CSV file and copy data into the table
with open('Bank_Personal_Loan_Modelling.csv', 'r') as f:
    next(f)  # Skip the header row
    cur.copy_from(f, 'customer_data', sep=',')

# Commit the transaction and close the connection
conn.commit()
cur.close()
conn.close()
