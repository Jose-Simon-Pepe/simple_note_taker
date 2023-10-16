import os,shutil
import sys
import datetime

class NoteTaker:

    def __init__(self,note_path:str,note_templ:str):
        self._notes_path = note_path
        self._notes_templ = note_templ

    def notes_path(self):
        return self._notes_path

    def notes_templ(self):
        return self._notes_templ

    def create_note(self,name:str):
        template = r"/home/peace/note_template.md"
        args = sys.argv[1:]

        # Este script crea una nota dentro del standard zettelk
        title_words = [word for word in args if not word.startswith("-")]
        tags = [word.replace("-", "#") for word in args if word.startswith("-")]
        print(tags)
    
        title = '_'.join(map(str, title_words))
    
        target = "/home/peace/notes/study/"+title+".md"
    
        if len(sys.argv[1:])==0:
            target = os.getcwd()+"/nonamednote.md"
    
        print("target is :",target)
        
        shutil.copyfile(template, target)
        new_first_line = "# "+" ".join(map(str,title_words))
        tags_end_line = " ".join(map(str,[tag for tag in tags if not tag=="#noedit"]))
        
        with open(target, "r") as file:
            lines = file.readlines()
        
        separator = "---"+"\n"
        
        lines[0] = separator
        lines[1] = "ID: "+str(hash(' '.join(map(str,title_words))))  + "\n"  # id
        print("ID: "+lines[1])
        lines[2] = "Date: "+str(datetime.datetime.now()) + "\n"
        lines[3] = new_first_line + "\n"  # Reemplazar la primera línea
        lines[4] = separator
        if "#noedit" in tags:
            lines[6] = "## Definiciones (se responde la duda del documento)\n"+" ".join(title_words)+"\n"
        lines[len(lines)-1] = tags_end_line
        
        with open(target, "w") as file:
            file.writelines(lines)
        if not "#noedit" in tags:
            os.system("nvim "+target)
