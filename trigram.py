import nltk
from nltk.util import trigrams
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

nltk.download('punkt_tab', quiet=True)

text = "Natural language processing is a very interesting field of computer science and natural language processing is widely used"

tokens = [word.lower() for word in word_tokenize(text)]

tri_grams = list(trigrams(tokens))

freq_dist = FreqDist(tri_grams)

def predict_next(w1, w2):
  candidates = {}

  for (a, b, c), count in freq_dist.items():
    if a == w1 and b == w2:
       candidates[c] = count

  if candidates:
    return max(candidates, key=candidates.get)
  else:
    return "No prediction found"

print(f"The predicted next word after '{'natural'}' and '{'language'}' is: {predict_next('natural', 'language')}")
