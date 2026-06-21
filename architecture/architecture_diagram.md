flowchart TD

A[British Airways Reviews Dataset]
--> B[Amazon S3]

B --> C[Python NLP Pipeline]

C --> D[Text Cleaning]
C --> E[VADER Sentiment Analysis]
C --> F[Feature Engineering]

E --> G[Sentiment Score]
F --> H[Review Length]

G --> I[Satisfaction Label]

I --> J[Amazon SageMaker Canvas Autopilot]

H --> J
G --> J

J --> K[Customer Satisfaction Prediction Model]

K --> L[AWS Lambda]

L --> M[Amazon API Gateway]

M --> N[Streamlit Dashboard]

L --> O[Amazon DynamoDB]

N --> P[Customer Satisfaction Prediction]
N --> Q[Complaint Topic Detection]
N --> R[Service Recommendations]

S[LDA Topic Modeling]
--> Q

R --> T[Future: Amazon Bedrock Recommendations]