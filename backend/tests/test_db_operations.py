# test_db_connection.py

import unittest
from sqlalchemy import create_engine

# Use python-dotenv to load the environment variables
from dotenv import load_dotenv
import os


class TestDBConnection(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Load environment variables from .env file
        load_dotenv()

        # Fetch the test database path from environment variable
        cls.test_database_path = os.getenv("TEST_DATABASE_PATH")
        if not cls.test_database_path:
            raise ValueError("TEST_DATABASE_PATH environment variable is not set. Please define it in the .env file.")

    def test_connection(self):
        engine = create_engine(f"sqlite:///{self.test_database_path}")
        connection = engine.connect()
        self.assertIsNotNone(connection)
        connection.close()


if __name__ == "__main__":
    unittest.main()
