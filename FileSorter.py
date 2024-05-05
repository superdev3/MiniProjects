from rich import print
import os

FileArray = []

for path in os.listdir(fr"{os.getcwd()}"): 
    if os.path.isfile(os.path.join(fr"{os.getcwd()}", path)): 
        FileArray.append(path)
try:
    for i in range(0, len(FileArray)):
        if "." not in FileArray[i] or FileArray[i] == str(__file__): 
            continue
        
        new_file_name = f"File-{i+1}.{str(FileArray[i]).split('.')[1]}"
        os.rename(str(FileArray[i]), new_file_name)
        print(f"Renamed {FileArray[i]} -> {new_file_name}")
        
except Exception as exception:
    print(f"[red]{exception}[/red]")
