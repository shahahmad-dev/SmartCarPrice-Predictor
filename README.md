
# 🚗 SmartCarPrice-Predictor

**SmartCarPrice-Predictor** is a machine learning web application that predicts the **estimated selling price of a car** based on key vehicle details such as purchase year, present price, kilometers driven, and number of previous owners.

The project uses a **Random Forest Regression model** and an interactive **Streamlit web interface** to provide fast and user-friendly predictions.

---

# 📌 Project Overview

Buying or selling a car often requires estimating its market value.
This project demonstrates how **machine learning can be used to predict car resale prices** based on historical data.

Users input vehicle details, and the system predicts the **expected selling price in lakhs** using a trained ML model.

---

# ⚙️ Features

* 🚗 Predict car selling price using Machine Learning
* 🧠 Random Forest Regression model
* 📊 Interactive Streamlit interface
* 📋 Prediction summary table
* 📈 Price comparison visualization
* 📂 Dataset preview inside the app

---

# 🧠 Machine Learning Model

**Algorithm Used:** Random Forest Regressor

**Input Features:**

* Year of Purchase
* Present Price
* Kilometers Driven
* Number of Owners

**Target Variable:**

* Selling Price

Random Forest is used because it performs well with **non-linear relationships and reduces overfitting**.

---

# 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Pandas**
* **NumPy**
* **Scikit-learn**

---

# 📂 Project Structure

```
SmartCarPrice-Predictor
│
├── app.py
├── car data.csv
├── README.md
└── requirements.txt
```

---

# 🚀 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/shahahmad-dev/SmartCarPrice-Predictor.git
cd SmartCarPrice-Predictor
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 📊 Example Inputs

Users provide:

* Car Name
* Year of Purchase
* Fuel Type
* Transmission
* Present Price (in lakhs)
* Kilometers Driven
* Number of Previous Owners

The model then predicts the **estimated selling price**.

---

# 📈 Output

The app displays:

* 💰 Estimated selling price
* 📋 Prediction summary table
* 📊 Bar chart comparing present price vs predicted price

---

# 🎯 Learning Outcomes

This project demonstrates:

* Building **Machine Learning regression models**
* Creating **interactive ML web applications**
* Using **Streamlit for deployment**
* Data preprocessing and model training

---

# 👨‍💻 Author

**Shah Ahmad Noorani**
Data Science Learner

🔗 LinkedIn
🔗 GitHub
🔗 Kaggle



