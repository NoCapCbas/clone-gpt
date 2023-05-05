import requests
import os

# get training data
# tinyshakespeare_url = 'https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt'
# r = requests.get(tinyshakespeare_url)
# with open(os.path.join(os.getcwd(), 'input.txt'), 'w') as f:
#     f.write(r.text)
# end get training data


text_path = r'/Users/cbas/Documents/Code Projects/pythonWork/clone-gpt/input.txt'

# get unique chars that occur in this text
with open(text_path, 'r') as f:
    text = f.read()

chars = sorted(list(set(text)))
vocab_size = len(chars)
# print(''.join(chars))
# print(vocab_size)

# tokenization
stoi = { ch:i for i,ch in enumerate(chars)}
itos = { i:ch for i,ch in enumerate(chars)}
encode = lambda s: [stoi[c] for c in s] #endcoder: take a string, output a list of integers
decode = lambda l: ''.join([itos[i] for i in l]) #decoder: take a list of integers, output a string

print(encode('hii there'))
print(decode(encode('hii there')))




