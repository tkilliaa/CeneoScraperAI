from app import app
from app.utils import extractElements
class Opinion:

        selectors = {
            "author": ["span.user-post__author-name"],
            "recomendation": ["span.user-post__author-recomendation > em"],
            "stars": ["span.user-post__score-count"],
            "content": ["div.user-post__text"],
            "advantages": ["div.review-feature__col:has(> div[class*=\"positives\"])"],
            "disadvantages": ["div.review-feature__col:has(> div[class*=\"negatives\"])"],
            "helpful": ["button.vote-yes > span"],
            "unhelpful": ["button.vote-no > span"],
            "publishDate": ["span.user-post__published > time:nth-child(1)","datetime"],
            "purchaseDate": ["span.user-post__published > time:nth-child(2)","datetime"]
        }

        def __init__(self, opinionID=None, author=None, recomendation=None, stars=None, content=None, advantages=None, disadvantages=None, helpful=None, unhelpful=None, purchased=None, purchaseDate=None, publishDate=None):
            self.opinionID = opinionID
            self.author = author
            self.recomendation = recomendation
            self.stars = stars
            self.content = content
            self.advantages = advantages
            self.disadvantages = disadvantages
            self.helpful = helpful
            self.unhelpful = unhelpful
            self.purchased = purchased
            self.purchaseDate = purchaseDate
            self.publishDate = publishDate

        def extractOpinion(self, opinionTree):
            for key, value in self.selectors.items():
                setattr(self, key, extractElement(opinion, *value))
            self.opinionID = opinion["data-entry-id"]
            self.transformOpinioin()
        def transformOpinioin(self):
            try:
                    self.advantages = self.advantages.replace("Zalety\n", "").replace("\n", ", ")
                except AttributeError:
                    pass
                try:
                    self.disadvantages = self.disadvantages.replace("Wady\n", "").replace("\n", ", ")
                except AttributeError:
                    pass
                
                self.recomendation = True if self.recomendation == "Polecam" else False if self.recomendation == "Nie Polecam" else None
                self.stars = float(self.stars.split("/")[0].replace(",","."))
                self.content = self.content.replace("\n", " ").replace("\r", " ").replace("\t", " ")
                self.helpful = int(self.helpful)
                self.unhelpful = int(self.unhelpful)

        def __str__(self): #return the product and details
            pass