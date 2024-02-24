import re
import feedparser
import ssl
from langchain.llms import Ollama
from datetime import datetime

# Disable https
ssl._create_default_https_context = ssl._create_unverified_context

def get_news(url):
    feed = feedparser.parse(url)

    if not feed.bozo:
        news_data = [(entry.title, entry.summary) for entry in feed.entries]
        return news_data
    else:
        print(f"{url} doesn't have data. Error: {feed.bozo_exception}")
        return None

def write_resume(title, resume):
    prompt = '''I'm looking to receive a succinct summary of an article along with its title.
    The summary should encompass crucial information about the topic, highlighting any unique or surprising aspects, eliminating the need to read the entire article. 
    Please show me summary in French (if not already in French, please translate it in french), but without including the English version.'''
    model = Ollama(model="llama2")
    response = model.predict(prompt + title + resume)
    return response

def main():
    sources = {
        'Le monde de l\'informatique': "https://www.lemondeinformatique.fr/flux-rss/thematique/toutes-les-actualites/rss.xml",
        'ZNet': "https://www.zdnet.fr/feeds/rss/actualites/informatique/",
        'TomsGuide': "https://www.tomsguide.fr/feed/",
        'Silicon': "https://www.silicon.fr/actualites/workspace/browser/feed",
        'Frandroid': "https://www.frandroid.com/feed"
    }
    summaries = {}

    print("Résumons l'actualité d'aujourd'hui :", datetime.today().strftime('%d-%m-%Y') )

    for media, url in sources.items():
        news_data = get_news(url)
        summaries[media] = []

        print(" ")
        print(f"Conception du résumé de {media}...")
        
        if len(news_data) > 0:
            print(f"{len(news_data)} articles trouvés")
        else:
            print(f"{media} n'a aucun article aujourd'hui")

        print(" ")

        for i in range(0, len(news_data)):
            title, resume = news_data[i]
            print(f"Titre : {title}")

            try:
                article = write_resume(title, resume)
                summaries[media].append(article)
                print(f"Résumé : {article}")
            except Exception as e:
                print(
                    f"'{title}' n'a pas pu être créer: {e}"
                )

if __name__ == "__main__":
    main()