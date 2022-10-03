def read_text_fromfile(file_path: str, default: str) -> str:
    try:
        with open(file_path) as f:
            data = f.read()
            try:
                text_data = data.decode('utf-8')
                if text_data:
                    return text_data
            except UnicodeDecodeError:
                pass
    except FileNotFoundError:
        pass
    return default