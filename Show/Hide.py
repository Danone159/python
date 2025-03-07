# zle zadanie
def main():
    with open("data k ulohe 6.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f]

    count = int(lines[0])
    records = lines[1:count + 1]
    removed = [False] * count
    toggle_indices = list(map(int, lines[count + 1:]))

    for index in toggle_indices:
        if index == -1:
            break
        if 0 <= index < count:
            removed[index] = not removed[index]

    for i, record in enumerate(records):
        if not removed[i]:
            print(record)

if __name__ == "__main__":
    main()
