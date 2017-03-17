# portugal-on-reddit
A Reddit bot that collects mentions to Portugal throughout Reddit and repost them to [r/PortugalOnReddit](https://www.reddit.com/r/PortugalOnReddit/).

### Usage
You can easily configure the bot to create a similar subreddit for your country. 
1. Download the code
2. Edit the appropriate variables in config.py
3. Pass your Reddit app credentials and account logging to the authenticate function. You can do this by creating a praw.ini file in the same directory of bot.py with the following format:
```
[OnReddit]
client_id=YOUR_CLIENT_ID
client_secret=YOUR_CLIENT_SECRET
password=YOUR_REDDIT_ACCOUNT_PASSWORD
username=YOUR_REDDIT_ACCOUNT_USERNAME
```
4. Run bot:
```
python bot.py
```

### Other tools
`start_subreddit` allows you to set up your new subreddit with up to 100 submissions to get things started. It uses Reddit search function to get post with a minimum score of `REQUIRED_SCORE` as defined in config.py.

`delete_posts` if anything goes wrong you can clean up your new subreddit. Removes all submissions.

##### To do
* Add statistics