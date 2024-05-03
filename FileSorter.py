from rich import print
import os

FileArray = []
for path in os.listdir(fr"{os.getcwd()}"): 
    if os.path.isfile(os.path.join(fr"{os.getcwd()}", path)): 
        FileArray.append(path)
try:
    for i in range(0, len(res)):
        if "." not in FileArray[i] or FileArray[i] == str(__file__): 
            continue
        os.rename(str(FileArray[i]), f"file_{i}.{str(FileArray[i]).split('.')[1]}")
except Exception as exception:
    print(f"[red]{exception}[/red]")
