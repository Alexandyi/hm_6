import sys
from pathlib import Path

dct={'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'e',
      'ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n',
      'о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h',
      'ц':'c','ч':'cz','ш':'sh','щ':'scz','ъ':'','ы':'y','ь':'','э':'e',
      'ю':'u','я':'ja', 'А':'A','Б':'B','В':'V','Г':'G','Д':'D','Е':'E','Ё':'E',
      'Ж':'ZH','З':'Z','И':'I','Й':'I','К':'K','Л':'L','М':'M','Н':'N',
      'О':'O','П':'P','Р':'R','С':'S','Т':'T','У':'U','Ф':'F','Х':'H',
      'Ц':'C','Ч':'CZ','Ш':'SH','Щ':'SCH','Ъ':'','Ы':'y','Ь':'','Э':'E',
      'Ю':'U','Я':'YA'
      }
types={"Audio": [".mp3", ".ogg", ".wav", ".amr"],
       "Docs": [".doc",".pptx",".xlsx",".docx", ".txt", ".pdf"],
       "Arh":[".zip",".gz",".tag"],
       "Video":[".avi",".mp4",".mov",".mkv"],
       "Foto":[".jpej",".png",".jpg",".svg"]         
       }
 
def normalize(str) -> str:
    ext = str.translate(dct)
    for i in ext:
        if ord(i)>90 or ord(i)<41:
            if ord(i)>122 or ord(i)<97:
                if not ord(i)>47 and not ord(i)<58:
                    i="_"

    print(ext)
    for i, j in types.items():
        if ext in j:
            return i
    return "Other"
 

def movefile(file:Path, category:str, root:Path) -> None:
    target = root.joinpath(category)
    if not target.exists():
        target.mkdir()
    new_path = target.joinpath(file.name)
    if not new_path.exists():
        file.replace(new_path)


def sort_folder(path:Path) -> None:
    for el in path.glob("**/*"):
        if el.is_file():
            category = normalize(el)
            movefile(el, category, path)

def main() -> str:
    try:
        path = Path(sys.argv[1])
    except IndexError:
        return "No path to folder."
    
    if not path.exists():
        return "Folder doesn't exist."
    
    sort_folder(path)
    
    return "Ok"

if __name__=='__main__':
    print(main())