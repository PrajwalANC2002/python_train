# Write a fn. that takes a filename and 'n' and finds the number of words with 'n' characters. Assume one or more words per line

def number_of_words_with_n_char_in_sentencefile(filename,n):
    file_handler = open(filename,"r")  #used to store the content of file in file_handler
    file_list = file_handler.readlines() #used to store the individual lines as list in file_list
    wordcount = 0
    for sentence in file_list:#iterate through the sentence
        words = sentence.strip().split() #removes the spaces and splits the sentence into words
        for word in words: #iterates through the words
            if(len(word) == n):
                wordcount += 1
    file_handler.close()
    return wordcount

print(number_of_words_with_n_char_in_sentencefile("sentences_1.txt",10))
