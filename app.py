from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import pandas as pd
import plotly.express as px

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from news_api import fetch_news
from langchain_config import create_news_summary

st.set_page_config(
    page_title="News Research Dashboard",
    page_icon="📰",
    layout="wide"
)

analyzer = SentimentIntensityAnalyzer()

st.title("📰 Advanced News Research Tool")
st.subheader("News Analysis, Sentiment Analysis and Dashboard")

st.divider()

query = st.text_input(
    "Enter your News Query",
    placeholder="Example: Artificial Intelligence"
)

if st.button("Search News", type="primary"):

    if not query.strip():
        st.warning("Please enter a search query.")

    else:
        try:
            with st.spinner("Fetching news articles..."):

                articles = fetch_news(query)

                if not articles:
                    st.warning("No news articles found.")
                    st.stop()

                summary = create_news_summary(query, articles)

                results = []

                for article in articles:

                    title = article.get("title") or "No Title"
                    description = article.get("description") or ""

                    text = title + " " + description

                    score = analyzer.polarity_scores(text)["compound"]

                    if score >= 0.05:
                        sentiment = "Positive"
                    elif score <= -0.05:
                        sentiment = "Negative"
                    else:
                        sentiment = "Neutral"

                    results.append({
                        "Title": title,
                        "Description": description,
                        "Source": article.get("source") or "Unknown",
                        "Sentiment": sentiment,
                        "Sentiment Score": score,
                        "URL": article.get("url") or ""
                    })

                df = pd.DataFrame(results)

            st.success("News analysis completed successfully!")

            # Dashboard metrics
            st.header("📊 News Research Dashboard")

            col1, col2, col3, col4 = st.columns(4)

            col1.metric("Total News", len(df))

            col2.metric(
                "Positive News",
                int((df["Sentiment"] == "Positive").sum())
            )

            col3.metric(
                "Negative News",
                int((df["Sentiment"] == "Negative").sum())
            )

            col4.metric(
                "Neutral News",
                int((df["Sentiment"] == "Neutral").sum())
            )

            st.divider()

            # Sentiment chart
            st.subheader("📈 Sentiment Distribution")

            sentiment_counts = df["Sentiment"].value_counts()

            fig1 = px.pie(
                values=sentiment_counts.values,
                names=sentiment_counts.index,
                title="News Sentiment Analysis",
                hole=0.4
            )

            st.plotly_chart(fig1, use_container_width=True)

            # Source chart
            st.subheader("📰 News Source Analysis")

            source_counts = df["Source"].value_counts()

            fig2 = px.bar(
                x=source_counts.index,
                y=source_counts.values,
                labels={
                    "x": "News Source",
                    "y": "Number of Articles"
                },
                title="Articles by News Source"
            )

            st.plotly_chart(fig2, use_container_width=True)

            st.divider()

            # Summary
            st.header("📝 News Summary")
            st.markdown(summary)

            st.divider()

            # News articles
            st.header("📚 News Articles")

            for _, row in df.iterrows():

                with st.expander(row["Title"]):

                    st.write(row["Description"])

                    st.write("Source:", row["Source"])

                    st.write("Sentiment:", row["Sentiment"])

                    st.write(
                        "Sentiment Score:",
                        round(row["Sentiment Score"], 3)
                    )

                    if row["URL"]:
                        st.markdown(
                            f"[Read Full Article]({row['URL']})"
                        )

            # Download report
            st.divider()

            st.subheader("📥 Download Report")

            csv = df.to_csv(index=False).encode("utf-8")

            st.download_button(
                "Download News Analysis CSV",
                data=csv,
                file_name="news_analysis.csv",
                mime="text/csv"
            )

        except Exception as e:
            st.error(f"Something went wrong: {e}")

st.divider()

st.caption(
    "News Research Tool | Python | Streamlit | NewsAPI | VADER"
)