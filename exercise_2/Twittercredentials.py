import tweepy

consumer_key = "6WZUammZHcxxbGdf5pSltotPd";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "Rq444DPWapbVAaxgriecve7Et4vsFYLKXiBVQGpHmW9XlNcFQw";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "937440107195351040-TwKzujD6bS74oat3brT2MUf9pVV6HjU";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "NKLImTROOnzjgjrtqVrEy9mr7XiiYmavMk9GZwsVcSn3V";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



