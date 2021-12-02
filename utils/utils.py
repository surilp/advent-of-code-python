def file_to_collection(input_file):
    result = []
    with open(input_file, 'r') as file:
        item = file.readline()
        while item:
            result.append(item.strip())
            item = file.readline()
        return result

