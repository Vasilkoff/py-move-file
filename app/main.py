import os


def move_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) != 3:
        raise ValueError('wrong command')
    cmd, old_file, new_file = parts
    if not cmd == "mv":
        return



    with open(old_file, "r") as old_f:
        new_path = new_file
        if new_file.endswith('/'):
             new_path = os.path.join(new_file, os.path.basename(old_file))

        folder = os.path.dirname(new_path)
        if folder:
            os.makedirs(folder, exist_ok=True)

        with open(new_path, "w") as new_f:
            new_f.write(old_f.read())
        pass

    os.remove(old_file)
