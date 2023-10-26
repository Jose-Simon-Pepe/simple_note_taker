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
            raise DuplicatedNoteError()

    def create_note(self,name:str):
        """ Este script crea una nota dentro del standard zettelk """
        self._verify_unicity(name)
        self.generate_id(name)
        title_words = [word for word in name.split() if not word.startswith("-")]
        self.get_tags(name)
        title = '_'.join(map(str, title_words))
        target = self._notes_path+title+".md"
        print("target is :",target)
        self._repo.create_from_templ(self._notes_templ,target)
        self._repo.save(Note("# "+" ".join(title_words)).set_tags(self._tags),target)
        #TODO: Improve this shit
        if self.editor != None:
            self.open_editor(target)

 
    def get_tags(self,name:str):
        self._tags = [word.replace("-", "#") for word in name.split() if word.startswith("-")]

    def open_editor(self,target:str):
        self.editor.open(target)

    def generate_id(self,name:str):
        self._id = hash(name)

   
class DuplicatedNoteError(BaseException):
    pass
