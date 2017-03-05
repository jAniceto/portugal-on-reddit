import praw
import time
import pprint


# expressions_to_monitor = ["portugal", "portuguese", "porto", "lisboa", "oporto", "lisbon"]
expressions_to_monitor = ["portugal"]
subreddits_to_monitor = "all"
required_score = 100


def authenticate():
    print("Authenticating...")
    reddit = praw.Reddit('PortugalOnReddit', user_agent='PortugalOnReddit v0.1')
    print("Authenticated as {}".format(reddit.user.me()))
    return reddit


def run_bot(reddit):
    submissions_number = 0
    for expression in expressions_to_monitor:
        search_query = 'title:' + expression

        for submission in reddit.subreddit(subreddits_to_monitor).search(search_query, syntax='lucene', time_filter='week'):
            # pprint.pprint(vars(submission))
            if submission.score >= required_score:
                title = submission.title  # Output the submission's title
                print(title + '\n')
                submissions_number += 1

    print(submissions_number)


def main():
    reddit = authenticate()
    run_bot(reddit)


if __name__ == '__main__':
    main()
