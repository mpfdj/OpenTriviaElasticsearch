import glob
import json
import ntpath


def convert_data_to_es_bulk_format(input_folder, output_folder, file_name, i):
    input_file = open(input_folder + file_name)
    output_file = open(output_folder + file_name, "w")

    json_array = json.load(input_file)
    i = 1
    for data in json_array:
        action_and_meta_data = {"index": {"_id": "" + str(i) + ""}}

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
        i += 1

    input_file.close()
    output_file.close()


# Main
input_folder = "ascii-2/"
output_folder = "elasticsearch-2/"

for filepath in glob.iglob(input_folder + "*.json"):
    file_name = ntpath.basename(filepath)

    print("curl -H \"Content-Type: application/x-ndjson\" -XPOST \"localhost:9200/open-trivia/_bulk?pretty\" --data-binary @" + file_name)
    convert_data_to_es_bulk_format(input_folder, output_folder, file_name, i)

