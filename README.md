## Student marks predictor

### Project Description
This project is an end-to-end machine learning pipeline to predict students' math scores based on various features such as gender, race/ethnicity, parental level of education, lunch type, test preparation course, reading score, and writing score. The pipeline includes data ingestion, data transformation, model training with hyperparameter tuning, and model evaluation.

### Dataset
The dataset used is a student performance dataset containing the following features:
- gender
- race_ethnicity
- parental_level_of_education
- lunch
- test_preparation_course
- math_score (target variable)
- reading_score
- writing_score

The dataset is stored in `Notebook/Data/stud.csv`.

### Project Structure
- `src/components/`: Contains modules for data ingestion, data transformation, and model training.
- `src/pipeline/`: Contains the training pipeline (`train_pipeline.py`) and prediction pipeline (`predict_pipeline.py`).
- `artifacts/`: Stores processed data, trained model (`model.pkl`), and preprocessor (`preprocessor.pkl`).
- `Notebook/`: Jupyter notebooks for exploratory data analysis and model training.
- `templates/`: Contains HTML files for the web application.
- `app.py`: A Flask web application for serving the model and making predictions.
- `requirements.txt`: Python dependencies.
- `setup.py`: Setup script for the project.
- `README.md`: Project documentation.

### Installation
1. Create a virtual environment:
```
conda create -n stud_perf python=3.8 -y
conda activate stud_perf
```

2. Install the required dependencies:
Install the required dependencies using:
```
pip install -r requirements.txt
```

### Usage
1. Run the data ingestion, transformation, and model training pipeline by executing the training pipeline script:
```bash
python src/pipeline/train_pipeline.py
```
2. The trained model and preprocessor will be saved in the `artifacts/` directory.

### Model Training
The project trains multiple regression models including Random Forest, Decision Tree, Gradient Boosting, Linear Regression, K-Neighbors, XGBoost, CatBoost, and AdaBoost. Hyperparameter tuning is performed using GridSearchCV to select the best model based on R2 score.

### Artifacts
- `artifacts/train.csv` and `artifacts/test.csv`: Train and test splits of the dataset.
- `artifacts/model.pkl`: Serialized best trained model.
- `artifacts/preprocessor.pkl`: Serialized data preprocessing pipeline.

### Author
Anish Goyal
Email: goyalanish1708@gmail.com
