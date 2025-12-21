# 🏠 Bengaluru House Price Predictor

A full-stack machine learning web application that predicts house prices in Bengaluru using Linear Regression. Built with Django and scikit-learn, this project provides real-time price estimates based on property features and location.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/Django-4.0+-green.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

![House Price Predictor](https://github.com/vishalVlogger/House_Price_Predict_ML/blob/main/Screenshot%202025-12-18%20184747.png)

## ✨ Features

- 🎯 **Accurate Predictions**: ML model trained on 13,000+ Bengaluru property records
- 📍 **Location-Based Pricing**: 100+ locations with one-hot encoding for precise estimates
- ⚡ **Real-Time Results**: Instant predictions via AJAX (no page reload)
- 💰 **Smart Formatting**: Auto-converts lakhs to crores for better readability
- 🎨 **Modern UI**: Responsive design with gradient backgrounds and smooth animations
- 📊 **Data Pipeline**: Complete preprocessing with outlier removal and feature engineering

## 🚀 Demo

Enter property details (location, square feet, BHK, bathrooms) and get instant price estimates:

```
Input: 3 BHK, 1500 sq.ft, Whitefield, 2 bathrooms
Output: ₹1.25 Crores
```

## 🛠️ Tech Stack

**Backend:**
- Django 4.0+
- Python 3.8+
- scikit-learn
- pandas & NumPy

**Frontend:**
- HTML5/CSS3
- Vanilla JavaScript (Fetch API)
- Responsive Design

**Machine Learning:**
- Linear Regression
- StandardScaler normalization
- One-hot encoding for locations
- Feature engineering (price-per-sqft)

## 📦 Installation

### Prerequisites
```bash
Python 3.8+
pip
```

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/bengaluru-house-price-predictor.git
cd bengaluru-house-price-predictor
```

2. **Install dependencies**
```bash
pip install django scikit-learn pandas numpy kagglehub
```

3. **Train the ML model**
```bash
python train_model.py
```
This will download the dataset and generate:
- `model.pkl` - Trained Linear Regression model
- `scaler.pkl` - Feature scaler
- `locations.json` - List of valid locations
- `columns.json` - Feature column names

4. **Set up Django**
```bash
python manage.py migrate
```

5. **Run the server**
```bash
python manage.py runserver
```

6. **Open your browser**
```
http://127.0.0.1:8000/
```

## 📁 Project Structure

```
bengaluru-house-price-predictor/
├── train_model.py          # ML training script
├── model.pkl               # Trained model (generated)
├── scaler.pkl              # Feature scaler (generated)
├── locations.json          # Available locations (generated)
├── columns.json            # Feature columns (generated)
├── manage.py               # Django management script
├── config/
│   ├── settings.py         # Django settings
│   └── urls.py             # Main URL configuration
├── predictor/
│   ├── views.py            # View logic & ML inference
│   ├── urls.py             # App URLs
│   └── models.py           # Django models
├── static/
│   ├── css/
│   │   └── style.css       # style css
│   └── js/
│       └── script.js       # js 
├── templates/
│   └── predictor/
│       └── home.html       # Frontend interface
└── README.md
```

## 🧠 Machine Learning Pipeline

### 1. Data Preprocessing
- Load Bengaluru house price dataset from Kaggle
- Handle missing values and data type conversions
- Extract BHK from the size column
- Filter locations with 10+ data points

### 2. Feature Engineering
- Calculate price-per-sqft
- One-hot encode location data
- Remove outliers using the IQR method

### 3. Model Training
- Split data (80-20 train-test)
- StandardScaler normalization
- Linear Regression model
- Evaluation: R² score & MAE

### 4. Model Persistence
- Save model, scaler, and metadata using pickle
- Load once at Django startup for fast inference

## 📊 Model Performance

```
R² Score: ~0.85
Mean Absolute Error: ~15-20 Lakhs
Training Samples: 10,000+
Features: 100+ (location dummies + numerical features)
```

## 🎯 API Endpoints

### GET `/`
Returns the home page with the prediction form

### POST `/predict/`
Predicts house prices based on input features

**Request Body:**
```json
{
  "location": "Whitefield",
  "sqft": "1500",
  "bhk": "3",
  "bath": "2"
}
```

**Response:**
```json
{
  "success": true,
  "price": 125.45,
  "price_formatted": "₹1.25 Crores"
}
```

## 🎨 UI Features

- **Gradient Background**: Eye-catching purple gradient
- **Form Validation**: Client-side validation for all inputs
- **Loading States**: Visual feedback during prediction
- **Error Handling**: User-friendly error messages
- **Responsive**: Works on desktop, tablet, and mobile

## 🔮 Future Enhancements

- [ ] Add more ML models (Random Forest, XGBoost)
- [ ] Interactive price trends chart
- [ ] Property comparison feature
- [ ] User authentication & saved searches
- [ ] RESTful API with authentication
- [ ] Docker containerization
- [ ] Deploy to cloud (AWS/Heroku)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Vishal Patil**
- GitHub: [vishalVlogger](https://github.com/vishalVlogger)
- LinkedIn: [Vishal-Patil03](https://linkedin.com/in/vishal-patil03)

## 🙏 Acknowledgments

- Dataset: [Bengaluru House Price Data](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data) on Kaggle
- Inspired by real estate price prediction challenges
- Built with ❤️ using Django and scikit-learn

## 📧 Contact

If you have any questions or feedback, please open an issue or email me.

---
