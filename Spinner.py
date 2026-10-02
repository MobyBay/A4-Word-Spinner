# Name: Hongbei Meng
# u1617689
import random


class Spinner:
    # Create a Spinner and build the synonym dictionary from a file.
    def __init__(self, synonym_file: str):
        self.synonyms = {}
        self.text = ""

        with open(synonym_file, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                word, synonym_text = line.split(":", 1)
                synonym_list = synonym_text.split(",") if synonym_text else []
                self.synonyms[word] = synonym_list

    # Store the text that will be changed by spin().
    def setText(self, text: str):
        self.text = text

    # Randomly replace words in the current text with synonyms.
    def spin(self):
        words = self.text.split()
        spun_words = []

        for word in words:
            if word in self.synonyms and self.synonyms[word]:
                if random.random() < 0.5:
                    word = random.choice(self.synonyms[word])
            spun_words.append(word)

        self.text = " ".join(spun_words)

    # Return the current text stored by the Spinner.
    def getText(self) -> str:
        return self.text
