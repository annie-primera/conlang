import logging

from database_handler import DatabaseOperations
from models.words import LexicalRelationships


log = logging.getLogger(__name__)


class Words:
    def __init__(self, word: str):
        self.word = word

    def create_word(self):
        """Creates a new word"""
        pass

    def delete_word(self):
        """Deletes an existing word"""
        database = DatabaseOperations(self.word)
        try:
            word_to_delete = DatabaseOperations.retrieve_word()
        except Exception:
            log.error(f"{self.word} is not in the dictionary")
        database.delete_word

    def add_word_relationship(related_word: str, relationship: LexicalRelationships):
        """Adds a lexical relationship to a word
        Args:
        - related_word: the word to add as a relationship
        - relationship: the type of relationship (synonym or antonym)
        """
        pass

    def retrieve_word(self) -> dict:
        """Retrieves general information about a given word"""
        pass

    def retrieve_words_by_meaning(self, meaning: str) -> list[str]:
        pass

    def retrieve_related_word(self, relationship: LexicalRelationships) -> list[str]:
        """Retrives a list of all the synonyms or antonyms of a word"""
        pass
