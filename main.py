import json
import os


def process_json_file(json_file):
    with open(json_file) as f:
        try:
            # parse JSON data to python dict
            data = json.load(f)
        except json.JSONDecodeError:
            print(f"Error: {json_file} is not valid JSON")
            return None

        # Capture only the attributes within the "message" key
        message_data = data.get("message", {})

        return sniff_schema_item(message_data)


def sniff_schema_item(item):
    # function to sniff JSON object schema structure

    item_props = {}
    for item_attr, item_val in item.items():
        # declare type string if value of the attribute is a string
        if isinstance(item_val, str):
            item_props[item_attr] = {
                'type': 'string'}

        # declare type boolean if value of the attribute is a boolean
        elif isinstance(item_val, bool):
            item_props[item_attr] = {
                "type": "boolean"
            }

        # declare type integer if value of the attribute is a integer
        elif isinstance(item_val, int):
            item_props[item_attr] = {
                'type': 'integer'}

        elif isinstance(item_val, list):
            # Check if the list contains only strings
            # Thus, declare type enum
            if all(isinstance(sub_item, str) for sub_item in item_val):
                item_props[item_attr] = {
                    'type': 'enum'}

            # Check if the list contains only JSON objects
            # Thus, declare type array and  append the schema structure of the JSON objects to items key
            elif all(isinstance(sub_item, dict) for sub_item in item_val):
                item_props[item_attr] = {
                    'type': 'array'}
                sub_item_schema = {}
                for sub_item in item_val:
                    sub_item_props = sniff_schema_item(sub_item)
                    sub_item_schema.update(sub_item_props)
                if sub_item_schema:
                    item_props[item_attr]['items'] = sub_item_schema

            else:
                item_props[item_attr] = {
                    'type': 'array'
                }
        # declare type object if the value of the attribute is a JSON object
        # sniff the schema structure of the JSON object and append to properties key
        elif isinstance(item_val, dict):
            item_props[item_attr] = {
                'type': 'object',
            }
            item_props[item_attr]['properties'] = sniff_schema_item(item_val)

        # Catch undefined schema type
        else:
            item_props[item_attr] = {
                'type': 'undefined'
            }

        # add "tag" and "description" keys to attribute schema
        # and set all properties "required": false
        item_props[item_attr].update({
            'description': '',
            'tag': '',
            'required': False
        })
    return item_props


def write_schema_file(schema, output_file):
    with open(output_file, "w") as f:
        # Convert python dict to json object and write to output file
        json.dump(schema, f, indent=2)


def process_all_json_files(input_dir, output_dir):
    # Create output directory if not exists
    os.makedirs(output_dir, exist_ok=True)

    # Sniff all json files in input directory and write schema structure to output directory
    for json_file in os.listdir(input_dir):
        if json_file.endswith(".json"):
            input_path = os.path.join(input_dir, json_file)
            output_path = os.path.join(
                output_dir, json_file.replace("data", "schema"))
            schema = process_json_file(input_path)
            write_schema_file(schema, output_path)


if __name__ == '__main__':
    input_dir = "./data"
    output_dir = "./schema"
    process_all_json_files(input_dir, output_dir)
