# SkySense AI
### AI-Driven Predictive Customer Satisfaction Analysis for British Airways Reviews

By Andrea Delgado

---

## Project Overview

SkySense AI is a cloud-based customer satisfaction intelligence platform designed to analyze British Airways customer reviews using Natural Language Processing (NLP), Machine Learning, and AWS serverless services.

The system automatically:

- Analyzes customer sentiment
- Predicts customer satisfaction
- Identifies major complaint categories
- Extracts recurring themes using topic modeling
- Generates service improvement recommendations
- Stores prediction results in AWS DynamoDB
- Exposes predictions through AWS Lambda and API Gateway
- Visualizes insights through an interactive Streamlit dashboard

---

## Business Problem

British Airways receives thousands of customer reviews containing valuable feedback about flight experiences, customer service, delays, comfort, and operational issues.

Manually reviewing large amounts of customer feedback is time-consuming and inefficient.

This project uses AI and cloud technologies to automate customer satisfaction analysis and provide actionable insights that help improve customer experience.

---

## Solution Architecture

The solution combines NLP, machine learning, AWS serverless services, and dashboard visualization.

### Workflow

1. British Airways reviews dataset loaded from CSV
2. NLP preprocessing cleans customer reviews
3. VADER performs sentiment analysis
4. Satisfaction labels are generated
5. Random Forest model predicts customer satisfaction
6. LDA topic modeling identifies recurring complaint themes
7. AWS Lambda provides prediction services
8. API Gateway exposes prediction endpoints
9. DynamoDB stores prediction results
10. Streamlit dashboard visualizes insights and predictions

---

## Technologies Used

### Machine Learning & NLP

- Python
- Pandas
- Scikit-Learn
- NLTK
- VADER Sentiment Analysis
- Latent Dirichlet Allocation (LDA)

### Cloud Services

- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- AWS IAM

### Dashboard

- Streamlit
- Plotly
- Matplotlib

### Development

- GitHub
- GitHub Codespaces

---

## Features

### Sentiment Analysis

Customer reviews are analyzed using VADER sentiment scoring.

Outputs:

- Satisfied
- Neutral
- Unsatisfied

---

### Customer Satisfaction Prediction

A Random Forest classifier predicts customer satisfaction using sentiment features.

Model Performance:

- Accuracy: 100%

---

### Topic Modeling

LDA identifies major complaint categories found in negative reviews.

Example topics:

- Flight Delays
- Customer Service
- Seat Comfort
- Food Quality
- Airport Experience

---

### AWS Serverless Prediction API

Customers can submit a new review through:

AWS API Gateway → AWS Lambda → DynamoDB

The API returns:

- Satisfaction prediction
- Complaint category
- Improvement recommendation

---

### Interactive Dashboard

The Streamlit dashboard includes:

- Dataset overview
- KPI cards
- Satisfaction distribution
- Complaint category analysis
- Real-time prediction interface
- AWS API integration

---

## AWS Architecture

### Services Implemented

| Service | Purpose |
|----------|----------|
| Lambda | Prediction engine |
| API Gateway | REST API endpoint |
| DynamoDB | Store prediction results |
| IAM | Permissions management |

---

## Sample API Response

```json
{
  "satisfaction_prediction": "Unsatisfied",
  "complaint_topic": "Flight Delays",
  "recommendation": "Improve delay communication, provide proactive notifications, and offer compensation options."
}
```

---

## Project Structure

```
app/
 └── streamlit_app.py

data/
 ├── british_airways_reviews.csv
 └── british_airways_processed.csv

notebooks/
 └── 01_exploration.ipynb

src/
 ├── preprocess.py
 ├── sentiment.py
 ├── recommendations.py
 └── customer_satisfaction_model.pkl

architecture/
 └── architecture_diagram.md
```

---

## Future Improvements

- Amazon Bedrock integration
- SageMaker Autopilot model training
- Real-time airline monitoring
- Advanced recommendation generation
- Interactive executive dashboard

---

## Author

Andrea Delgado

Community Leader | Data Analytics & AI Practitioner | Silicon Slopes Latino Co-Chair
