import os,shutil
from simple_note_taker.src.domain.note import Note
from simple_note_taker.src.infra.ports.repo_notes import RepoNotes
import sys
import datetime
from simple_note_taker.src.infra.ports.editor import EDITOR

class NoteTaker:


    def __init__(self,note_path:str,note_templ:str):
        self._notes_path = note_path
        self._notes_templ = note_templ
        self._tags = list()
        self.editor:EDITOR = None
        self._id:int = 0
        self._repo = None

    def set_repo(self,repo:RepoNotes):
        self._repo = repo
        return self

    def id(self):
        return self._id

    def set_editor(self,editor:EDITOR):
        self.editor = editor 

    def notes_path(self):
        return self._notes_path

    def notes_templ(self):
        return self._notes_templ


    def _verify_unicity(self,name:str):
        if self._repo.exists(name,self._notes_path):
            raise DuplicatedNoteError("Duplicated note")

    def create_note(self,name:str):
        """ Este script crea una nota dentro del standard zettelk """
        self._verify_unicity(name)
        self.generate_id(name)
        title_words = [word for word in name.split() if not word.startswith("-")]
        self.get_tags(name)
        title = '_'.join(map(str, title_words))
        target = self._notes_path+title+".md"
        self._prevent_duplicated_notes(target)
        print("target is :",target)
        self._repo.create_from_templ(self._notes_templ,target)
        if self._repo!= None:
            self._repo.save(Note("# "+" ".join(title_words)).set_tags(self._tags),target)
        if self.editor != None:
            self.open_editor(target)

    #TODO: Remove
    def _prevent_duplicated_notes(self,target:str):
        if os.path.isfile(target):
            raise DuplicatedNoteError()
        

    def print_title(self,name:str,target:str):
        name =[word for word in name.split() if not word.startswith("-")]
        title="# "+" ".join(name)+"\n"   
        new_lines = list()
        new_lines.append(title)
        with open(target,mode='r') as f:
            new_lines.extend(f.readlines())
        with open(target,mode='w') as f:
            f.writelines(new_lines)
        
    def print_id(self,target:str):
        new_lines = list()
        with open(target,mode='r') as f:
            existing = f.readlines()
        with open(target,mode='w') as f:
            existing.insert(0,"- ID: "+str(self._id)+"\n")
            f.writelines(existing)

    def get_tags(self,name:str):
        self._tags = [word.replace("-", "#") for word in name.split() if word.startswith("-")]

    def open_editor(self,target:str):
        self.editor.open(target)

    def generate_id(self,name:str):
        self._id = hash(name)

        #TODO: Mover esto a repo imp
#    def add_tags(self,target:str,tags:list):
#        if len(tags)>0:
#            tags_end_line = " ".join(map(str,[tag for tag in tags if not tag=="#noedit"]))
#            with open(target, "r") as file:
#                lines = file.readlines()
#            lines[len(lines)-1] = tags_end_line
 #           with open(target, "w") as file:
 #               file.writelines(lines)

    def add_meta(self,target:str):
       # new_first_line = "# "+" ".join(map(str,title_words))
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

class DuplicatedNoteError(BaseException):
    pass
