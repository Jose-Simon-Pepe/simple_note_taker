import pytest
from simple_note_taker.src.infra.ports.repo_notes import RepoNotes
from simple_note_taker.src.domain.note import Note
from simple_note_taker.src.infra.ports.repo_notes import RepoNotes
import os
from simple_note_taker.src.infra.adapters.editor_nvim import Nvim
from simple_note_taker.src.note_taker.create_note import NoteTaker

# FIX: Possible evitable coupling, why is necesssary to import so many components here?

notes_path = os.getcwd()+"/tests/notes/"
notes_templ = os.getcwd()+"/tests/template_demo.md"

class DommieRepo(RepoNotes):
    def get(id:int)-> Note:  
        pass
    def get(name:str)-> list:
        pass
    def get_all()-> list:
        pass
    def save(self,note_dto,path)-> bool:
        pass
    def update(id:int)-> bool:
        pass
    def create_from_templ(self,templ,targ):
        pass 
    def exists(self,name:str,path:str) -> bool:
        return False

@pytest.fixture(autouse=True)
def remove_test_notes():
    if os.path.isdir(notes_path):
        os.system("rm -rf "+notes_path)
    os.mkdir(notes_path)
    yield
    os.system("rm -rf "+notes_path)

@pytest.mark.integration
def test_app_should_open_neovim():
    nt = NoteTaker(notes_path,notes_templ)
    nt.set_repo(DommieRepo())
    nv = Nvim(False)
    nt.set_editor(nv)
    nt.create_note("nota prueba neovim")
    assert nv.env=="nvim "+notes_path+"nota_prueba_neovim.md"
    # How nasty this... isn't it?
    



