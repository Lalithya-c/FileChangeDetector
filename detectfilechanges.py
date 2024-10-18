import os
import hashlib
import getpass
import json

# get file names and their hashes in a directory path
def list_files(directory):
    files = []
    file_hashes = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(root,filename)
            file_hash = calculate_file_hash(file_path)
            files.append(file_path)
            file_hashes.append(file_hash)
    return dict(zip(files, file_hashes))

# calculate the hash of each file
def calculate_file_hash(file_path):
    try:
        with open(file_path, "rb") as f:
            file_content = f.read()
            return hashlib.sha256(file_content).hexdigest()
    except FileNotFoundError:
        return None
    
# to save the current state into a json file
def save_state(directory):
    file_state = list_files(directory)
    with open("file_state.json", "w") as f:
        json.dump(file_state, f, indent=4)

# fetch details of previously saved state from json file
def load_state():
    with open("file_state.json", "r") as f:
        return json.load(f)
    
# compare the current state with previous state
def detect_changes(directory):
    current_state = list_files(directory)
    previous_state = load_state()

    user = getpass.getuser() # to get the user who made the change in the directory
    #print("Current State:", current_state)
    #print("Previous State:", previous_state)


    for file, hash in current_state.items():
        if file not in previous_state:
            print(f"Added: {file} by {user}")
        elif previous_state[file] != hash:
            print(f"Modified: {file} by {user}")

    for file in previous_state:
        if file not in current_state:
            print(f"Removed: {file} by {user}")


# Prompt the user to enter a directory path
directory_path = input("Please enter the directory path: ")

# Check if the directory exists
if os.path.isdir(directory_path):
    print(f"The directory '{directory_path}' exists.")
else:
    print(f"The directory '{directory_path}' does not exist.")

# Check if the state file exists; if not, save the initial state
if not os.path.exists("file_state.json"):
    save_state(directory_path)

# Detect changes
detect_changes(directory_path)

# Save the current state again after checking for changes
save_state(directory_path)
