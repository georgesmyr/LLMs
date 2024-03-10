import torch
from torch.utils.data import Dataset, DataLoader
import tiktoken
 

class GPTDataset(Dataset):
    def __init__(self, txt, tokenizer, max_length, stride):
        self.tokenizer = tokenizer
        self.input_ids = []
        self.target_ids = []
 
        token_ids = tokenizer.encode(txt)
 
        for i in range(0, len(token_ids) - max_length, stride):
            input_chunk = token_ids[i:i + max_length]
            target_chunk = token_ids[i + 1: i + 1 + max_length]
            self.input_ids.append(torch.tensor(input_chunk))
            self.target_ids.append(torch.tensor(target_chunk))
 
    def __len__(self):
        return len(self.input_ids)
 
    def __getitem__(self, idx):
        return self.input_ids[idx], self.target_ids[idx]


def create_dataloader(text: str, batch_size: int = 4, max_length: int = 256, stride: int = 128, shuffle: bool = False, tokenizer=None):
    """
    Creates a dataloader.
    
    Args:
        text: The text to be tokenized.
        batch_size: The batch size.
        max_length: The maximum length of the tokenized sequence.
        stride: The stride for the tokenized sequence.
        shuffle: Whether to shuffle the dataset.
        tokenizer: The tokenizer to use.

    Returns:
        A dataloader.
    """ 
    tokenizer = tokenizer or tiktoken.get_encoding("gpt2")
    dataset = GPTDataset(text, tokenizer, max_length, stride)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)
    return dataloader
