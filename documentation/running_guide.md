## 📊 MapReducer Steps

#### Step 1: Clone the repository

```bash
    git clone https://github.com/Amayuru1999/tweets-sentiment-analysis.git
```

#### Step 1: Create a input file

```bash
    hadoop fs -mkdir /input
```

#### Step 2: Copy the dataset into input file

```bash
    hadoop fs -put ./Data/tweets_data.csv /input
```
![screenshot](./assets/Screenshot%20(245).png)

#### Step 3: Run the hashtag count job

```bash
    hadoop jar /home/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \ 
        -input /input/tweets_data.csv \
        -output /hashtag_count_output  \
        -mapper /home/hadoop/tweets-sentiment-analysis/hashtag_count_mapper.py \
        -reducer /home/hadoop/tweets-sentiment-analysis/hashtag_count_reducer.py
```
![screenshot](./assets/Screenshot%20(246).png)

#### Step 4: Run the hashtag sentiment analysis job

```bash
    hadoop jar /home/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
        -input /input/tweets_data.csv \
        -output /hashtag_sentiment_analysis_output  \
        -mapper /home/hadoop/tweets-sentiment-analysis/hashtag_sentiment_analysis_count_mapper.py \
        -reducer /home/hadoop/tweets-sentiment-analysis/hashtag_sentiment_analysis_count_reducer.py
```
![screenshot](./assets/Screenshot%20(249).png)

#### Step 5: Run the user sentiment analysis job

```bash
    hadoop jar /home/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
        -input /input/tweets_data.csv \
        -output /hashtag_sentiment_analysis_user_output  \
        -mapper /home/hadoop/tweets-sentiment-analysis/user_sentiment_analysis_count_mapper.py \
        -reducer /home/hadoop/tweets-sentiment-analysis/user_sentiment_analysis_count_reducer.py
```
![screenshot](./assets/Screenshot%20(251).png)

#### Hadoop File System UI

![screenshot](./assets/Screenshot%20(244).png)
![screenshot](./assets/Screenshot%20(253).png)
![screenshot](./assets/Screenshot%20(254).png)
![screenshot](./assets/Screenshot%20(255).png)
![screenshot](./assets/Screenshot%20(256).png)