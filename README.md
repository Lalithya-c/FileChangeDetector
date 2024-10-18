# Directory Change Detection Tool

This Python tool monitors a specified directory for changes in files. It calculates the SHA-256 hash of each file and compares the current state with a previously saved state, reporting any additions, modifications, or removals.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/lalithya-c/filechangedetector.git
   ```

2. Navigate to the project directory:
   ```bash
   cd repo-name
   ```

3. (Optional) Set up a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

## Usage

To use the Directory Change Detection Tool, run the script in your terminal:

```bash
python detectfilechanges.py
```

### Example

1. Run the script, and when prompted, enter the path of the directory you want to monitor.
2. The tool will check for changes, including any files that were added, modified, or removed, and display the results in the terminal.

## Functions

### `list_files(directory)`

- **Description**: Lists all files in the specified directory and calculates their SHA-256 hashes.
- **Parameters**: `directory` (str): The path to the directory.

### `calculate_file_hash(file_path)`

- **Description**: Computes the SHA-256 hash of a file.
- **Parameters**: `file_path` (str): The path to the file.
- **Returns**: The SHA-256 hash of the file content.

### `save_state(directory)`

- **Description**: Saves the current state of the directory (file paths and hashes) to a JSON file named `file_state.json`.

### `load_state()`

- **Description**: Loads the previously saved state from `file_state.json`.

### `detect_changes(directory)`

- **Description**: Compares the current state of the directory with the previously saved state and prints any changes (additions, modifications, removals) along with the user who made the changes.


