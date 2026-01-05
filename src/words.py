import logging

from database_handler import DatabaseOperations
from models.words import LexicalRelationships


log = logging.getLogger(__name__)


class Words:
    def __init__(self, word: str):
        self.word = word

    def create_word(self):
        """Creates a new word"""
        database = DatabaseOperations(self.word)
        existing_word = database.get_word()
        if existing_word:
            log.error(f"{self.word} already exists in the dictionary")
        else:
            database.add_word()
            return f"{self.word} added to the dictionary"


    def delete_word(self):
        """Deletes an existing word"""
        database = DatabaseOperations(self.word)
        try:
            word_to_delete = DatabaseOperations.get_word()
        except Exception:
            log.error(f"{self.word} is not in the dictionary, cannot delete what is not there")
        database.delete_word
        return f"{self.word} deleted from the dictionary."

    def add_word_relationship(self, related_word: str, relationship: LexicalRelationships):
        """Adds a lexical relationship to a word
        Args:
        - related_word: the word to add as a relationship
        - relationship: the type of relationship (synonym or antonym)
        """
        database = DatabaseOperations(self.word)
        try:
            database.get_word(related_word)
        except Exception:
            log.error(f"{related_word} does not exist in the dictionary. Cannot create relationship.")
        database.add_word_relationship(related_word, relationship)
        return f"{related_word} added as {relationship.relationship.value} to {self.word}"

    def retrieve_word(self) -> dict:
        """Retrieves general information about a given word"""
        pass

    def retrieve_words_by_meaning(self, meaning: str) -> list[str]:
        pass

    def retrieve_related_word(self, relationship: LexicalRelationships) -> list[str]:
        """Retrives a list of all the synonyms or antonyms of a word"""
        pass
