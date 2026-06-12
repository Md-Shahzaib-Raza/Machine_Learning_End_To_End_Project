# Network Security Project — Phishing Detection ML Pipeline

## 📋 Project Overview

This is a **machine learning pipeline** designed to detect phishing attacks in network data. It provides an end-to-end workflow for data ingestion, validation, transformation, model training, evaluation, and batch predictions.

---

## 📁 File-by-File Breakdown

### Root Level Files

| File | Purpose |
|------|---------|
| **main.py** | Entry point to run the entire training pipeline. Orchestrates data ingestion → validation → transformation → model training. Execute with `python main.py`. |
| **app.py** | Optional application wrapper or demo script for running specific components or serving predictions. |
| **setup.py** | Python package setup configuration. Defines the `networksecurity` package metadata, dependencies, and installation instructions. |
| **requirements.txt** | List of all Python dependencies (e.g., scikit-learn, pandas, numpy). Install with `pip install -r requirements.txt`. |
| **Dockerfile** | Container configuration for running the pipeline in Docker. Build with `docker build -t netsec-phishing .` |
| **push_data.py** | Script to push/sync data to cloud storage (e.g., AWS S3). Used with the cloud sync utilities. |
| **README.md** | This file — project documentation and usage guide. |

---

## 📂 Directory Structure & Components

### `data_schema/`
- **schema.yaml**: Defines the expected structure and validation rules for the phishing dataset (column names, types, constraints). Used by the data validation component to ensure incoming data matches the schema.

### `Network_Data/`
- **phisingData.csv**: The training dataset containing network and phishing-related features. This CSV is loaded during the data ingestion phase.

### `networksecurity/` (Main Package)

#### `__init__.py`
- Makes `networksecurity` a Python package.

#### `cloud/`
- **s3_syncer.py**: Utility for syncing data and model artifacts to AWS S3. Handles authentication and file upload/download operations.

#### `components/` (Core Pipeline Components)
| Component | Responsibility |
|-----------|-----------------|
| **data_ingestion.py** | Loads raw data from `Network_Data/phisingData.csv`, performs initial checks, and splits it into train/test sets. Output is saved as artifacts. |
| **data_validation.py** | Validates that incoming data matches the schema defined in `data_schema/schema.yaml`. Checks for missing values, data types, and anomalies. |
| **data_transformation.py** | Preprocesses and transforms validated data (e.g., encoding, scaling, feature engineering). Prepares data for model training. |
| **model_trainer.py** | Trains machine learning models on the transformed data, performs hyperparameter tuning, and evaluates performance. Saves the best model. |

#### `constant/`
- **training_pipeline/**: Contains configuration constants (paths, hyperparameters, thresholds) used throughout the pipeline.

#### `entity/`
| File | Contains |
|------|----------|
| **artifact_entity.py** | Data classes that represent pipeline artifacts (ingested data paths, trained models, metrics, etc.). |
| **config_entity.py** | Data classes for pipeline configuration (input paths, output paths, model parameters). |

#### `exception/`
- **exception.py**: Custom exception classes for error handling specific to the phishing detection pipeline.

#### `logging/`
- **logger.py**: Sets up logging for the pipeline. Logs are written to files for debugging and monitoring pipeline runs.

#### `pipeline/` (Orchestration)
| Script | Purpose |
|--------|---------|
| **training_pipeline.py** | Main orchestrator that chains all components in order: ingestion → validation → transformation → training. Called by `main.py`. |
| **batch_prediction.py** | Loads a trained model and makes predictions on new/test data in batch. Outputs results to `prediction_output/output.csv`. |

#### `utils/` (Helper Utilities)
- **main_utils/utils.py**: General utilities (file I/O, data loading, common helper functions).
- **ml_utils/metric/classification_metric.py**: Calculates classification metrics (accuracy, precision, recall, F1-score, confusion matrix, etc.) for model evaluation.
- **ml_utils/model/estimator.py**: Model estimator wrapper — loads and wraps trained models for inference.

---

## 📊 Output Directories

| Directory | Contents |
|-----------|----------|
| **final_model/** | Stores the trained model artifact after successful training. |
| **prediction_output/** | Contains `output.csv` — batch prediction results from the `batch_prediction.py` script. |
| **valid_data/** | Contains `test.csv` — sample or validation test data used for batch predictions. |
| **notebooks/** | (Optional) Jupyter notebooks for exploration and experimentation. |
| **templates/** | Contains `table.html` — HTML template for displaying prediction results in a web view. |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip or conda

### Steps

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the training pipeline**
   ```bash
   python main.py
   ```
   This will execute:
   - Data ingestion (from `Network_Data/phisingData.csv`)
   - Data validation (against `data_schema/schema.yaml`)
   - Data transformation
   - Model training & evaluation
   - Saves trained model to `final_model/`

3. **Run batch predictions**
   ```bash
   python push_data.py
   ```
   or
   ```bash
   python -m networksecurity.pipeline.batch_prediction
   ```
   This loads the trained model and predicts on test data, outputting results to `prediction_output/output.csv`.

4. **(Optional) Run with Docker**
   ```bash
   docker build -t netsec-phishing .
   docker run -v %cd%/Network_Data:/app/Network_Data netsec-phishing python main.py
   ```

---

## 🔧 Configuration

Adjust pipeline behavior by modifying:
- **networksecurity/constant/training_pipeline/** — Model hyperparameters, paths, batch sizes
- **networksecurity/entity/config_entity.py** — Input/output paths, data split ratios
- **data_schema/schema.yaml** — Expected data schema for validation

---

## 📈 Data Flow

```
Network_Data/phisingData.csv
    ↓
data_ingestion.py (Load & split)
    ↓
data_validation.py (Validate against schema)
    ↓
data_transformation.py (Preprocess & transform)
    ↓
model_trainer.py (Train & evaluate)
    ↓
final_model/ (Save best model)
    ↓
batch_prediction.py (Make predictions on new data)
    ↓
prediction_output/output.csv (Store results)
```

---

## 📝 Logging & Monitoring

- Pipeline logs are written to `networksecurity/logging/` during execution.
- Check logs for debugging and tracking component progress.
- Predictions and model metrics are saved as artifacts in `final_model/` and `prediction_output/`.

---

## 🤝 Next Steps / Enhancements

- Add CLI arguments to `main.py` for selective pipeline stages
- Implement unit tests for each component
- Add hyperparameter grid search
- Deploy model as REST API using Flask/FastAPI
- Integrate with cloud services (S3, SageMaker, etc.)

---
