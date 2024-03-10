from typing import Union
from os import PathLike
import re
from .consts import UKNOWN_WORD, END_OF_TEXT

def get_vocab(text: str):
	"""Returns the vocabulary of the text (token, id)"""
	text_split = split_text(text)
	all_words = sorted(list(set(text_split)))
	all_words.extend([UKNOWN_WORD, END_OF_TEXT])
	vocab = {word: integer for integer, word in enumerate(all_words)}
	return vocab


def split_text(text: str) -> list[str]:
	"""Splits text into words"""
	text_split = re.split(r'([,.?_!()\'\"]|--|\s)', text)
	text_split = [item.strip() for item in text_split if item.strip()]
	return text_split


def read(path: Union[PathLike, list[PathLike]]) -> str:
	""" Reads text from path, returns it as string """
	with open(path, "r", encoding="utf-8") as file:
		return file.read()
