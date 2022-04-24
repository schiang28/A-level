import tweepy
from datetime import datetime

# https://www.dataquest.io/blog/streaming-data-python/
# https://developer.twitter.com/en/docs/tutorials/consuming-streaming-data
# https://docs.tweepy.org/en/latest/getting_started.html

################################
# Class Definitions
################################
class MyApp(tweepy.Stream):

    TWITTER_APP_KEY = "" # (API key)
    TWITTER_APP_SECRET = "" # (API secret key)
    TWITTER_KEY = "" #(Access token)
    TWITTER_SECRET = "" #(Access token secret)

    def __init__(self):
        super().__init__(
            MyApp.TWITTER_APP_KEY, 
            MyApp.TWITTER_APP_SECRET,
            MyApp.TWITTER_KEY, 
            MyApp.TWITTER_SECRET)
        self.tweets = 0
        
    """
    We can extract this information in the on_status method:

    description = status.user.description
    loc = status.user.location
    text = status.text
    coords = status.coordinates
    name = status.user.screen_name
    user_created = status.user.created_at
    followers = status.user.followers_count
    id_str = status.id_str
    created = status.created_at
    retweets = status.retweet_count
    bg_color = status.user.profile_background_color
    """
    
    def on_status(self, status):
        if self.tweets == 0:
            self.start = datetime.now()
        self.tweets += 1
        #print(status.text)
        if self.tweets % 10 == 0:
            now = datetime.now()
            tps = self.tweets/(now - self.start).total_seconds()
            print(f'{tps:.2f}')

    def on_error(self, status_code):
        if status_code == 420:
            return False

################################
# Main Program
################################
app = MyApp()

try:
    app.filter(track=["trump", "donald trump"])
except KeyboardInterrupt:
    print("Closing!")
