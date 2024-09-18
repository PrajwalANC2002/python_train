# Write a fn. which takes two input filenames and one output filename and writes the concatanated output to the output file
# but after removing common strings

def remove_common_strings(file1,file2,output_file):
    file1_handler = open(file1,"r")
    file2_handler = open(file2,"r")

    output_file_handler = open(output_file,"w")

    file1_data = file1_handler.readlines()
    file2_data = file2_handler.readlines()

    freq_strings = {}                      #empty dictionary to keep track of frequency of strings in both files
    for string in file1_data + file2_data:
        if(string in freq_strings):
            freq_strings[string] += 1
        else:
            freq_strings[string] = 1

    for count in freq_strings:
        if(freq_strings[count] == 1):
            output_file_handler.writelines(count)

    output_file_handler.close()

remove_common_strings("words1.txt","words2.txt","problem7_out.txt")
