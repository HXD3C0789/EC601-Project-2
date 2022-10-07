import botometer

rapidapi_key = "XXXXXX"
twitter_app_auth = {
    'consumer_key': 'XXXXXX',
    'consumer_secret': 'XXXXXX',
    'access_token': 'XXXXXX',
    'access_token_secret': 'XXXXXX',
  }

blt_twitter = botometer.BotometerLite(rapidapi_key=rapidapi_key, **twitter_app_auth)

# Prepare a list of screen_names you want to check.
# The list should contain no more than 100 screen_names; please remove the @
screen_name_list = ['username']
blt_scores = blt_twitter.check_accounts_from_screen_names(screen_name_list)

# Prepare a list of user_ids you want to check.
# The list should contain no more than 100 user_ids.
user_id_list = [userid]
blt_scores = blt_twitter.check_accounts_from_user_ids(user_id_list)

# run these in terminal:
# pip install botometer
# pip install requests tweepy