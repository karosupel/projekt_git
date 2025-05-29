import sys
import json
import yaml
import xmltodict

def read_file(path):
    ext = path.lower().split('.')[-1]
    with open(path, 'r', encoding='utf-8') as f:
        if ext == 'json':
            return json.load(f)
        elif ext in ('yaml', 'yml'):
            return yaml.safe_load(f)
        elif ext == 'xml':
            return xmltodict.parse(f.read())
        else:
            raise ValueError(f"Nieobsługiwany format wejściowy: {ext}")

def write_file(data, path):
    ext = path.lower().split('.')[-1]
    with open(path, 'w', encoding='utf-8') as f:
        if ext == 'json':
            json.dump(data, f, indent=2, ensure_ascii=False)
        elif ext in ('yaml', 'yml'):
            yaml.dump(data, f, allow_unicode=True)
        elif ext == 'xml':
            xml_str = xmltodict.unparse(data, pretty=True)
            f.write(xml_str)
        else:
            raise ValueError(f"Nieobsługiwany format wyjściowy: {ext}")

def main():
    if len(sys.argv) != 3:
        print("Użycie: program.exe pathToFile1 pathToFile2")
        sys.exit(1)
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    data = read_file(input_path)
    # xmltodict.parse zwraca słownik z jednym głównym kluczem, upraszczam jeśli to możliwe
    if isinstance(data, dict) and len(data) == 1 and output_path.lower().endswith('.xml') is False:
        # upraszczam strukturę dla json/yaml
        data = list(data.values())[0]
    if output_path.lower().endswith('.xml'):
        # xmltodict.unparse wymaga głównego klucza
        if not (isinstance(data, dict) and len(data) == 1):
            data = {'root': data}
    write_file(data, output_path)
    print(f"Plik został przekonwertowany: {output_path}")

if __name__ == "__main__":
    main()