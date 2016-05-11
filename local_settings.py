'''
Local Settings for a heroku_ebooks account. #fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY = 'vVFOj3eLK1D4JA3ocTg5iHEaR'
MY_CONSUMER_SECRET = 'racP3i193FDTKzS7kgo1b58qWKaLAMXIovIeg9UmsmAeNovlMD'
MY_ACCESS_TOKEN_KEY = '730445955191836672-T9xkRCJ92Gu0EqS7vYEn2h9s6avziSW'
MY_ACCESS_TOKEN_SECRET = 'j8fSgMizNd3NfmJwCsddEFbKo8RvkK6RbpGeCBOARuUjw'

SOURCE_ACCOUNTS = ["heyaudy"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 4 #How often do you want this to run? 1/8 times?
ORDER = 2 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = False #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API.
TWEET_ACCOUNT = "heyaudy_ebooks" #The name of the account you're tweeting to.
