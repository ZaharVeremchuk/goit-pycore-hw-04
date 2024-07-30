import sys
from pathlib import Path

try:
    from colorama import init, Fore
except ImportError:
    print("Please install colorama using: pip install colorama")
    sys.exit(1)

# Initialize colorama for colored output
init(autoreset=True)

def explore_directory(path_to_dir, level=0):
    actual_path = Path(path_to_dir)

    if not actual_path.exists() or not actual_path.is_dir():
        print(Fore.RED + f"Path '{path_to_dir}' does not exist or it is not a directory.")
        return

    print(" " * level + Fore.BLUE + f"📂 {actual_path.name}/")

    for element in actual_path.iterdir():
        if element.is_dir():
            print(" " * (level + 2) + Fore.CYAN + f"📂 {element.name}/")
            explore_directory(element, level + 4)
        elif element.is_file():
            print(" " * (level + 2) + Fore.GREEN + f"📄 {element.name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{Fore.RED} Please specify the path to a directory.")
        sys.exit(1)

    path_argument = sys.argv[1]

    explore_directory(path_argument)