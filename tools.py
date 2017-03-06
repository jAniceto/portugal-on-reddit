import praw


def authenticate():
    print("Authenticating...")
    reddit = praw.Reddit('PortugalOnReddit', user_agent='PortugalOnReddit v0.1')
    print("Authenticated as {}".format(reddit.user.me()))
    return reddit


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
