def input_data():
    print('Введите имя файла')
    file_with_text = input()
    return file_with_text


def top_ten_word():
    import chardet
    with open(input_data(), 'br') as f:
        text = f.read()
        encoding_detected = chardet.detect(text)
        decoded_text = text.decode(encoding_detected['encoding'])
        listed_text = decoded_text.split()
        dict_used_in_text = set(listed_text)

        top_more_six_letter_list = []
        for word in dict_used_in_text:
            if len(word) >= 6:
                top_more_six_letter_list.append(word)

        counted_each_word_quantity = []
        for word in top_more_six_letter_list:
            counted_each_word_quantity.append([listed_text.count(word),word])
            counted_each_word_quantity.sort(reverse=True)

    for i in range(0,10):
        print(i+1, counted_each_word_quantity[i])


top_ten_word()