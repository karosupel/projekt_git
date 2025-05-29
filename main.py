import sys
import json

def read_file(path):
    ext = path.lower().split('.')[-1]
    with open(path, 'r', encoding='utf-8') as f:
        if ext == 'json':
            return json.load(f)

def main():
    if len(sys.argv) != 3:
        print("Użycie: program.exe pathToFile1 pathToFile2")
        sys.exit(1)
    input_path = sys.argv[1]
    output_path = sys.argv[2]