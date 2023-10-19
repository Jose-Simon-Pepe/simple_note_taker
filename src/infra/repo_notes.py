from simple_note_taker.src.domain.note import Note
"""
Repo interface for CrUD notes
Entity: Note
Methods: 
    - get(id:int)-> A note  
    - get(name:str)-> A list of string pattern matching notes
    - save(note_dto)-> Boolean depending on op status
    - update(id:int)-> Boolean depending on op status
    - get_all()-> A list of all existing notes
"""

class RepoNotes:
    def get(id:int)-> Note:  
        pass
    def get(name:str)-> list:
        pass
    def get_all()-> list:
        pass
    def save(note_dto)-> bool:
        pass
    def update(id:int)-> bool:
        pass
