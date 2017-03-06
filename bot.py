import praw
import time
import pprint


# expressions_to_monitor = ["portugal", "portuguese", "porto", "lisboa", "oporto", "lisbon"]
expressions_to_monitor = ["portugal"]
subreddits_to_monitor = "all-portugal-PORTUGALCARALHO-PrimeiraLiga"
required_score = 500


def authenticate():
    print("Authenticating...")
    reddit = praw.Reddit('PortugalOnReddit', user_agent='PortugalOnReddit v0.1')
    print("Authenticated as {}".format(reddit.user.me()))
    return reddit


def start_subreddit(reddit):
    submissions_number = 0
    for expression in expressions_to_monitor:
        search_query = 'title:' + expression

        for submission in reddit.subreddit(subreddits_to_monitor).search(search_query, syntax='lucene', time_filter='year'):
            # pprint.pprint(vars(submission))
            if submission.score >= required_score:
                title = submission.title  # Submission's title
                url = submission.url  # Submission's url
                xpost = "[{}] ".format(submission.subreddit.display_name)  # x-post string: [subreddit]
                comments_url = 'https://www.reddit.com' + submission.permalink  # link to submission's comment section

                new_post_title = xpost + title
                new_post_url = url
                new_post_text = "[Link to original post here]({})".format(comments_url)
                post_to = reddit.subreddit('PortugalOnReddit')

                print(new_post_title + ' - ' + url + '\n' + comments_url + '\n')

                new_post(post_to, new_post_title, new_post_url, new_post_text)

                submissions_number += 1

    print(str(submissions_number) + ' submissions found')


def new_post(subreddit, title, url, text):
    post = subreddit.submit(title, url=url)
    sticky_comment = post.reply(text).mod.distinguish(sticky=True)


def main():
    reddit = authenticate()
    start_subreddit(reddit)


if __name__ == '__main__':
    main()
