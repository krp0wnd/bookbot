def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    word_count = get_word_count(text)
    text_as_list = []
    text_as_list = text.split()
    text_as_list.sort()
    final_report(word_count, text_as_list)


def final_report(word_count, text_as_list):
    list_of_words_with_a = []
    print ("--- Begin report of books/frankenstein.txt ---")
    print (f"{word_count} words found in the document")
    for word in text_as_list:
        if word.isalpha():
            print(word)
            if "z" in word:
                #print (f"{word} contains z")
                list_of_words_with_a += word
    #print(list_of_words_with_a)
    

def get_word_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()