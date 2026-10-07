import os


def move_file(command: str) -> None:
    cmd, old_file, new_file = command.split(" ")

    if not cmd == "mv":
        return

    old_f = open(old_file, "r")

    folder = os.path.dirname(new_file)
    if folder:
        os.makedirs(folder, exist_ok=True)

    new_f = open(new_file, "w")

    new_f.write(old_f.read())

    new_f.close()
    old_f.close()

    os.remove(old_file)
