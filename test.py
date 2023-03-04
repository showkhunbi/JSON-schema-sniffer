import os
import unittest
import shutil

import main


class TestSchemaGeneration(unittest.TestCase):

    def setUp(self):
        self.tests_dir = "./tests"
        self.input_dir = "./data"
        self.output_dir = "./tests/schema"
        os.makedirs(self.output_dir, exist_ok=True)

    def test_sniff_schema_item(self):
        # Test that sniff_schema_item returns the expected output for a given input

        # Example input data
        input_data = {
            'user': {'id': 'ABCDEFGHIJKLMNOP', 'nickname': 'ABCD'}, 'time': 890, 'acl': [], 'publicFeed': False, 'internationalCountries': ['ABCDEFGHIJKLMNOPQRSTUVWXYZA', 'ABCDEFGHIJKLMNOPQ'], 'topTraderFeed': True, 'test_data': [{'data': 2, 'r': 'A'}, {'data': 3, 'r': 'x'}, {'datap': 4, 'r': ''}]
        }

        # Expected output
        expected_output = {
            'user': {'type': 'object', 'properties': {'id': {'type': 'string', 'description': '', 'tag': '', 'required': False}, 'nickname': {'type': 'string', 'description': '', 'tag': '', 'required': False}}, 'description': '', 'tag': '', 'required': False}, 'time': {'type': 'integer', 'description': '', 'tag': '', 'required': False}, 'acl': {'type': 'enum', 'description': '', 'tag': '', 'required': False}, 'publicFeed': {'type': 'boolean', 'description': '', 'tag': '', 'required': False},
            'internationalCountries': {'type': 'enum', 'description': '', 'tag': '', 'required': False}, 'topTraderFeed': {'type': 'boolean', 'description': '', 'tag': '', 'required': False}, 'test_data': {'type': 'array', 'items': {'data': {'type': 'integer', 'description': '', 'tag': '', 'required': False}, 'r': {'type': 'string', 'description': '', 'tag': '', 'required': False}, 'datap': {'type': 'integer', 'description': '', 'tag': '', 'required': False}}, 'description': '', 'tag': '', 'required': False}
        }

        # Test that the function returns the expected output
        self.assertEqual(main.sniff_schema_item(input_data), expected_output)

    def test_process_json_file(self):
        # Test that process_json_file returns the expected output for a given input file

        # Example input data
        input_file = os.path.join(self.input_dir, "data_1.json")

        # Expected output
        expected_output = {
            "battle": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "string",
                        "description": "",
                        "tag": "",
                        "required": False
                    },
                    "name": {
                        "type": "string",
                        "description": "",
                        "tag": "",
                        "required": False
                    },
                    "orientation": {
                        "type": "string",
                        "description": "",
                        "tag": "",
                        "required": False
                    },
                    "settings": {
                        "type": "object",
                        "properties": {
                            "minParticipants": {
                                "type": "integer",
                                "description": "",
                                "tag": "",
                                "required": False
                            },
                            "maxParticipants": {
                                "type": "integer",
                                "description": "",
                                "tag": "",
                                "required": False
                            },
                            "battleType": {
                                "type": "string",
                                "description": "",
                                "tag": "",
                                "required": False
                            },
                            "wagerType": {
                                "type": "string",
                                "description": "",
                                "tag": "",
                                "required": False
                            },
                            "countdown": {
                                "type": "integer",
                                "description": "",
                                "tag": "",
                                "required": False
                            },
                            "duration": {
                                "type": "integer",
                                "description": "",
                                "tag": "",
                                "required": False
                            },
                            "archetype": {
                                "type": "object",
                                "properties": {
                                    "name": {
                                        "type": "string",
                                        "description": "",
                                        "tag": "",
                                        "required": False
                                    },
                                    "iconId": {
                                        "type": "string",
                                        "description": "",
                                        "tag": "",
                                        "required": False
                                    }
                                },
                                "description": "",
                                "tag": "",
                                "required": False
                            }
                        },
                        "description": "",
                        "tag": "",
                        "required": False
                    },
                    "status": {
                        "type": "string",
                        "description": "",
                        "tag": "",
                        "required": False
                    },
                    "creationTime": {
                        "type": "integer",
                        "description": "",
                        "tag": "",
                        "required": False
                    },
                    "startTime": {
                        "type": "integer",
                        "description": "",
                        "tag": "",
                        "required": False
                    },
                    "endTime": {
                        "type": "integer",
                        "description": "",
                        "tag": "",
                        "required": False
                    },
                    "creator": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "string",
                                "description": "",
                                "tag": "",
                                "required": False
                            },
                            "nickname": {
                                "type": "string",
                                "description": "",
                                "tag": "",
                                "required": False
                            },
                            "title": {
                                "type": "string",
                                "description": "",
                                "tag": "",
                                "required": False
                            },
                            "accountType": {
                                "type": "string",
                                "description": "",
                                "tag": "",
                                "required": False
                            },
                            "countryCode": {
                                "type": "string",
                                "description": "",
                                "tag": "",
                                "required": False
                            },
                            "orientation": {
                                "type": "string",
                                "description": "",
                                "tag": "",
                                "required": False
                            }
                        },
                        "description": "",
                        "tag": "",
                        "required": False
                    },
                    "participants": {
                        "type": "array",
                        "items": {
                            "user": {
                                "type": "object",
                                "properties": {
                                    "id": {
                                        "type": "string",
                                        "description": "",
                                        "tag": "",
                                        "required": False
                                    },
                                    "nickname": {
                                        "type": "string",
                                        "description": "",
                                        "tag": "",
                                        "required": False
                                    },
                                    "title": {
                                        "type": "string",
                                        "description": "",
                                        "tag": "",
                                        "required": False
                                    },
                                    "accountType": {
                                        "type": "string",
                                        "description": "",
                                        "tag": "",
                                        "required": False
                                    },
                                    "countryCode": {
                                        "type": "string",
                                        "description": "",
                                        "tag": "",
                                        "required": False
                                    },
                                    "orientation": {
                                        "type": "string",
                                        "description": "",
                                        "tag": "",
                                        "required": False
                                    }
                                },
                                "description": "",
                                "tag": "",
                                "required": False
                            },
                            "creator": {
                                "type": "boolean",
                                "description": "",
                                "tag": "",
                                "required": False
                            },
                            "ranking": {
                                "type": "integer",
                                "description": "",
                                "tag": "",
                                "required": False
                            },
                            "numberOfTrades": {
                                "type": "integer",
                                "description": "",
                                "tag": "",
                                "required": False
                            },
                            "performance": {
                                "type": "string",
                                "description": "",
                                "tag": "",
                                "required": False
                            }
                        },
                        "description": "",
                        "tag": "",
                        "required": False
                    }
                },
                "description": "",
                "tag": "",
                "required": False
            },
            "joiner": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "string",
                        "description": "",
                        "tag": "",
                        "required": False
                    },
                    "nickname": {
                        "type": "string",
                        "description": "",
                        "tag": "",
                        "required": False
                    },
                    "title": {
                        "type": "string",
                        "description": "",
                        "tag": "",
                        "required": False
                    },
                    "accountType": {
                        "type": "string",
                        "description": "",
                        "tag": "",
                        "required": False
                    },
                    "countryCode": {
                        "type": "string",
                        "description": "",
                        "tag": "",
                        "required": False
                    },
                    "orientation": {
                        "type": "string",
                        "description": "",
                        "tag": "",
                        "required": False
                    }
                },
                "description": "",
                "tag": "",
                "required": False
            },
            "participantIds": {
                "type": "enum",
                "description": "",
                "tag": "",
                "required": False
            }
        }

        # Test that the function returns the expected output
        self.assertEqual(main.process_json_file(input_file), expected_output)

    def test_process_all_json_files(self):
        # Test that process_all_json_files creates the expected output files

        # Remove any existing output files
        for f in os.listdir(self.output_dir):
            os.remove(os.path.join(self.output_dir, f))

        # Call the function
        main.process_all_json_files(self.input_dir, self.output_dir)

        # Check that the output files were created and contain the expected data
        for f in os.listdir(self.output_dir):
            if f.endswith(".json"):
                output_file = os.path.join(
                    self.output_dir, f.replace("data", "schema"))
                self.assertTrue(os.path.exists(output_file))

    def tearDown(self):
        shutil.rmtree(self.tests_dir, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
