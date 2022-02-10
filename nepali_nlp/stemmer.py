import snowballstemmer

class Stem:
    """Stem the words to its root eg 'गरेका' to 'गर'.
    Credit: https://github.com/snowballstem/snowball
    """
    def __init__(self) -> None:
        self.stemmer = snowballstemmer.NepaliStemmer()
    
    def rootify(self, text):
        """Generates the stem words for input text.

        Args:
            text (Union(List, str)): Text to be stemmed or lemmatized.

        Returns:
            Union(List, str): stemmed text.
        """
        if isinstance(text, str):
            return self.stemmer.stemWords(text.split())
        
        return self.stemmer.stemWords(text)
        