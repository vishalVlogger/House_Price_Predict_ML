from django.shortcuts import render
from django.http import JsonResponse
import pickle
import numpy as np
import pandas as pd
import json
import os

# Load model once
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "model.pkl")
scaler_path = os.path.join(BASE_DIR, "scaler.pkl")
locations_path = os.path.join(BASE_DIR, "locations.json")
columns_path = os.path.join(BASE_DIR, "columns.json")

with open(model_path, "rb") as f:
    model = pickle.load(f)
with open(scaler_path, "rb") as f:
    scaler = pickle.load(f)
with open(locations_path, "r") as f:
    locations = json.load(f)
with open(columns_path, "r") as f:
    columns = json.load(f)


def home(request):
    print(f"DEBUG: Total locations loaded: {len(locations)}")
    print(f"DEBUG: First 5 locations: {locations[:5]}")
    return render(request, "predictor/home.html", {"locations": locations})


def predict(request):
    if request.method == "POST":
        try:
            # Get input
            sqft = float(request.POST.get("sqft"))
            bath = float(request.POST.get("bath"))
            bhk = float(request.POST.get("bhk"))
            location = request.POST.get("location")

            # Create feature array matching training columns
            features_dict = {col: 0 for col in columns}
            features_dict["total_sqft"] = sqft
            features_dict["bath"] = bath
            features_dict["bhk"] = bhk

            # Set location dummy variable
            loc_col = f"loc_{location}"
            if loc_col in features_dict:
                features_dict[loc_col] = 1

            # Convert to array in correct order
            features = np.array([[features_dict[col] for col in columns]])
            features_scaled = scaler.transform(features)

            # Predict
            price = model.predict(features_scaled)[0]

            # Format price in Indian currency style
            price_cr = price / 100  # Convert lakhs to crores if needed
            if price >= 100:
                price_formatted = f"₹{price_cr:.2f} Crores"
            else:
                price_formatted = f"₹{price:.2f} Lakhs"

            return JsonResponse(
                {
                    "success": True,
                    "price": round(price, 2),
                    "price_formatted": price_formatted,
                }
            )
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})

    return JsonResponse({"success": False, "error": "Invalid request"})
