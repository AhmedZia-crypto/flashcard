class Flashcard():
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return self.word + self.meaning
    
list1 = []
while True:
    word = input("Please enter a word: " )
    meaning = input("Please enter the meaning of the word: " )
    obj1 = Flashcard(word, meaning)
    list1.append(obj1)
    a = input("Do you want to continue: Yes/No: ")
    if a == "Yes":
        continue
    else:
        break


for i in list1:
    print(i) 