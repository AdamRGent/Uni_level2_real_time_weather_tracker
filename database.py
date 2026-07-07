import sqlite3
from datetime import datetime

class WeatherDatabase:
    def __init__(self, db_path="weather_hub.db"):
        self.db_path = db_path
        self._create_tables()

    def _get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _create_tables(self):
        import os
        # Dynamically locate schema.sql relative to database.py
        base_dir = os.path.dirname(os.path.abspath(__file__))
        schema_path = os.path.join(base_dir, "schema.sql")
        
        with self._get_connection() as conn:
            with open(schema_path, "r") as f:
                conn.executescript(f.read())
            conn.commit()


    def get_cached_location(self, city_name):
        with self._get_connection() as conn:
            row = conn.execute(
                "SELECT * FROM location_cache WHERE LOWER(city_name) = LOWER(?)", 
                (city_name.strip(),)
            ).fetchone()
            return dict(row) if row else None

    def save_location(self, city_name, lat, lon):
        with self._get_connection() as conn:
            cursor = conn.execute(
                "INSERT OR IGNORE INTO location_cache (city_name, latitude, longitude) VALUES (?, ?, ?)",
                (city_name.strip().title(), lat, lon)
            )
            conn.commit()
            return cursor.lastrowid or self.get_cached_location(city_name)['id']

    def save_weather_reading(self, location_id, temp, condition, wind, humidity):
        with self._get_connection() as conn:
            cursor = conn.execute(
                """
                INSERT INTO weather_records 
                (location_id, temperature, condition_text, wind_speed, humidity) 
                VALUES (?, ?, ?, ?, ?)
                """,
                (location_id, temp, condition, wind, humidity)
            )
            return cursor.lastrowid
    
    def clear_location_history(self, city_name):
        """Wipes out all historical weather snapshots for a specific city name."""
        with self._get_connection() as conn:
            cursor = conn.execute(
                """
                DELETE FROM weather_records 
                WHERE location_id = (SELECT id FROM location_cache WHERE LOWER(city_name) = LOWER(?))
                """,
                (city_name.strip(),) # Fixed: Passed the city variable to fill the '?' spot!
            )
            return cursor.rowcount # Fixed: Returns the count of deleted logs (e.g., 5 logs deleted)


    def get_location_history(self, city_name, limit=5):
        with self._get_connection() as conn:
            rows = conn.execute(
                """
                SELECT weather_records.*, location_cache.city_name 
                FROM weather_records
                JOIN location_cache ON weather_records.location_id = location_cache.id
                WHERE LOWER(location_cache.city_name) = LOWER(?)
                ORDER BY weather_records.captured_at DESC 
                LIMIT ?
                """,
                (city_name.strip(), limit)
            ).fetchall()
            return [dict(r) for r in rows]
