import json
import chardet


def input_data():
    file_with_text = ['newsafr.json', 'newsit.json', 'newscy.json', 'newsfr.json']
    return file_with_text


def sum_of_all_news():
    all_text = ""
    for file in input_data():
        with open(file, 'rb') as f:
            temp_f = f.read()
            text_encoding = chardet.detect(temp_f)
        with open(file, encoding=text_encoding['encoding']) as f:
            text = json.load(f)

            for news in text['rss']['channel']['items']:
                all_text += news['description']
    return all_text


def count_unique_words_more_six_letters():
        listed_text = sum_of_all_news().split()
        dict_used_in_text = set(listed_text)

        top_more_six_letter_list = []
        for word in dict_used_in_text:
            if len(word) >= 6:
                top_more_six_letter_list.append(word)

        counted_each_word_quantity = []
        for word in top_more_six_letter_list:
            counted_each_word_quantity.append([listed_text.count(word), word])
        counted_each_word_quantity.sort(reverse = True)
        return counted_each_word_quantity


def print_top_ten_words():
    counted_each_word_quantity = count_unique_words_more_six_letters()
    for i in range(10):
        print(i + 1, counted_each_word_quantity[i])


print_top_ten_words()