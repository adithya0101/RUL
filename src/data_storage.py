import sqlite3

def save_predictions_to_db(db_path, predictions):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS rul_predictions (id INTEGER PRIMARY KEY, prediction REAL)''')
    cursor.executemany('INSERT INTO rul_predictions (prediction) VALUES (?)', [(p,) for p in predictions])
    conn.commit()
    conn.close()

def save_predictions_to_csv(filepath, predictions):
    pd.DataFrame(predictions, columns=['RUL Prediction']).to_csv(filepath, index=False)
