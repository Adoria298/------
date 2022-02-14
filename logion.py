from pathlib import Path
from random import choice

class Logion:
    def __init__(self, word_file, out_func, in_func):
        self._word_list = list(self.read_word_list(word_file))
        self.out = out_func
        self.inf = in_func
        self.word = self.get_word("NO WORDS IN LIST!")

    def play(self):
        for _ in range(6):
            guess = self.inf()[:5]
            answer = ""
            word = self.word["word"]
            for l, i in enumerate(guess):
                if l in self.word:
                    if self.word[i] == l:
                        answer += "🟩"
                    else:
                        answer += "🟨"
                else:
                    answer += "⬛"
            self.out(answer)
        self.out(self.word["word"], "which means", self.word["meaning"])
        
    def read_word_list(self, filepath):
        p = Path(filepath)
        if p.exists():
            with open(p, "rt", encoding="utf8") as f:
                for line in f.readlines():
                    line = line.rstrip()
                    if len(line) < 1 or line[0] == "#":
                        continue
                    splitted = line.split(" - ")
                    yield {"word": splitted[0], "meaning": splitted[1]}

    def get_word(self, error):
        #try:
        return choice(self._word_list)
        #except:
        #    raise ValueError(error)

if __name__ == "__main__":
    Λ = Logion("words.txt", print, (lambda: input("guess: ")))
    Λ.play()