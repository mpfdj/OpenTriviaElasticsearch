import glob
import json
import ntpath


def convert_data_to_es_bulk_format(input_folder, output_file, file_name):
    global index

    input_file = open(input_folder + file_name)

    json_array = json.load(input_file)
    for data in json_array:
        action_and_meta_data = {"index": {"_id": "" + str(index) + ""}}

        try:
            optional_source = {
                "category": file_name.split(".")[0].replace("_", " "),
                "question": data["question"],
                "type": "multiple-choice",
                "answer": data["answer"],
                "choices": data["choices"]
            }
        except:
            continue

        # print(action_and_meta_data)
        # print(data)
        output_file.write(json.dumps(action_and_meta_data) + "\n")
        output_file.write(json.dumps(optional_source) + "\n")
        index += 1

    input_file.close()


# Main
input_folder = "ascii-2/"
output_file = open("elasticsearch-2/es-data.json", "w")
index = 1

for filepath in glob.iglob(input_folder + "*.json"):
    file_name = ntpath.basename(filepath)
    convert_data_to_es_bulk_format(input_folder, output_file, file_name)


output_file.close()
