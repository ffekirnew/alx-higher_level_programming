#!/usr/bin/python3
"""Contains class definition for the class Base."""


import json
import os
import tkinter


class Base:
    """Define the class base.

    Class Attribues:
    ----------------
    __nb_objects - keeps track of the number of object of the class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize an instance of the class Base."""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries): 
        """Return the JSON string representation of list_dictionaries"""
        import json
        json_string = json.dumps(list_dictionaries)
        return json_string

    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        with open(cls, 'w') as f:
            json.dump(list_objs, f)

    @staticmethod
    def from_json_string(json_string):
        """Returns a list of the JSON string representation json_string."""

        # If json_string is an empty string, return an empty list
        if json_string == "":
            return []

        # Convert JSON string to list
        json_list = json_string.split(',')

        # Create empty list to store each dictionary representation
        output_list = []

        for item in json_list:
            dictionary = json.loads(item)
            output_list.append(dictionary)

        return output_list

    def load_from_file(cls):
        """Returns a list of instances from the named class given.

        Params: 
        cls (Class): The named class to instantiate objects from

        Returns: 
        entities_list (list): List of instantiated objects
        """

        if not os.path.isfile(cls.__name__ + ".json"):
            return []

        try:
            with open(cls.__name__ + ".json", 'r', encoding='utf-8') as f:
                json_string = f.read()
                list_from_json = cls.from_json_string(json_string)
            return list_from_json
        except:
            return []

    def save_to_file_csv(cls, list_objs):
        """Serializes and saves to the named class given, the list of objects."""

        # Check if the CSV file exists. If not, create it.
        if not os.path.isfile(cls.__name__ + ".csv"):
            open(cls.__name__ + ".csv", 'a', encoding='utf-8').close()

        csv_list = []

        # Serialize each object in list_objs to CSV format
        for obj in list_objs:
            # Get data from object
            obj_dict = obj.to_dictionary()

        # Convert dictionary to a row of each key-value pair in order
        csv_row = ""
        # Iterate through keys in order
        for key in cls.list_keys:
            # Get value associated with key and format it correctly
            if type(obj_dict[key]) != str: 
                val = '"' + str(obj_dict[key]) + '"'
            else: 
                val = obj_dict[key]

        # If not first column, add leading comma
        if csv_row != "":
            csv_row += ","

        # Add key-value pair to row string
        csv_row += val

        # Append row to CSV list of rows
        csv_list.append(csv_row)

        try:
            # Join the CSV list with newline and write to file with utf-8 encoding
            with open(cls.__name__ + ".csv", 'w', encoding='utf-8') as f:
                f.write('\n'.join(csv_list))
        except OSError as e:
            print(f'Failed to save file: {e}')


    def load_from_file_csv(cls):
        """Deserializes and loads from the named class given a CSV file."""

        # Check that the CSV file exists
        if not os.path.isfile(cls.__name__ + ".csv"):
            return []

        try:
            entities = []

            # Open file for reading with utf-8 encoding and read into string lines
            with open(cls.__name__ + ".csv", 'r', encoding='utf-8') as f:
                lines = f.read().split('\n')

            # Iterate through string lines of CSV, create objects, and append them to entities list
            for line in lines:
                values = line.split(',')
                entity = cls(*values)
                entities.append(entity)

            return entities

        except OSError as e:
            print(f'Failed to read file: {e}')

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares given."""

        # Set up Window dimensions and variables before drawing 
        width = 800
        height = 600
        root = tkinter.Tk.Tk()

        # Create canvas object using Window size information
        canvas = tkinter.Canvas(root, width = width, height = height)
        canvas.pack()

        # Iterate through list of Rectangle objects to draw them on canvas 
        for rect in list_rectangles:
            top_left_x = rect.position[0]
            top_left_y = rect.position[1]
            w = rect.width
            h = rect.height

        # Create rectangle on canvas with those parameters
        canvas.create_rectangle(top_left_x, top_left_y, top_left_x + w, top_left_y + h)

        # Iterate through list of Square objects to draw them on canvas 
        for sq in list_squares:
            top_left_x = sq.position[0]
            top_left_y = sq.position[1]
            side = sq.side

        # Create square on canvas with those parameters
        canvas.create_rectangle(top_left_x, top_left_y, top_left_x + side, top_left_y + side)

        # Displays the window with all shapes drawn on it  
        root.mainloop()
