# Mini Projects


## File Sorter

**How to use:**
> The file sorter can moved to a directory that you want to sort. Then run the file and wait for a confirmation that it has completed sorting.

**How does it work?**
> After it has been moved to the directory that needs to be sorted, it loops through all the files in the directory and adds them to the res array. Then it loops through the array and renames every file to a format based on their index in the array.

**Why was this created?**

> As a photographer you often deal with thousands of photos in just one folder. You need to sort these to be able to manage and reference these images. Therefore I created this small Python script to do that for me.



## Spelling Checker

**How to use:**
> First you have to open a terminal and run `pip install rich` and `pip install english_words`. Now you can run the Spelling Checker file and it will open a terminal window. 

**How does it work?**

> After it has been run it takes an input (The sentence to be checked), then it splits the user input by spaces and adds them to the anonymous array. After which it loops through the array and checks if the word is correct. Based on whether the word is correct or not it will add it to a new array called checkedWorldList. Then it can turn the array into a string and display it in standard output. After which the program loops back and the process restarts.

**Why was this created?**

> Unlike most of my Mini Projects this one didn't have a good reason for its creation. The main reason this was created was to test the rich library and the english_words library. This can be refactored in the future to be part of a text input or something similar to a spell highlighter.
