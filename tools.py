import praw
from bot import process_submission
from config import *
import sys
from collections import defaultdict
import pprint
import matplotlib.pyplot as plt


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


def stats(reddit):
    source_subreddit_list = []
    for submission in reddit.subreddit('PortugalOnReddit').hot(limit=None):
        title = submission.title

        try:
            source_subreddit = title.split('[')[1].split(']')[0]
        except IndexError:
            continue

        if source_subreddit[0:2] == 'r/':
            source_subreddit = source_subreddit[2:]

        source_subreddit_list.append(source_subreddit)

    appearances = defaultdict(int)

    for curr in source_subreddit_list:
            appearances[curr] += 1

    # Treat data
    appearances_summary = {'others': 0}
    for subreddit_key in appearances:
        if appearances[subreddit_key] == 1:
            appearances_summary['others'] += 1
        else:
            appearances_summary[subreddit_key] = appearances[subreddit_key]

    pprint.pprint(appearances_summary)
    appearances = appearances_summary  # use treated data for stats

    # PLOTS
    # Bar chart
    plt.figure(1)
    plt.bar(range(len(appearances)), appearances.values(), align='center')
    plt.xticks(range(len(appearances)), list(appearances.keys()), rotation='vertical')
    plt.ylabel('Number of submissions')
    plt.title('Mentions per subreddit')

    # Horizontal bar chart
    plt.figure(2)
    plt.barh(range(len(appearances)), appearances.values(), align='center', color='green')
    plt.yticks(range(len(appearances)), list(appearances.keys()))
    plt.xlabel('Number of submissions')
    plt.title('Mentions per subreddit')

    # Pie chart
    plt.figure(3)
    plt.pie(list(appearances.values()), labels=list(appearances.keys()), autopct='%1.1f%%')

    plt.show()

try:
    tool = sys.argv[1]
except IndexError:
    tool = "stats"

reddit = authenticate()
if tool == "start":
    start_subreddit(reddit)
elif tool == "delete":
    delete_posts(reddit)
elif tool == "stats":
    stats(reddit)
