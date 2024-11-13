words=[]
count= []

for word in range(10):
    word= input("Enter a word:")
    words.append(word)

min_length= int(input("Enter a number for the minimum length of words to dsiplay:"))

for word in words:
    if len(word) == min_length:
        count.append(word)
    else:
        continue
print(f"Here are the words with {min_length} letters: {count}")