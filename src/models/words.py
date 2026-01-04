from pydantic import BaseModel
from enum import Enum


class GrammarClass(Enum):
    VERB = "verb"
    NOUN = "noun"
    ADJECTIVE = "adjective"
    ADVERB = "adverb"
    ARTICLE = "article"


class TimePeriod(Enum):
    MODERN = "modern"
    ANCIENT = "ancient"


class LexicalRelationships(Enum):
    SYNONYM = "synonym"
    ANTONYM = "antonym"


class Word(BaseModel):
    word: str
    meaning: str
    pronunciation: str
    grammar_class: GrammarClass
    time_period: TimePeriod


class LexicalRelationshipEdge(BaseModel):
    relationship: LexicalRelationships
