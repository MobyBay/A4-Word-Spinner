# Name: Hongbei Meng
# GitHub: PASTE_YOUR_PRIVATE_REPOSITORY_LINK_HERE

import string
from Spinner import Spinner


# Read a text file, remove punctuation, and convert it to lowercase.
def read_clean_text(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    for punctuation in string.punctuation:
        text = text.replace(punctuation, "")

    return " ".join(text.lower().split())


# Run the word spinner on essay.txt and print three new versions.
def main():
    original_text = read_clean_text("essay.txt")
    print("Original:", original_text)

    spinner = Spinner("synonyms-simplified.txt")
    spinner.setText(original_text)

    for version in range(1, 4):
        print(f"Version {version}")
        spinner.spin()
        print(spinner.getText())


if __name__ == "__main__":
    main()
