# JSON Schema Generator

This is a Python program that generates JSON Schema definitions from a collection of JSON files.

## Installation

1. Clone this repository or download the ZIP file and extract it to your desired location.
2. Make sure you have Python 3.6 or later installed.

## Usage
1. Place your JSON files in the data directory.
2. cd into the repo folder
3. Run the program with the following command:

```bash
python main.py
```

The generated schema files will be placed in the schema directory.

## Error Handling

The program includes error handling for the following scenarios:

1. The input file is not a valid JSON file.
2. The JSON data file does not have a "message" key.

If any of these errors occur, terminate silently.

Conversely, if any of the following errors occur, the program will raise an exception and terminate.

1. The input directory specified does not exist.
2. The output directory specified does not exist and cannot be created.
3. The schema file cannot be written due to permission issues.

## Unit Tests
This program includes unit tests to ensure that it functions correctly. To run the tests, use the following command:

```bash
python test.py
```


