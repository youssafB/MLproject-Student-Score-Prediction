# this is for any fonctionalty written in  a common way 

import pickle


# this fucntion is responsible for  svaing  any object to a file using pickle:

def save_object(obj, file_path):
    """
    Save an object to a file using pickle.

    Parameters:
    - obj: The object to be saved.
    - file_path (str): The path to the file where the object will be saved.
    """
    with open(file_path, 'wb') as file:
        pickle.dump(obj, file)
    print(f"Object saved to {file_path}")


