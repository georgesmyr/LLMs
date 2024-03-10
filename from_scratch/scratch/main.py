from tokenizer.utils import get_vocab, read
from tokenizer.simple import SimpleTokenizer
from dataset import create_dataloader


text = read("../data/the-verdict.txt")
vocab = get_vocab(text)

tokenizer = SimpleTokenizer(vocab)

sentence = "This is a sample sentence. Create a dataloader with it."
dataloader = create_dataloader(text, batch_size=2, max_length=4, stride=1, tokenizer=tokenizer)
data_iter = iter(dataloader)
print("First batch:")
first_batch = next(data_iter)
print(first_batch)
print("Second batch:")
second_batch = next(data_iter)
print(second_batch)