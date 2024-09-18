# Write a fn. which takes a filename and write a histogram of word lengths to a file. 
# Output looks like this:
# 1: ######
# 2: ##########

def histogram_of_file(filename,histogram):
    histogram_count = {}

    file_handler = open(filename,"r")
    file_list = file_handler.readlines()

    output_handler = open(histogram,"w")

    for sentences in file_list:
        words = sentences.strip().split()
        for word in words:
            wordlength = len(word)
            if(wordlength in histogram_count):
                histogram_count[wordlength] += 1
            else:
                histogram_count[wordlength] = 1
    
    for wordlength in sorted(histogram_count):
        count = histogram_count[wordlength]
        output_handler.write(str(wordlength) + ": " + "#" * count + "\n")
    file_handler.close()
    output_handler.close()
histogram_of_file("sentences_1.txt","histogram.txt")

