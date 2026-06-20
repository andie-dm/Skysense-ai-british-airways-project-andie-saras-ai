flowchart TD

A[British Airways Reviews CSV]
--> B[Amazon S3]

B --> C[Python NLP Pipeline]

C --> D[VADER Sentiment Analysis]

D --> E[Processed Dataset]

E --> F[Random Forest Model Training]

F --> G[customer_satisfaction_model.pkl]

G --> H[Streamlit Dashboard]

H --> I[API Gateway]

I --> J[AWS Lambda]

J --> K[DynamoDB]

J --> L[Customer Satisfaction Prediction]

J --> M[Complaint Topic Detection]

J --> N[Recommendation Engine]


*End-to-End Cloud Architecture:*

User
  ↓
Streamlit Dashboard
  ↓
API Gateway
  ↓
AWS Lambda
  ↓
Sentiment Analysis
Complaint Classification
Recommendation Engine
  ↓
DynamoDB
