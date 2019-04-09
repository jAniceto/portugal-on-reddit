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
python3 bot.py
```

#### To run it automatically use `cron`

```
cd /
sudo crontab -e
```

For example, to run the bot every 15 minutes set the following job:
```
*/15 * * * * python3 /path/to/file/bot.py
```


### Other tools
A few usefull tools are available to help manage your new subreddit. They are:

`start_subreddit` allows you to set up your new subreddit with up to 100 submissions to get things started. It uses Reddit search function to get posts with a minimum score of `REQUIRED_SCORE` as defined in config.py.

`delete_posts` removes all submissions. If anything goes wrong you can clean up your new subreddit.

`stats` gives a few stats

For example, to get your subreddit stats do this:
```
python3 tools.py stats
```
