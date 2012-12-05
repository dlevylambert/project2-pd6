from log import Logger
from twitter import *

logger = Logger("log.txt")

consumer_key="6UyBIoeC3XNhAZJt9NLQrw"
consumer_secret="I1av2O10CzAUSfdjlHGbIGbUqmvgJ7h1aJNCqIPj8"

access_token="946880250-f4ZMJlIC1gFehq9OWWHYMY4M7IV7OtpIwT6SHnts"
access_token_secret="tEuprZbab9mx4u9uvHmEd7adFZw51eVp1tACdzM0"

t = Twitter(
    auth=OAuth(access_token, access_token_secret,
                consumer_key, consumer_secret)
            )

def get_celeb(name):
    logger.log("Searching for verified user '%s'"%(name))
    for user in t.users.search(q=name):
        if user['verified']:
            return user
    logger.log("No user found", "WARNING")
    return None

def get_tweets(screen_name):
    count = 200
    include_rts = False
    trim_user = True
    logger.log("Retrieving first tweets...")
    res = t.statuses.user_timeline(screen_name=screen_name, count=200, include_rts=False, trim_user=True)
    if not res:
        logger.log("No tweets found for user '%s'"%(screen_name))
        return []
    since_id = res[-1]['id']
    for i in range(15):
        logger.log("Retrieving tweets %i to %i"%(i*count + count, i*count + 2 * count))
        tweets = t.statuses.user_timeline(screen_name=screen_name, count=200, include_rts=False, trim_user=True, since_id=since_id)
        if not tweets:
            break
        res.extend(tweets)
        since_id=tweets[-1]['id']
    return res

if __name__ == "__main__":
    user_input = raw_input("Input name\n")
    celeb = get_celeb(user_input)
    if not celeb:
        print("Could not find Celebrity.")
    else:
        with open("res.txt", "w") as f:
            for tweet in get_tweets(celeb['screen_name']):
                f.write(tweet["text"].encode("utf8") + "\n\n")
        print("Success! Results can be found in res.txt.")
