def read_secret(file_path: str) -> str:
    with open(file_path) as f:
        data = f.read()
        if data:
            return data.strip()
        else:
            raise ValueError(f"Secret file {file_path} is empty")