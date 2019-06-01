class JokeManager:
    def __init__(self, language):
        self.language = language
        return

    def get_random_joke(self, categories=None):
        return "joke..."