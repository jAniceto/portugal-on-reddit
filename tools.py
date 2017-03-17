import praw
from bot import process_submission
from config import *


def authenticate():
    print("Authenticating...")
    reddit = praw.Reddit('OnReddit', user_agent='PortugalOnReddit v0.1')
    print("Authenticated as {}".format(reddit.user.me()))
    return reddit


def start_subreddit(reddit):
    submissions_number = 0
    for expression in EXPRESSIONS_TO_MONITOR:
        search_query = 'title:' + expression

        for submission in reddit.subreddit(SUBREDDITS_TO_MONITOR).search(search_query, syntax='lucene', time_filter='year'):
            if submission.score >= REQUIRED_SCORE:
                process_submission(reddit, submission)
                submissions_number += 1

    print(str(submissions_number) + ' submissions found')


def delete_posts(reddit):
    i = 0
    for submission in reddit.subreddit('PortugalOnReddit').hot(limit=100):
        if "PortugalOnReddit" not in submission.title:
            # print(submission.title)
            submission.delete()
            i += 1

    print(i)


if __name__ == '__main__':
    reddit = authenticate()
    delete_posts(reddit)
