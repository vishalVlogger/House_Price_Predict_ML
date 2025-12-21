import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_absolute_error
import pickle
import json

# Load data
df = pd.read_csv(f"Bengaluru_House_Data.csv")
print(f"Shape: {df.shape}")

# Clean data
df = df.dropna()
df["bhk"] = df["size"].str.extract("(\d+)").astype(float)
df["total_sqft"] = pd.to_numeric(df["total_sqft"], errors="coerce")
df = df.dropna(subset=["total_sqft", "bhk", "price", "location"])

# Get top locations (appearing more than 10 times)
location_counts = df["location"].value_counts()
top_locations = location_counts[location_counts > 10].index.tolist()
df = df[df["location"].isin(top_locations)]

# One-hot encode locations
location_dummies = pd.get_dummies(df["location"], prefix="loc")

# Select features
X = pd.concat([df[["total_sqft", "bath", "bhk"]], location_dummies], axis=1)
y = df["price"]

# Remove outliers
q1, q3 = y.quantile([0.25, 0.75])
iqr = q3 - q1
lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
mask = (y >= lower) & (y <= upper)
X, y = X[mask], y[mask]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Evaluate
y_pred = model.predict(X_test_scaled)
print(f"\nR² Score: {r2_score(y_test, y_pred):.3f}")
print(f"MAE: {mean_absolute_error(y_test, y_pred):.2f} lakhs")

# Save model, scaler, and locations
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)
with open("locations.json", "w") as f:
    json.dump(sorted(top_locations), f)
with open("columns.json", "w") as f:
    json.dump(X.columns.tolist(), f)

print("\n✅ Model saved! (model.pkl, scaler.pkl, locations.json, columns.json)")
print(f"Total locations: {len(top_locations)}")
print(f"Features: {X.columns.tolist()[:5]}...")
df.to_csv("Clean_House_Data.csv")
