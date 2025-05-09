import requests

class NewsFeed:
    base_url = "https://newsapi.org/v2/everything"
    api_key="Your-API-Key-after-regrstrn."

    def __init__(self,interest,from_date,to_date,language):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = f"{self.base_url}?q={self.interest}&from={self.from_date}&to={self.to_date}&language={self.language}&apiKey={self.api_key}"
        response = requests.get(url)
        content = response.json()
        articles = content['articles']

        email_body = ''
        for article in articles:
            email_body += article['title'] + "\n" + article['url'] + "\n\n"

        return email_body