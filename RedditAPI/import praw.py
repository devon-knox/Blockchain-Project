import praw

# Initialize the Reddit API client
reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="YOUR_USER_AGENT",
)

# Define the subreddit you want to analyze
subreddit = reddit.subreddit("crypto")

# Define a list of keywords related to sentiment
keywords = ["positive", "negative", "neutral"]

# Initialize counters for sentiment analysis
sentiment_counts = {keyword: 0 for keyword in keywords}

# Search for posts and comments related to sentiment keywords
for submission in subreddit.search("sentiment", limit=10):
    submission.comments.replace_more(limit=None)
    for comment in submission.comments:
        for keyword in keywords:
            if keyword in comment.body.lower():
                sentiment_counts[keyword] += 1

# Print sentiment analysis results
print("Sentiment Analysis Results:")
for keyword, count in sentiment_counts.items():
    print(f"{keyword.capitalize()}: {count}")
