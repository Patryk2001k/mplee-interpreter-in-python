import os
import sys
import subprocess
from mplee_interpreter.interpreter import run

def find_python_path():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    while True:
        candidate = os.path.join(current_dir, "Python_package", "python.exe")
        if os.path.exists(candidate):
            return candidate
        
        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir: 
            break
        current_dir = parent_dir
    
    raise FileNotFoundError("Not found 'Python_package/python.exe' in path")

PYTHON_PATH = find_python_path()

def load_from_file(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File {filename} doesn't exist")
    
    
    with open(filename, "r") as file:
        code = file.read()
        
    return code

def execute_python_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Python file {file_path} doesn't exist")
    
    try:
        result = subprocess.run([PYTHON_PATH, file_path], capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)
    except Exception as e:
        print(f"Failed to execute Python file: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    filename = sys.argv[1]
    if filename.endswith(".py"):
        execute_python_file(filename)
    elif filename.endswith(".mplee"):
        code = load_from_file(filename)
        _, error = run(filename, code)
        if error:
            print(error.as_string())
    else:
        print(f"Unsupported file type: {filename}. Use .mplee or .py")
        sys.exit(1)
