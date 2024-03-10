from tokenize.utils import get_vocab, read
from tokenize.simple import SimpleTokenizer


text = read("../data/the-verdict.txt")
vocab = get_vocab(text)

tokenizer = SimpleTokenizer(vocab)

sentence = "This is a sample sentence."
ids = tokenizer.encode(sentence)
ids_inv = tokenizer.decode(ids)

print(sentence)
print(ids)
print(ids_inv)
