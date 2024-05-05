# Mini Projects

**General Information:**
> This repository houses a collection of smaller projects that I believe don't require their own repository. For detailed information about each script, please take a look at the README.md file.


## File Sorter

**How to use:**
> The file sorter can moved to a directory that you want to sort. Then run the file and wait for a confirmation that it has completed sorting.

**How does it work?**
> After it has been moved to the directory that needs to be sorted, it loops through all the files in the directory and adds them to the res array. Then it loops through the array and renames every file to a format based on their index in the array.

**Why was this created?**

> As a photographer you often deal with thousands of photos in just one folder. You need to sort these to be able to manage and reference these images. Therefore I created this small Python script to do that for me.



## Spelling Checker

**How to use:**
> First you have to open a terminal and run `pip install rich` and `pip install english_words`. Now you can run the Spelling Checker file and it will open a terminal window. After it has been run, it will ask you for a sentence to check. Press enter and it will show you in Green all the correct words and in red all the incorrect words. To end the program you can press the little `x` in the top right of the window, or you can press `ALT + F4`.

**How does it work?**

> After it has been run it takes an input (The sentence to be checked), then it splits the user input by spaces and adds them to the anonymous array. After which it loops through the array and checks if the word is correct. Based on whether the word is correct or not it will add it to a new array called checkedWorldList. Then it can turn the array into a string and display it in standard output. After which the program loops back and the process restarts.

**Why was this created?**

> Unlike most of my Mini Projects this one didn't have a good reason for its creation. The main reason this was created was to test the rich library and the english_words library. This can be refactored in the future to be part of a text input or something similar to a spell highlighter.



## Phone Number Tracer

**How to use:**
> First you have to open a terminal and run `pip install phonenumbers`. Now you can run the Phone Number Tracer file and it will open a terminal window. After it has been run, it will ask you for a phone number to trace. Press enter and you should see the Geolocation of where the Simcard linked to that phone number is or is registered. To end the program you can press the little `x` in the top right of the window, or you can press `ALT + F4`.

**How does it work?**

> After receiving the input, the number is passed to the phonenumbers.geocoder library. Then the returned string is printed to the Standard Output. Then the loop repeats.

**Why was this created?**

> The reason for the creation of this truly small project is that I saw a YouTube Short showing this library and its commands. This project was to test the library. I felt that its useful to upload and show others.



## Ip Address Geo Locator

**How to use:**
> You can run the IP Address Geo Locator file and it will open a terminal window. After it has been run, it will ask you for an `IpV4 Address` to trace. Press enter and you should see the general public information about the IP address. This includes City, Region, Country, Location, Time zone, ASN and Google Maps Link to Geolocation. The Geolocation is not accurate but is most likely to be in the right country. To end the program you can press the little `x` in the top right of the window, or you can press `ALT + F4`.

**How does it work?**

> After receiving the input, the program sends a Get HTTPS request to `https://ipinfo.io/` (Example: `https://ipinfo.io/{ip_address}/json`). Then it uses F Strings to print the information to the terminal. Then this repeats.

**Why was this created?**

> There is no direct reason for the creation of this project. However, this was strongly inspired by Spelis (https://github.com/Spelis/simple/blob/main/geolocator/main.py) who is my friend and is aware and consented to this being refactored and uploaded to my Github.
