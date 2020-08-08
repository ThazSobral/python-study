# utiliza a biblioteca TWITTER_SCRAPER para pegar uma "raspagem"
from twitter_scraper import get_tweets

# definimos uma lista para armazenar os tweets
tweets = []
# realizamos a busca utilizando o método GET_TWEETS
for tweet in get_tweets('jairbolsonaro'):
    # criamos um dicionário já formatado
    item = {'text': tweet['text'], 'likes':tweet['likes']}
    # adicionamos o dicionario na lista
    tweets.append(item)

# definimos uma função para considerar os likes como critério
def criteria(tweet): return tweet['likes']

# ordenamos os tweets na lista pelo critério definido e de forma reversa (do maior para o menor)
tweets_ordened = sorted(tweets, key=criteria, reverse=True)

print('TOP 10 tweets\n')

# mostramos apenas os 10 primeiros da lista
for tweet in tweets_ordened[:10]:
    print(f'Tweet: {tweet["text"]}\nLikes: {tweet["likes"]}\n')
