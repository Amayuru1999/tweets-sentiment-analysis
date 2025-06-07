## 📊 Dataset Description

### Dataset Name: Twitter Sentiment Analysis Dataset

This dataset contains a large collection of tweets labeled with sentiment (positive, negative, or neutral). Each row represents a tweet and its corresponding sentiment label, allowing us to perform large-scale sentiment-based analytics.

### 📁 Dataset Source

The dataset was obtained from a public GitHub repository:
https://github.com/Amayuru1999/tweets-sentiment-analysis

This dataset is based on a widely-used version of the Sentiment140 dataset, which includes over 100,000 labeled tweets.

### 🧠 Why This Dataset?

This dataset is well-suited for MapReduce tasks due to:

- Large volume of text (ideal for distributed word-level processing)
- Structured format (CSV with clear sentiment labels)
- Real-world relevance (sentiment analysis is a common NLP application)

### 🛠️ Planned MapReduce Task

We plan to implement a MapReduce job to compute the **frequency of words** grouped by sentiment (positive, negative, neutral). This can help us identify:

- Most common positive words
- Most common negative words
- Neutral expressions

This can be extended to:

- Hashtag frequency per sentiment
- Average tweet length per sentiment
- Time-based sentiment trends (if timestamp is included)

### 📦 Hadoop Installation

Follow this guide to install Apache Hadoop on Ubuntu system

- [Hadoop Installation Guide](https://medium.com/@abhikdey06/apache-hadoop-3-3-6-installation-on-ubuntu-22-04-14516bceec85)
