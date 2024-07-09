from textblob import TextBlob


def analyze_sentiment(text):
    """
    Analyse le sentiment du texte donné.
    Retourne 'positif', 'négatif' ou 'neutre'.
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        return "positif"
    elif polarity < 0:
        return "négatif"
    else:
        return "neutre"
