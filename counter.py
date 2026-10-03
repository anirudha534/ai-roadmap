from collections import Counter

sentence = "the cat sat on the mat and the cat slept"
words = sentence.split()

counts = Counter(words)

print(dict(counts))

print(dict(counts.most_common(3)))