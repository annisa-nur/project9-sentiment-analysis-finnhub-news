import finnhub

def scrape_news():
    finnhub_client = finnhub.Client(api_key="cptts59r01qnga5inj30cptts59r01qnga5inj3g")

    news = finnhub_client.general_news('general', min_id=0)

    return news
