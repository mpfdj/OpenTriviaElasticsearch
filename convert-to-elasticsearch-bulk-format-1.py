import glob
import json
import ntpath
import random


def convert_data_to_es_bulk_format(input_folder, output_folder, file_name):
    input_file = open(input_folder + file_name)
    output_file = open(output_folder + file_name, "w")

    json_array = json.load(input_file)
    i = 1
    for data in json_array:
        action_and_meta_data = {"index": {"_id": "" + str(i) + ""}}

        optional_source = {"question": data["question"], "type": "multiple-choice", "answer": None, "choices": None}
        if len(data["answers"]) == 1: optional_source["type"] = "open-ended"
        optional_source["answer"] = data["answers"][data["answer"]]
        optional_source["choices"] = random.shuffle(data["answers"])

        output_file.write(json.dumps(action_and_meta_data) + "\n")
        output_file.write(json.dumps(optional_source) + "\n")
        i += 1

    input_file.close()
    output_file.close()


# Main
input_folder = "ascii-1/"
output_folder = "elasticsearch-1/"

for filepath in glob.iglob(input_folder + "*.json"):
    file_name = ntpath.basename(filepath)
    print("Converting " + file_name)
    convert_data_to_es_bulk_format(input_folder, output_folder, file_name)
