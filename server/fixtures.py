"""Simple fixtures script to create the database and insert a sample Pet.

Run this from the `server/` directory with:

    python fixtures.py

This will create the SQLite database file `app.db` (if missing), create any
tables and insert one sample Pet if none exist. It's intended for quick local
testing without running Flask-Migrate commands.
"""

from app import app
from models import db, Pet


def create_sample_data():
    with app.app_context():
        # Create tables if they don't exist (safe for local dev)
        db.create_all()

        # Insert a sample pet only if the table is empty
        if Pet.query.first() is None:
            sample = Pet(name="Fido", species="Dog")
            db.session.add(sample)
            db.session.commit()
            print(f"Inserted sample pet: {sample}")
        else:
            print("Pets table already has data; no fixtures inserted.")


if __name__ == "__main__":
    create_sample_data()
