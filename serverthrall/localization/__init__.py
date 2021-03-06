from .translations import language_map

class Localization():

    def __init__(self, config):
        self.config = config

    def return_word(self, key):
        language = self.config.get('language', default='en')

        if language not in language_map:
            language = 'en'

        if key not in language_map[language]:
            language = 'en'

        if key not in language_map[language]:
            return key

        return language_map[language][key]
