# Skysense-ai-british-airways-project-andie-saras-ai
AI-powered customer sentiment analysis and recommendation dashboard for British Airways reviews using Python, Streamlit, AWS Lambda, API Gateway, SageMaker, and Amazon Bedrock.

# Build with AWS

## AI-Driven Predictive Customer Satisfaction and Personalized Experience Recommendations

### By Andrea Delgado

---

# Project Proposal

This project will develop an AI-powered customer satisfaction analysis system for British Airways customer reviews. The application will use Natural Language Processing (NLP), machine learning, serverless AWS services, and generative AI to analyze airline passenger feedback, predict customer satisfaction levels, and generate personalized service improvement recommendations.

The system will process British Airways review data, identify whether customer feedback is positive, neutral, or negative, and use these insights to predict satisfaction trends. It will also identify common customer concerns such as flight delays, baggage issues, seat comfort, food quality, and customer service complaints. Based on these patterns, the application will generate recommendations that airline teams could use to improve customer experience.

The final solution will include a Streamlit dashboard, an AWS-based backend, API endpoints, and AI-generated recommendations using Amazon Bedrock.

---

# Architecture

The proposed architecture follows a cloud-based AI workflow using AWS services.

## High-Level Architecture Flow

British Airways Reviews Dataset
↓
Amazon S3 stores raw and processed data
↓
Python NLP pipeline cleans and analyzes review text
↓
Sentiment analysis creates satisfaction labels
↓
Amazon SageMaker trains a model to predict customer satisfaction
↓
AWS Lambda runs backend prediction logic
↓
Amazon API Gateway exposes the prediction API
↓
Amazon Bedrock generates personalized improvement recommendations
↓
Streamlit dashboard displays insights, predictions, and recommendations

## Architecture Explanation 

The dataset starts as a CSV file containing British Airways customer reviews. This file is stored in Amazon S3, which acts like a cloud folder for the project data.

Python is used to clean the review text and extract sentiment scores. These sentiment scores help determine whether a customer review sounds satisfied, neutral, or unsatisfied.

A machine learning model is then trained to predict satisfaction based on patterns in the review text. AWS Lambda and API Gateway are used to make the prediction logic available through an API. This means another application, such as the Streamlit dashboard, can send a review and receive a prediction.

Amazon Bedrock is used to generate natural-language recommendations. For example, if many negative reviews mention delays, Bedrock can suggest actions such as improving delay communication, offering proactive updates, or providing compensation options.

The final Streamlit dashboard will allow users to explore sentiment trends, test new review predictions, and view AI-generated service improvement recommendations.

---

# Problem Statement and Solution Overview

## Problem Statement

British Airways receives large amounts of customer feedback through online reviews. These reviews contain valuable information about passenger satisfaction, service quality, and recurring customer pain points. However, reading and analyzing hundreds or thousands of reviews manually is time-consuming and inefficient.

Without an automated system, it is difficult for airline teams to quickly identify major issues, understand customer sentiment trends, and decide which service areas need improvement.

## Solution Overview

This project proposes an AI-driven customer satisfaction and recommendation system that automatically analyzes British Airways customer reviews.

The solution will:

* Clean and process customer review text using NLP techniques.
* Analyze review sentiment to classify feedback as positive, neutral, or negative.
* Create customer satisfaction labels based on sentiment patterns.
* Train a predictive model to estimate customer satisfaction.
* Identify recurring complaint themes such as delays, baggage, staff service, and comfort.
* Use Amazon Bedrock to generate personalized improvement recommendations.
* Display results through a Streamlit dashboard.
* Use AWS services to demonstrate cloud infrastructure, serverless APIs, AI/ML integration, and generative AI capabilities.

This solution helps airline customer experience teams make faster, data-driven decisions from unstructured customer feedback.

---

# AWS Services to Be Used

## Amazon S3

Amazon S3 will be used to store the British Airways review dataset, processed data files, and model artifacts. In this project, S3 acts as the main cloud storage location.

## Amazon SageMaker

Amazon SageMaker will be used for the machine learning part of the project. The model will predict customer satisfaction levels based on sentiment scores and review features.

## AWS Lambda

AWS Lambda will be used to run backend logic without managing servers. A Lambda function will receive review text, process it, and return a satisfaction prediction or recommendation result.

## Amazon API Gateway

Amazon API Gateway will expose the Lambda function as an API endpoint. This allows the Streamlit dashboard to communicate with the backend.

## Amazon Bedrock

Amazon Bedrock will be used for generative AI recommendations. It will generate business-friendly recommendations based on customer complaints and sentiment analysis results.

## Amazon DynamoDB

Amazon DynamoDB may be used to store prediction results, review summaries, and generated recommendations. This allows the application to keep a record of analyzed feedback.

## AWS IAM

AWS IAM will manage access permissions between services. It helps ensure that Lambda, S3, SageMaker, DynamoDB, and Bedrock can communicate securely.

## Streamlit

Streamlit will be used as the user-facing dashboard. Although it is not an AWS service, it will display the final insights, predictions, visualizations, and recommendations.

---

# Expected Outcome

By the end of the project, the application will demonstrate how AI can help airline companies understand customer sentiment, predict satisfaction, and generate practical recommendations to improve passenger experience.

The final deliverables will include:

* GitHub repository with source code
* Architecture diagram
* Streamlit dashboard
* Sentiment analysis workflow
* Predictive customer satisfaction model
* AWS Lambda and API Gateway backend
* Amazon Bedrock recommendation feature
* Final presentation
* Demo video
* Project documentation
