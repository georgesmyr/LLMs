from typing import Dict
from .base import BaseTokenizer
from .utils import split_text
from .consts import UKNOWN_WORD


class SimpleTokenizer(BaseTokenizer):
    """
    Simple tokenizer that uses a vocabulary to encode and deconde text.
    If a word in the text in not in the vocabulary, it is replaced by '<|unknown|>'.
    """

    def __init__(self, vocab: Dict[str, int]):
        """Initialize the tokenizer with a vocabulary."""
        self.word_to_id = vocab
        self.id_to_word = {id: word for word, id in vocab.items()}

    def encode(self, text: str) -> list[int]:
        """Encodes the input text. Returns a list of ids."""
        text_split = split_text(text)
        text_split = [word if word in self.word_to_id.keys() else UKNOWN_WORD for word in text_split]
        ids = [self.word_to_id[word] for word in text_split]
        return ids
    
    def decode(self, ids: list[int]) -> str: 
        """Decodes the input list oof ids. Returns text."""
        words = [self.id_to_word[id] for id in ids]
        text = " ".join(words)
        return text