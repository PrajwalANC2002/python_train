# Write a fn. which takes two input filenames and one output filename and writes the concatanated output to the output file

def concat_two_files(file1,file2,output_file):
    file1_handler = open(file1,"r")
    file2_handler = open(file2,"r")

    output_file_handler = open(output_file,"w")

    file1_data = file1_handler.read()
    file2_data = file2_handler.read()

    output_data = file1_data + file2_data

    output_file_handler.write(output_data)

    output_file_handler.close()

concat_two_files("words1.txt","words2.txt","problem5_out.txt")


