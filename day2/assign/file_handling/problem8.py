# Write a fn. which takes two input filenames and one output filename and writes the common strings to the output file

def common_strings(file1,file2,output_file):
    file1_handler = open(file1,"r")
    file2_handler = open(file2,"r")

    output_file_handler = open(output_file,"w")

    file1_data = file1_handler.readlines()
    file2_data = file2_handler.readlines()

    freq_strings = {}
    for string in file1_data + file2_data:
        if(string in freq_strings):
            freq_strings[string] += 1
        else:
            freq_strings[string] = 1

    for count in freq_strings:
        if(freq_strings[count] == 2):
            output_file_handler.writelines(count)

    output_file_handler.close()

common_strings("words1.txt","words2.txt","problem8_out.txt")
