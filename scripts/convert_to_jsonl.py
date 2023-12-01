import json
import sys
import csv

# Determines if the row is formatted correctly
def is_valid(element: list[str]):
    must_contain_requirement = "Title:"
    must_contain_pattern = "Software Architecture Pattern:"
    return (must_contain_requirement in element[0]) and (must_contain_pattern in element[1])

# Read the data in from the path and convert each row to a json object (dictionary)
def read_and_convert(path: str) -> list[dict]:
    jsonl_list = []
    with open(path, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if is_valid(row):
                new_jsonl_obj = {"text": f"<s>{row[0]}\n{row[1]}</s>"}
                jsonl_list.append(new_jsonl_obj)
        return jsonl_list
    
# Take the data and write it to the path
def write_to_jsonl(data: list[dict], path: str) -> None:
    with open(path, "w") as file:
        for row in data:
            json_string = json.dumps(row)
            file.write(f"{json_string}\n")

if __name__ == "__main__":
    # Command to run the code is as follows: python3 convert_to_jsonl.py [csv_path] [jsonl_path]
    # where [csv_path] and [jsonl_path] are relative paths to the csv and jsonl files.

    arguments = [argument for argument in sys.argv[1:]] # Extract the command line arguments

    if len(arguments) <= 0:
        print("This command takes exactly two arguments. [csv_path] followed by [jsonl_path], which are relative paths to the csv and jsonl files.")
    else:
        is_csv = False
        is_jsonl = False

        if ".csv" == arguments[0][-4:]:
            is_csv = True
            csv_path = arguments[0]
        else:
            print(arguments[-4:])
            is_csv = False
            print(f"{arguments[0]} is not a valid csv file")

        if ".jsonl" == arguments[1][-6:]:
            is_jsonl = True
            jsonl_path = arguments[1]
        else:
            is_jsonl = False
            print(f"{arguments[1]} is not a valid jsonl file")

        if is_csv and is_jsonl:
            data = read_and_convert(csv_path)
            write_to_jsonl(data, jsonl_path)
            print(f"Data successfully written to jsonl file")
