from simple_note_taker.src.domain.note import Note
import os, shutil
"""
Repo adapter for CrUD notes repository
Entity: Note
Methods: 
    - get(id:int)-> A note  
    - get(name:str)-> A list of string pattern matching notes
    - save(note_dto)-> Boolean depending on op status
    - update(id:int)-> Boolean depending on op status
    - get_all()-> A list of all existing notes
"""

class RepoNotesOs:
    def get(id:int)-> Note:  
        pass

    def get(name:str)-> list:
        pass

    def get_all(self)-> list:
        return [Note("this is an empty test note")]

    def create_from_templ(self,template:str,target:str):
        target = target.replace(" ", "_")
        shutil.copyfile(template, target)

    def save(self,note_dto:Note)-> bool:
        pass

    def exists(self,name:str) -> bool:
        pass

    def update(id:int)-> bool:
        pass
