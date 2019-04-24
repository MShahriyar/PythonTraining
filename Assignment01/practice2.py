import re
import csv

words = []
matched_words = []
counter = 0

with open(file = 'program.txt', mode = 'r') as read:
    data = read.readlines()                                            
    for line in data:                                                  
        for word in line.split():                                      
            # words.append(word.strip("."))                            
             words.append(re.sub('[^a-zA-Z0-9]+', '', word))

print(words)

with open('mycsvfile.csv', 'w') as f:
    field_names = (['Matching item', 'Frequency of matching items', 'Split items'])
    the_writer = csv.DictWriter(f, fieldnames=field_names)
    the_writer.writeheader()

    for i in range(0, len(words), 2):
        counter = 0
        if i+1 < len(words):
            word_to_match = words[i] + words[i+1]
            if word_to_match not in matched_words:
                for j in range(0, len(words), 2):
                    if j+1 < len(words):
                        current_word = words[j]+words[j+1]
                        if word_to_match == current_word:
                            counter += 1
                matched_words.append(word_to_match)
                data = {
                    'Matching item': word_to_match,
                    'Frequency of matching items': counter-1,
                    'Split items': [words[i], words[i+1]]
                }
                if data['Frequency of matching items'] > 0:
                    the_writer.writerow(data)
