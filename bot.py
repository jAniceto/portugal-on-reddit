import praw

reddit = praw.Reddit('PortugalOnReddit', user_agent='PortugalOnReddit v0.1')

subreddit = reddit.subreddit('portugal')

for submission in subreddit.hot(limit=2):
    print(submission.title)  # Output: the submission's title
    print(vars(submission))

