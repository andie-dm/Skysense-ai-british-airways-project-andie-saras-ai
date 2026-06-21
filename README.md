# SkySense AI: British Airways Customer Satisfaction Prediction

### AI-Driven Predictive Customer Satisfaction and Personalized Experience Recommendations

**Author:** Andrea Delgado

---

# Project Overview

SkySense AI is an end-to-end machine learning application designed to analyze British Airways customer reviews, predict customer satisfaction, identify recurring complaint themes, and generate service improvement recommendations.

The project combines Natural Language Processing (NLP), machine learning, AWS cloud services, and interactive dashboards to help airline customer experience teams make data-driven decisions.

---

# Business Problem

British Airways receives thousands of customer reviews containing valuable information about passenger satisfaction and service quality.

Manually analyzing large volumes of customer feedback is time-consuming and makes it difficult to identify:

- Satisfaction trends
- Recurring customer complaints
- Service improvement opportunities
- Customer experience risks

SkySense AI automates this process using AI and cloud technologies.

---

# Solution Overview

The application:

1. Cleans and preprocesses customer reviews
2. Performs sentiment analysis using VADER
3. Creates satisfaction labels based on sentiment scores
4. Identifies complaint topics using LDA Topic Modeling
5. Trains a predictive satisfaction model using Amazon SageMaker Canvas (Autopilot)
6. Exposes predictions through AWS Lambda and API Gateway
7. Stores prediction results in DynamoDB
8. Displays predictions and recommendations through a Streamlit dashboard

---

# Dataset

Dataset:

British Airways Customer Reviews Dataset

The dataset contains:

- Review titles
- Customer review text
- Ratings
- Airline experience information

After preprocessing, the dataset includes:

- review_length
- sentiment_score
- satisfaction_label

---

# NLP Pipeline

## Text Preprocessing

The reviews were cleaned using:

- Lowercasing
- Punctuation removal
- Stopword removal
- Tokenization

---

## Sentiment Analysis

Sentiment analysis was performed using VADER.

Example:

Review:

> "My flight was delayed for five hours and customer service was rude."

Result:

- Sentiment Score: -0.91
- Satisfaction Label: Unsatisfied

---

# Topic Modeling (LDA)

Latent Dirichlet Allocation (LDA) was used to identify recurring complaint themes from customer reviews.

Example topics discovered:

### Topic 1 – Service Experience

- service
- crew
- british
- flight
- airways

### Topic 2 – Flight Delays

- delayed
- hours
- airport
- customer
- flight

### Topic 3 – Boarding and Staff

- boarding
- passengers
- staff
- service

### Topic 4 – Luggage Issues

- luggage
- delayed
- connecting
- flight

These topics help identify the most common customer pain points.

---

# Machine Learning Model

## Amazon SageMaker Canvas (Autopilot)

Amazon SageMaker Canvas was used to automatically train and evaluate a customer satisfaction prediction model.

### Target Variable

```
satisfaction_label
```

### Input Features

- sentiment_score
- review_length
- title
- reviews

### Model Performance

Accuracy:

```
99.61%
```

Most influential feature:

```
sentiment_score
```

This confirms that customer sentiment strongly predicts satisfaction outcomes.

---

# AWS Architecture

## Amazon S3

Stores datasets and model assets.

## Amazon SageMaker Canvas

Trains and evaluates the satisfaction prediction model.

## AWS Lambda

Runs serverless prediction logic.

## Amazon API Gateway

Provides a public API endpoint for real-time predictions.

## Amazon DynamoDB

Stores prediction history and recommendation results.

## AWS IAM

Manages secure service permissions.

---

# Prediction API

Example Request

```json
{
  "review": "My flight was delayed for five hours and customer service was rude."
}
```

Example Response

```json
{
  "satisfaction_prediction": "Unsatisfied",
  "complaint_topic": "Flight Delays",
  "recommendation": "Improve delay communication, provide proactive notifications, and offer compensation options."
}
```

---

# Streamlit Dashboard

The Streamlit dashboard allows users to:

- Enter customer reviews
- Generate predictions
- View complaint topics
- View recommendations
- Explore customer sentiment insights

---

# Amazon Bedrock Enhancement

Amazon Bedrock was evaluated as a future enhancement for generating dynamic recommendations using foundation models.

A Bedrock prompt was successfully designed and tested; however, account token quotas limited full deployment during development.

Future versions of the project can replace rule-based recommendations with AI-generated recommendations from Amazon Bedrock.

---

# Technologies Used

- Python
- Pandas
- Scikit-Learn
- NLTK
- VADER
- LDA Topic Modeling
- Streamlit
- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- Amazon SageMaker Canvas
- Amazon S3
- AWS IAM
- GitHub

---

# Project Deliverables

- NLP Pipeline
- Sentiment Analysis
- Topic Modeling (LDA)
- SageMaker Autopilot Model
- AWS Lambda API
- API Gateway Integration
- DynamoDB Storage
- Streamlit Dashboard
- Cloud Architecture
- GitHub Repository

---

# Future Improvements

- Amazon Bedrock integration
- Real-time airline feedback monitoring
- Multi-language sentiment analysis
- BERTopic implementation
- Advanced recommendation engine
- Production deployment on AWS

---