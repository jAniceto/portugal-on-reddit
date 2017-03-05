import praw
import time


expressions_to_monitor = ["sporting"]


def authenticate():
    print("Authenticating...")
    reddit = praw.Reddit('PortugalOnReddit', user_agent='PortugalOnReddit v0.1')
    print("Authenticated as {}".format(reddit.user.me()))
    return reddit


def run_bot(reddit):
    for submission in reddit.subreddit('portugal').hot(limit=25):
        title = submission.title  # Output: the submission's title
        # print(title)

        for expression in expressions_to_monitor:
            if expression in title.lower():
                print(title)


    # Interval between runs
    time.sleep(10)


def main():
    reddit = authenticate()
    # while True:
    run_bot(reddit)


if __name__ == '__main__':
    main()
