# Chennai Housing Sale Price Predictor

This is a web-based application that predicts house sale prices in Chennai using a machine learning model. The user can select various features of a property, and the application provides a real-time price estimation. The project is built using Flask for the backend and a combination of HTML, CSS, and JavaScript for the front-end.

---

### Features

- **Interactive User Interface**: A clean and easy-to-use form allows users to input property details.
- **Machine Learning Backend**: A pre-trained Random Forest Regressor model handles the price prediction.
- **One-Hot Encoding**: The application correctly processes categorical features (like `AREA` and `MZZONE`) to match the format required by the model.
- **Real-time Predictions**: The frontend uses asynchronous JavaScript calls to communicate with the Flask API, providing instant predictions without a full page reload.

---

### Project Structure

The project follows a standard Flask directory layout:

chennai_housing_sale_price_predictor/
├── app.py                      # Main Flask application and prediction logic
├── random_forest_regressor_model.joblib # The trained machine learning model
├── model_features.joblib       # The list of feature names used by the model
├── templates/
│   └── index.html              # The main HTML file for the user interface
└── static/
├── style.css               # CSS for the application's styling
└── script.js               # JavaScript for frontend interactivity

---

### Setup and Installation

Follow these steps to get the project running on your local machine.

Markdown

# Chennai Housing Sale Price Predictor

This is a web-based application that predicts house sale prices in Chennai using a machine learning model. The user can select various features of a property, and the application provides a real-time price estimation. The project is built using Flask for the backend and a combination of HTML, CSS, and JavaScript for the front-end.

---

### Features

- **Interactive User Interface**: A clean and easy-to-use form allows users to input property details.
- **Machine Learning Backend**: A pre-trained Random Forest Regressor model handles the price prediction.
- **One-Hot Encoding**: The application correctly processes categorical features (like `AREA` and `MZZONE`) to match the format required by the model.
- **Real-time Predictions**: The frontend uses asynchronous JavaScript calls to communicate with the Flask API, providing instant predictions without a full page reload.

---

### Project Structure

The project follows a standard Flask directory layout:

chennai_housing_sale_price_predictor/
├── app.py                      # Main Flask application and prediction logic
├── random_forest_regressor_model.joblib # The trained machine learning model
├── model_features.joblib       # The list of feature names used by the model
├── templates/
│   └── index.html              # The main HTML file for the user interface
└── static/
├── style.css               # CSS for the application's styling
└── script.js               # JavaScript for frontend interactivity


---

### Setup and Installation

Follow these steps to get the project running on your local machine.

#### 1. Clone the Repository

Clone this repository to your local machine using git:

```bash
git clone <your-repository-url>
cd chennai_housing_sale_price_predictor
```
---

#### 2. Set Up a Virtual Environment
It is highly recommended to use a virtual environment to manage dependencies.

On macOS/Linux:

```bash

python3 -m venv venv
source venv/bin/activate

```

On Windows:

```PowerShell

python -m venv venv
.\venv\Scripts\Activate.ps1
```
---

#### 3. Install Dependencies
Install the required Python libraries using pip:

```bash

pip install Flask scikit-learn joblib numpy pandas
```

---

#### 4. Add Your Model Files

Ensure that your trained model files are in the root directory of the project:
```
random_forest_regressor_model.joblib
``` ```
model_features.joblib
```
---

#### 5. Run the Application
Start the Flask development server from your terminal:
```
flask run
```
The application will be accessible at ``` http://127.0.0.1:5000. ```Open this URL in your web browser to start predicting house prices.

