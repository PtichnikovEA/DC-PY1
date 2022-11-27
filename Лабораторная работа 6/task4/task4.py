import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='\n') -> list[dict]:
    rows = []
    headers = []
    with open(filename) as f:  # Прочитать файл
        row = f.readline()
        if not row:
            return []
        else:
            headers = row.replace('\n','').split(delimiter)  # Принимаем первую прочитанную строку за строку заголовков
        row = f.readline()
        while row:  # Читаем строки данных и записываем их в отдельный список
            rows.append(row.replace('\n','').split(delimiter))
            row = f.readline()
    return [{headers[i]: item[i] for i in range(0, len(item))} for item in rows]  # Генерируем список объектов
    # TODO реализовать конвертер из csv в json


print(json.dumps(csv_to_list_dict(INPUT_FILE, delimiter=',', new_line='\n'), indent=4))
