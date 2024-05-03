from english_words import get_english_words_set
from rich import print

wordList = get_english_words_set(['web2'], lower=True)

def CheckWords(argWordList: str) -> list[str]:
    """Checks if words are correct by looping through provided string and checking if the lowered string is in the Standard English Dictionary"""
    
    checked = []
    
    for word in argWordList.split():
        if word.casefold() in wordList:
            checked.append(f"[green]{word}[/green]")
        else:
            checked.append(f"[red]{word}[/red]")

    return checked

# Main Loop
while True:
    userInput = input("Please type in a sentence and press enter to check: ")
    
    checkedWorldList = CheckWords(userInput)
    
    # Turns List to string
    consoleOutput = " ".join(checkedWorldList)
    
    print(consoleOutput)

