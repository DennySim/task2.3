def input_data():
    print('Введите имя файла')
    file_with_text = input()
    return file_with_text


def top_ten_word():
    import json
    import chardet
    from pprint import pprint

    with open(input_data(), encoding = "utf-8" ) as f:

        text = json.load(f)

        all_text = ""
        for news in text['rss']['channel']['items']:
            all_text += news['description']

        listed_text = all_text.split()
        dict_used_in_text = set(listed_text)

        top_more_six_letter_list = []
        for word in dict_used_in_text:
            if len(word) >= 6:
                top_more_six_letter_list.append(word)

        counted_each_word_quantity = []
        for word in top_more_six_letter_list:
            counted_each_word_quantity.append([listed_text.count(word), word])
            counted_each_word_quantity.sort(reverse=True)

    for i in range(0, 10):
        print(i + 1, counted_each_word_quantity[i])

top_ten_word()