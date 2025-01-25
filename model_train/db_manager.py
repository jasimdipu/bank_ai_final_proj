import psycopg2
from psycopg2 import sql
from psycopg2.extras import DictCursor
from contextlib import contextmanager
import logging


class PostgresDBManager:
    def __init__(self, db_name="bank_admin_backend_db", user="postgres", password="bank@2024", host='localhost',
                 port=5432):
        """
        Initializes the PostgresDBManager with database connection details.
        dbname="bank_admin_backend_db",
        user="postgres",
        password="bank@2024",
        host="localhost",
        port="5432"
        """
        self.db_name = db_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None
        logging.basicConfig(level=logging.INFO)

    def connect(self):
        """
        Establishes a connection to the PostgreSQL database.
        """
        try:
            self.connection = psycopg2.connect(
                dbname=self.db_name,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            logging.info("Connected to the database successfully.")
        except psycopg2.Error as e:
            logging.error(f"Error connecting to database: {e}")
            raise

    def close(self):
        """
        Closes the database connection.
        """
        if self.connection:
            self.connection.close()
            logging.info("Database connection closed.")

    @contextmanager
    def cursor(self):
        """
        Provides a context manager for database operations.
        """
        if not self.connection:
            self.connect()
        cursor = self.connection.cursor(cursor_factory=DictCursor)
        try:
            yield cursor
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            logging.error(f"Error during database operation: {e}")
            raise
        finally:
            cursor.close()

    def execute_query(self, query, params=None):
        """
        Executes a single query with optional parameters.
        """
        with self.cursor() as cursor:
            cursor.execute(query, params)
            logging.info(f"Query executed: {cursor.query.decode()}")

    def fetch_one(self, query, params=None):
        """
        Executes a query and fetches a single result.
        """
        with self.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchone()
            logging.info(f"Query executed: {cursor.query.decode()}")
            return result

    def fetch_all(self, query, params=None):
        """
        Executes a query and fetches all results.
        """
        with self.cursor() as cursor:
            cursor.execute(query, params)
            results = cursor.fetchall()
            logging.info(f"Query executed: {cursor.query.decode()}")
            return results

    def insert(self, table, data):
        """
        Inserts data into a specified table.
        """
        columns = data.keys()
        values = tuple(data.values())
        query = sql.SQL("INSERT INTO {table} ({fields}) VALUES ({placeholders}) RETURNING id").format(
            table=sql.Identifier(table),
            fields=sql.SQL(", ").join(map(sql.Identifier, columns)),
            placeholders=sql.SQL(", ").join(sql.Placeholder() * len(values))
        )
        with self.cursor() as cursor:
            cursor.execute(query, values)
            inserted_id = cursor.fetchone()[0]
            logging.info(f"Inserted record with ID: {inserted_id}")
            return inserted_id
