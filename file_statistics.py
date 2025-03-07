def analyze_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.readlines()

        line_count = len(content)
        word_count = sum(len(line.split()) for line in content)
        char_count = sum(len(line) for line in content)

        print(f"Riadky v súbore: {line_count}")
        print(f"Slová v súbore: {word_count}")
        print(f"Znaky v súbore: {char_count}")

    except FileNotFoundError:
        print(f"Chyba: Súbor '{filename}' sa nenašiel.")

file_input = "data_k_ulohe_3.txt"
analyze_file(file_input)
