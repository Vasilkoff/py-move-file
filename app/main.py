import os


def move_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) != 3:
        raise ValueError(...)
    cmd, old_file, new_file = parts
    if not cmd == "mv":
        return
    with open(old_file, "r") as old_f:
        folder = os.path.dirname(new_file)
        if folder:
            os.makedirs(folder, exist_ok=True)

        with open(new_file, "w") as new_f:
            new_f.write(old_f.read())

    os.remove(old_file)
