flowchart TD
    A[British Airways Reviews CSV] --> B[Amazon S3: Raw & Processed Data]
    B --> C[Python NLP Pipeline]
    C --> D[VADER Sentiment Analysis]
    D --> E[Processed Dataset with Sentiment Scores]
    E --> F[Random Forest Satisfaction Model]
    F --> G[Saved Model Artifact: customer_satisfaction_model.pkl]
    G --> H[Streamlit Dashboard]
    H --> I[Customer Satisfaction Prediction]
    H --> J[Complaint Category Insights]
    H --> K[Recommended Actions]

    K --> L[Planned: Amazon Bedrock Recommendations]
    I --> M[Planned: AWS Lambda + API Gateway]