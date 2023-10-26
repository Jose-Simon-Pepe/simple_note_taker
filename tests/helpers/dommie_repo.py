from simple_note_taker.src.infra.ports.repo_notes import RepoNotes
from simple_note_taker.src.domain.note import Note

class DommieRepo(RepoNotes):

    def get(id:int)-> Note:  
        pass
    def get(name:str)-> list:
        pass
    def get_all()-> list:
        pass
    def save(self,note_dto,path:str)-> bool:
        pass
    def update(id:int)-> bool:
        pass
    def create_from_templ(self,templ,targ):
        pass
    def exists(self,name:str,path:str) -> bool:
        return False
