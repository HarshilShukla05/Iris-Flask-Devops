from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import joblib
import pickle

# Load environment variables from .env file
load_dotenv()

PORT = int(os.getenv("PORT", 5000))
MODEL_FILE = os.getenv("MODEL_FILE", "model.pkl")
SPECIES_MAP_FILE = os.getenv("SPECIES_MAP_FILE", "species_map.pkl")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

with open(MODEL_FILE, "rb") as f:
    model = joblib.load(f)

with open(SPECIES_MAP_FILE, "rb") as f:
    species_map = joblib.load(f)

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "ML API is running!"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Validate input
    required_features = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    if not all(feature in data for feature in required_features):
        return jsonify({"error": f"Missing one of the required features: {required_features}"}), 400

    # Prepare feature list in correct order
    features = [data[feature] for feature in required_features]

    # Predict label
    prediction_label = model.predict([features])[0]
    predicted_species = species_map.get(prediction_label, "Unknown")

    return jsonify({
        "input": data,
        "predicted_species": predicted_species
    })

