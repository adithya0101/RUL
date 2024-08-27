from src.data_preprocessing import load_data, preprocess_data
from src.feature_engineering import feature_engineering
from src.model_training import train_model
from src.model_evaluation import evaluate_model
from src.data_storage import save_predictions_to_db, save_predictions_to_csv

# Load and preprocess data
df = load_data('data/machinery_rul_data.csv')
X_train, X_test, y_train, y_test = preprocess_data(df)

# Feature engineering
X_train_scaled, X_test_scaled = feature_engineering(X_train, X_test)

# Train model
model = train_model(X_train_scaled, y_train)

# Evaluate model
mae, rmse, r2, y_pred = evaluate_model(model, X_test_scaled, y_test)
print(f"MAE: {mae}, RMSE: {rmse}, R²: {r2}")

# Save predictions
save_predictions_to_db('data/rul_predictions.db', y_pred)
save_predictions_to_csv('data/rul_predictions.csv', y_pred)
