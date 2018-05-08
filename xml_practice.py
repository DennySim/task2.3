from xml import etree
import xml.etree.ElementTree as ET
import chardet


def input_data():
    file_with_text = ['newscy.xml', 'newsfr.xml', 'newsit.xml', 'newsafr.xml']
    return file_with_text


def sum_of_all_news(file):
    all_text = ""

    # for file in input_data():
    with open(file, 'rb') as ff:
        text = ff.read()
        text_encoding = chardet.detect(text)

    parser = etree.ElementTree.XMLParser(encoding=text_encoding['encoding'])
    tree = ET.parse(file, parser)
    all_msg = tree.findall('channel/item/description')

    for desc in all_msg:
        all_text += desc.text
    return all_text


def count_unique_words_more_six_letters(file):
    listed_text = sum_of_all_news(file).split()
    dict_used_in_text = set(listed_text)

    top_more_six_letter_list = []
    for word in dict_used_in_text:
        if len(word) >= 6:
            top_more_six_letter_list.append(word)

    counted_each_word_quantity = []
    for word in top_more_six_letter_list:
        counted_each_word_quantity.append([listed_text.count(word), word])
    counted_each_word_quantity.sort(reverse=True)
    return counted_each_word_quantity


def print_top_ten_words():
    for file in input_data():
        print(file)
        counted_each_word_quantity = count_unique_words_more_six_letters(file)
        for i in range(10):
            print(i + 1, counted_each_word_quantity[i])


print_top_ten_words()


