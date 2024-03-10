from abc import ABC, abstractmethod


class BaseTokenizer(ABC):

	
	@abstractmethod
	def encode(self, text: str):
		"""Encodes text"""
		raise NotImplementedError()

	@abstractmethod
	def decode(self, text: str):
		"""Decodes text"""
		raise NotImplementedError()


