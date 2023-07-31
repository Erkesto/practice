#jingle bells code

counts = dict()
print ('Enter a line of text:')
line = input('')

words = line.split()

print('Words:',words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word,0) + 1
max_key = max(counts , key = counts.get)
print(max_key , counts[max_key])