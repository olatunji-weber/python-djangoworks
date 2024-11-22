from pathlib import Path

q = Path()
p = Path("FileZone")
p.mkdir()
print("Directory is created....")
print("Here are the files and folders in this directory:\n")
for file in q.glob("*"):
    print(file)
p.rmdir()
print("The Directory is removed...")