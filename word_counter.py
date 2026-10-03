sentence = "the cat sat on the mat and the cat slept"
words = sentence.split()

counts = {}
for i in words:
    counts[i] = counts.get(i,0) + 1
print(counts)