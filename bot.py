import time
import praw
from config import *


def authenticate():
    print("Authenticating...")
    reddit = praw.Reddit('PortugalOnReddit', user_agent='PortugalOnReddit v0.1')
    print("Authenticated as {}".format(reddit.user.me()))
    return reddit


def process_submission(reddit, submission):
    title = submission.title  # Submission's title
    url = submission.url  # Submission's url
    xpost = "[{}] ".format(submission.subreddit.display_name)  # x-post string: [subreddit]
    comments_url = 'https://www.reddit.com' + submission.permalink  # link to submission's comment section

    new_post_title = xpost + title
    new_post_url = url
    new_post_text = "[Link to original post here]({})".format(comments_url)
    post_to = reddit.subreddit(SUBREDDIT_TO_POST)

    # new_post(post_to, new_post_title, new_post_url, new_post_text)
    print(new_post_title + ' - ' + url + '\n' + comments_url + '\n')


def start_subreddit(reddit):
    submissions_number = 0
    for expression in EXPRESSIONS_TO_MONITOR:
        search_query = 'title:' + expression

        for submission in reddit.subreddit(SUBREDDITS_TO_MONITOR).search(search_query, syntax='lucene', time_filter='year'):
            # pprint.pprint(vars(submission))
            if submission.score >= REQUIRED_SCORE:
                process_submission(reddit, submission)
                submissions_number += 1

    print(str(submissions_number) + ' submissions found')


def monitor(reddit):
    # for submission in reddit.subreddit(subreddits_to_monitor).stream.submissions():
    for submission in reddit.subreddit(SUBREDDITS_TO_MONITOR).hot(limit=10):
        # pprint.pprint(vars(submission))
        for expression in EXPRESSIONS_TO_MONITOR:
            if expression in submission.title.lower():
                process_submission(reddit, submission)

                # Save submission so it doesn't repeat

    # Sleep for 10 seconds
    time.sleep(10)


def new_post(subreddit, title, url, text):
    post = subreddit.submit(title, url=url)
    sticky_comment = post.reply(text).mod.distinguish(sticky=True)
    return sticky_comment


def main():
    # Authentication
    reddit = authenticate()

    # Setting up subreddit with some older posts
    # start_subreddit(reddit)

    # Monitor Reddit for new submissions
    while True:
        monitor(reddit)


if __name__ == '__main__':
    main()
