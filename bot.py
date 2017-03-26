import time
import os
import logging
import praw
from config import *


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)


def authenticate():
    logging.info("Authenticating...")
    reddit = praw.Reddit('OnReddit', user_agent=USER_AGENT)
    logging.info("Authenticated as {}".format(reddit.user.me()))
    return reddit


def process_submission(reddit, submission):
    title = submission.title  # Submission's title
    url = submission.url  # Submission's url
    xpost = "[r/{}] ".format(submission.subreddit.display_name)  # x-post string: [r/subreddit]
    comments_url = 'https://www.reddit.com' + submission.permalink  # link to submission's comment section

    new_post_title = xpost + title
    new_post_url = url
    new_post_text = "[Link to original post here]({})".format(comments_url)
    post_to = reddit.subreddit(SUBREDDIT_TO_POST)

    new_post(post_to, new_post_title, new_post_url, new_post_text)
    logging.info(new_post_title + ' - ' + comments_url)


def monitor(reddit, submissions_found):
    counter = 0
    for submission in reddit.subreddit(SUBREDDITS_TO_MONITOR).hot(limit=SEARCH_LIMIT):
        for expression in EXPRESSIONS_TO_MONITOR:
            if expression in submission.title.lower() and submission.id not in submissions_found:
                process_submission(reddit, submission)
                submissions_found.append(submission.id)
                counter += 1

                with open('submissions_processed.txt', 'a') as f:
                    f.write(submission.id + '\n')

    # Log results
    t = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    logging.info(t + ': ' + str(counter) + ' submission(s) found')

    # Sleep for a few seconds
    logging.info('Waiting...')
    time.sleep(WAIT_TIME*60)


def new_post(subreddit, title, url, text):
    post = subreddit.submit(title, url=url)
    sticky_comment = post.reply(text).mod.distinguish(sticky=True)
    return sticky_comment


def get_submissions_processed():
    if not os.path.isfile('submissions_processed.txt'):
        submissions_processed = []
    else:
        with open('submissions_processed.txt', 'r') as f:
            submissions_processed = f.read()
            submissions_processed = submissions_processed.split('\n')

    return submissions_processed


def main():
    print('Reddit bot running...')

    # Authentication
    reddit = authenticate()

    # Monitor Reddit for new submissions
    submissions_found = get_submissions_processed()
    while True:
        try:
            monitor(reddit, submissions_found)
        except Exception as e:
            logging.warning("Random exception occurred: {}".format(e))
            time.sleep(WAIT_TIME * 60)


if __name__ == '__main__':
    main()
