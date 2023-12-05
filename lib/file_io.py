def write_file(file_name, file_content):
    file_name = str(file_name) + ".txt"
    
    try:
        with open(file_name, "w") as file:
            file.write(file_content)
        print(f"File '{file_name}' has been written successfully.")
    except Exception as e:
        print(f"Error writing to '{file_name}': {e}")

def append_file(file_name, append_content):
    file_name = str(file_name) + ".txt"
    
    try:
        with open(file_name, "a") as file:
            file.write(append_content + "\n")
        print(f"Content appended to '{file_name}' successfully.")
    except Exception as e:
        print(f"Error appending to '{file_name}': {e}")

def read_file(file_name):
    file_name = str(file_name) + ".txt"
    
    try:
        
        with open(file_name, "r") as file:
            content = file.read()
        return content
    except Exception as e:
        print(f"Error reading '{file_name}': {e}")
        return None
