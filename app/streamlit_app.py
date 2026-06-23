import streamlit as st
import pandas as pd
import joblib
import nltk
import boto3
from nltk.sentiment import SentimentIntensityAnalyzer
import requests

nltk.download("vader_lexicon")

sia = SentimentIntensityAnalyzer()

st.set_page_config(
    page_title="SkySense AI",
    page_icon="✈️",
    layout="wide"
)

st.title("SkySense AI ✈️") 
st.subheader("AI-Driven Customer Satisfaction Analysis for British Airways Reviews")

st.write("""
This dashboard analyzes British Airways customer reviews using NLP, sentiment analysis,
machine learning, and recommendation logic to identify customer satisfaction patterns
and service improvement opportunities.
""")

df = pd.read_csv("data/british_airways_processed.csv")

# KPI Section

st.header("Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Reviews",
        len(df)
    )

with col2:
    st.metric(
        "Satisfied Reviews",
        (df["satisfaction_label"] == "Satisfied").sum()
    )

with col3:
    st.metric(
        "Unsatisfied Reviews",
        (df["satisfaction_label"] == "Unsatisfied").sum()
    )

with col4:
    st.metric(
        "Average Sentiment",
        round(df["sentiment_score"].mean(), 2)
    )


# Load processed dataset

st.header("Dataset Overview")

st.write("Number of Reviews:", len(df))

st.dataframe(df.head())

#Customer Satisfaction Distribution chart

st.header("Customer Satisfaction Distribution")

satisfaction_counts = df["satisfaction_label"].value_counts()

st.bar_chart(satisfaction_counts)

#Top Complaint categories chart

st.header("Top Complaint Categories")

topic_counts = {
    "Flight Delays": 355,
    "Customer Service": 165,
    "Seat Comfort": 60,
    "Other": 30,
    "Food Quality": 10,
    "Airport Experience": 8
}

#Complaint Category & Reviews table 

topic_df = pd.DataFrame(
    topic_counts.items(),
    columns=["Complaint Category", "Number of Reviews"]
)

topic_df = topic_df.sort_values(
    by="Number of Reviews",
    ascending=False
)


st.bar_chart(
    topic_df.set_index("Complaint Category")
)
st.dataframe(topic_df)

st.header("Recommended Actions")

recommendations = {
    "Flight Delays":
        "Improve delay communication, provide proactive notifications, and offer compensation options.",

    "Customer Service":
        "Increase staff training and improve customer support responsiveness.",

    "Seat Comfort":
        "Review seat quality and cabin maintenance programs.",

    "Food Quality":
        "Expand menu options and improve meal consistency.",

    "Airport Experience":
        "Improve check-in, boarding, and baggage handling processes."
}

for category, recommendation in recommendations.items():
    st.subheader(category)
    st.write(recommendation)

    st.header("Predict Customer Satisfaction")

user_review = st.text_area(
    "Enter a customer review:",
    height=150
)

if st.button("Analyze Review"):

    score = sia.polarity_scores(user_review)["compound"]

    if score >= 0.05:
        prediction = "Satisfied"
    elif score <= -0.05:
        prediction = "Unsatisfied"
    else:
        prediction = "Neutral"

    st.subheader("Prediction Results")

    st.write("Sentiment Score:", round(score, 3))
    st.write("Predicted Satisfaction:", prediction)

#Prediction AWS

st.header("Predict New Customer Review")

review_input = st.text_area(
    "Enter a customer review"
)

if st.button("Analyze with AWS API", key= "aws_analyze_review"):

    api_url = "https://roechxk1h8.execute-api.us-west-2.amazonaws.com/predict"

    payload = {
        "review": review_input
    }

    response = requests.post(
        api_url,
        json=payload
    )

    result = response.json()

    st.subheader("Prediction Result")

    st.write(
        f"**Satisfaction:** {result['satisfaction_prediction']}"
    )

    st.write(
        f"**Complaint Topic:** {result['complaint_topic']}"
    )

    st.write(
        f"**Recommendation:** {result['recommendation']}"
    )

   # import boto3
#import json

#bedrock = boto3.client(
   # "bedrock-runtime",
   # region_name="us-west-2"
#)

prompt = """
Generate three recommendations for improving airline customer satisfaction
for complaints related to flight delays.
"""

#response = bedrock.invoke_model(
   # modelId="amazon.nova-micro-v1:0",
   # body=json.dumps({
   #     "messages": [
    #        {
    #            "role": "user",
    #            "content": [{"text": prompt}]
   #         }
   #     ]
   # })
#)

#print(response)