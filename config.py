# BOT CONFIGURATION OPTIONS

# Bot user agent
USER_AGENT = 'A bot that runs r/PortugalOnReddit. Created by u/Synergix'

# Subreddit where the bot will post
SUBREDDIT_TO_POST = 'PortugalOnReddit'

# Expressions to monitor for
EXPRESSIONS_TO_MONITOR = ['portugal', 'portuguese', 'português', 'portogallo', 'portugali', 'portugalia', 'Португалия', 'ポルトガル', '葡萄牙',
                          'portugisiska', 'portugalski', 'portoghese', 'portugais', 'portugués', '葡萄牙語', 'португальский',
                          'portugiesisch', 'portugisisk', 'portugees', 'ポルトガル語']

# Subreddits to monitor for (+ to monitor multiple subreddits; - to exclude a subreddit)
SUBREDDITS_TO_MONITOR = 'all-PortugalOnReddit-portugal-PORTUGALCARALHO-PrimeiraLiga-portugaltheman-PortugalGoneWild'

# Number of submissions to check in each run
SEARCH_LIMIT = 8000

# Post mode (choose 'direct' or 'comment')
# 'direct' will make the bot post the direct link of the source submission
# 'comment' will make the bot post the link to the comment section of the source submission
POST_MODE = 'comment'

# Required score to cross-post a submission found by search when setting up your subreddit
REQUIRED_SCORE = 500
