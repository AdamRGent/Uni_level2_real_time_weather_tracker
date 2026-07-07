CREATE TABLE IF NOT EXISTS location_cache (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city_name TEXT NOT NULL UNIQUE,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS weather_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    location_id INTEGER NOT NULL,
    temperature REAL NOT NULL,
    condition_text TEXT NOT NULL,
    wind_speed REAL NOT NULL,
    humidity INTEGER,
    captured_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(location_id) REFERENCES location_cache(id) ON DELETE CASCADE
);
