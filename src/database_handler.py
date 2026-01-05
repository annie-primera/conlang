import logging

from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection

from models.words import WordNode, LexicalRelationshipEdge


log = logging.getLogger(__name__)


class Database:    

    @staticmethod
    def get_connection(self):
        host = "ws://localhost:8182/gremlin"
        g = traversal().with_remote(DriverRemoteConnection(host,'g'))
        return g


class DatabaseOperations:

    def __init__(self, word):
        self.word = word
        self.g = Database.get_connection()

    def get_word(self, word = None):
        if word:
            retrieved_word = self.g.V().has("vocabulary", "word", word).toList()
        else:
            retrieved_word = self.g.V().has("vocabulary", "word", self.word).toList()
        return retrieved_word[0]

    def delete_word(self):
        word_vertex = self.g.V().has("vocabulary", "word", self.word).next()
        if word_vertex:
            self.g.V(word_vertex).drop().iterate()
            return f"{self.word} deleted from the dictionary"
        else:
            log.error(f"{self.word} does not exist in the dictionary")

    def add_word(self, word_info: WordNode):
        word_info_dict = word_info.model_dump()
        traversal = self.g.add_v("vocabulary")
        for key, value in word_info_dict:
            traversal = traversal.property(key, value)
        traversal.iterate()

    def add_word_relationship(self, relationship: LexicalRelationshipEdge, word_2):
        pass

    def fetch_related_words():
        pass
