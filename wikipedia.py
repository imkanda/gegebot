import wikipedia

class Wikipedia:
    def __init__(self, language='en'):
        self.language = language
        wikipedia.set_lang(language)

    def get_summary(self, search):
        return wikipedia.summary(search, chars = 1950)
    
    def get_random(self):
        # Get a title of a random Wikipedia article
        title = wikipedia.random()
        # Fix up the title so we can find the URL
        fixed_title = title.replace(' ', '_')
        return fixed_title
