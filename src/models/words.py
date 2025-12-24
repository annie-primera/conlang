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


class Word(BaseModel):
    word: str
    pronunciation: str
    grammar_class: GrammarClass
    time_period: TimePeriod
