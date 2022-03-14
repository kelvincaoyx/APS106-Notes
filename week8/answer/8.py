# Write a program that asks a user to enter a string and output letter 
# that appears the most times and the number of times it appears. 
# You need to deal with both capital and lower-case letters.

word = input("Enter a word: ")
counts = []
word = word.lower()

# initialize a list to store the number of times each letter appears
for i in range(26):
    counts.append(0)

# for each letter, add 1 to the list for that number
for i in word:
    counts[ord(i) - ord('a')] += 1

# find the index of the max entry in a
index = 0
for i in range(len(counts)):
    if(counts[i] > counts[index]):
        index = i

letter = chr(index + 97)
print("The letter " + letter +"/"+ letter.upper()+ " appears most often." )
