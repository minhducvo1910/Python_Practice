'''Pathlib practice: '''

import os
from pathlib import Path

'''print(Path.cwd())
for p in Path().iterdir():
    print(p)'''

'''
my_dir = path("Directory_1")
my_file = Path("file_1.txt")

new_file = my_dir / "new_file.txt"  ( my_dir.joinpath(...))

print(my_dir.suffix(name, stem,..))
print(my_file.exists())
print(new_file.parent.absoulte())
'''

#p = Path(__file__).resolve().parent.parent
dotfiles = Path.home() / "dotfiles"

#for p in dotfiles.rglob("*vscode*", case_sensitive=False):
    
p = Path("TempDir")
#p.mkdir(parents=True) #Create directory (create any parent directory on the way)
#p.rmdir() #Remove only empty directory
file = Path("temp_file.txt")
#file.touch()
#file.replace("temp_file.txt")
file.unlink()
