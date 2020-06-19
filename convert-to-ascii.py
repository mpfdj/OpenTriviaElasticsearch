import codecs
import glob
import ntpath

input_folder = "data-1/"
output_folder = "ascii-1/"
# input_folder = "data-2/"
# output_folder = "ascii-2/"


def convert_data(file_name):
    utf8_data = codecs.open(input_folder + file_name, "r", encoding="utf-8").read()
    ascii_file = codecs.open(output_folder + file_name, "w", encoding="ascii", errors="ignore")
    ascii_file.write(utf8_data)


# Main
for filepath in glob.iglob(input_folder + "*.json"):
    file_name = ntpath.basename(filepath)
    print("Converting " + file_name)
    convert_data(file_name)
