phrase = "just a random string "
lenght = len(phrase)



new_string = ""

for word in range(lenght):
    
    if word % 2 == 0:
        new_string += phrase[word].upper()
    else:
        new_string += phrase[word].lower()

print(new_string)
