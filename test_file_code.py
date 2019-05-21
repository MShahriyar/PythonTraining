
import textacy
import pandas
import time
import progressbar
start_time = time.time()

list_of_data = []
list_words = []
matched_list_words = []

def read_data_file(texts):
    count = 0
    for line in texts:
        for data in line.split():
            count +=1
            yield data


def compare_data():
    for item in read_data_file(text):
        list_words.append(item)

    for i in range(0, len(list_words)):
        counter = 0

        if i + 1 < len(list_words):
            word_to_match = list_words[i] + list_words[i + 1]

        if word_to_match not in matched_list_words:

            for j in range(0, len(list_words)):
                current_word = list_words[j]
                if word_to_match == current_word:
                    counter += 1

            matched_list_words.append(word_to_match)

            data = {
                'Matching item': word_to_match,
                'Frequency of items': counter,
                'Split items': [list_words[i], list_words[i + 1]]
            }

            if data['Frequency of items'] > 0:
                yield data


for i in progressbar.progressbar(range(100)):

    text = textacy.io.read_text('text_file', mode='rt', encoding='utf-8')
    read_data_file(text)

    for i in compare_data():
        list_of_data.append(i)
    time.sleep(0.02)

textacy.io.csv.write_csv(list_of_data, fname='matching_data_file.csv', encoding='utf-8',
                         fieldnames=['Matching item', 'Frequency of items', 'Split items'])


def sort_data():
    article_read = pandas.read_csv('matching_data_file.csv')
    sort_by_column_name = article_read.sort_values(by=['Frequency of items'], ascending=False)
    yield sort_by_column_name


print(next(sort_data()))


