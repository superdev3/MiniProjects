from rich import print, os
res = []
for path in os.listdir(fr"{os.getcwd()}"): 
    if os.path.isfile(os.path.join(fr"{os.getcwd()}", path)): res.append(path)
try:
    for i in range(0, len(res)):
        if "." not in res[i] or res[i] == str(__file__): continue
        os.rename(str(res[i]), f"file_{i}.{str(res[i]).split('.')[1]}")
except Exception as e:print(f"[red]{e}[/red]")
