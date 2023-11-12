import praw

# Initialize the Reddit API client
reddit = praw.Reddit(
    client_id="IuO2zGNIyvvSuweHpZbKkw",
    client_secret="jcj0-mFz3Xa6afskvw-r41WGvQaP-g",
    user_agent="SentimentAN/1.0 by /u/Awesomenesstw0",
)

# Define the subreddit you want to analyze
subreddit = reddit.subreddit("CryptoCurrency")

# Define a list of keywords related to sentiment
keywords = ["good", "bad", "awful"]
#"not good", "trash", "bullish","bearish"
# Initialize counters for sentiment analysis
sentiment_counts = {keyword: 0 for keyword in keywords}

# Search for posts and comments related to sentiment keywords
for submission in subreddit.search("sentiment", time_filter="week", limit=100):
    submission.comments.replace_more(limit=None)
    for comment in submission.comments:
        for keyword in keywords:
            if keyword in comment.body.lower():
                sentiment_counts[keyword] += 1

# Print sentiment analysis results
print("Sentiment Analysis Results:")
for keyword, count in sentiment_counts.items():
    print(f"{keyword.capitalize()}: {count}")
