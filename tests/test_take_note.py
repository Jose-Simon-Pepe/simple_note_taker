import pytest
from simple_note_taker.src.infra.ports.repo_notes import RepoNotes
from simple_note_taker.src.domain.note import Note
from simple_note_taker.tests.helpers.spy_editor import Editor
from simple_note_taker.src.note_taker.create_note import NoteTaker, DuplicatedNoteError

# TODO: Implementar repository o capa de persistencia para create_note
# TODO: Si almaceno la nota en proceso como una lista de lineas entonces puedo testear mejor y modularizar mas el codigo
# TODO: deberia crear una factoria de take notes?
# TODO: Testear si toma la ruta de templates para crear la nota
# TODO: define NoteDTO for persistence and use it in service note taker
# TODO: desacouple note taker of note modification
# TODO: Reemplazar os lib por repository e implementar un adaptador de repo mediante os lib

notes_path = "tests/notes/"
notes_templ = "tests/template_demo.md"

@pytest.fixture
def nt():
    return NoteTaker(notes_path, notes_templ)


class InMemoRepo():

    def __init__(self):
        self._all = list()
        self.exists_ = False

    def save(self,note_dto,path:str):
        self._all.append(note_dto)

    def create_from_templ(self,template,target):
        pass

    def get_all(self):
        return self._all

    def exists(self,name:str,path:str) -> bool:
        return self.exists_

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

     

class TestNoteTaker:

    def test_note_taker_should_exist_by_the_note_folder_paths_and_a_template_path(self,nt):
        assert nt.notes_path() == notes_path
        assert nt.notes_templ() == notes_templ

    
    @pytest.mark.integration
    def test_note_taker_should_allow_set_tags_from_note_name_using_middle_dash(self,nt):
        note_name = "note with tags -this_is_a_tag"
        repo = InMemoRepo()
        nt.set_repo(repo)
        nt.create_note(note_name)
        assert repo.get_all()[0].tags()==["#this_is_a_tag"]
        
    @pytest.mark.integration
    def test_note_taker_should_open_editor_for_edit_note(self,nt):
        nt.set_repo(DommieRepo())
        editor = Editor()
        nt.set_editor(editor)
        nt.create_note("edited note with my editor -this_is_great")
        assert editor.was_called 

    def test_note_taker_should_generate_a_unique_id_for_note(self,nt):
        """Genera IDS basados en el contenido"""    
        nt.set_repo(DommieRepo())
        nt.create_note("note with id -i_have_id")
        id1= nt.id()
        nt.create_note("another note with different id -i_have_id")
        id2=nt.id()
        assert id1 != id2

    
    @pytest.mark.integration    
    def test_note_taker_should_print_note_name_as_a_header_in_first_line(self,nt):
        repo = InMemoRepo()
        nt.set_repo(repo)
        nt.create_note("note with title -i_have_title")
        assert repo.get_all()[0].ordered_lines()[0]=="# note with title"

       
    @pytest.mark.integration    
    def test_note_taker_should_print_note_id_as_second_line(self,nt):
        repo = InMemoRepo()
        nt.set_repo(repo)
        nt.create_note("note with id impressed -i_have_id")
        assert str(repo.get_all()[0].ordered_lines()[1]).startswith("- ID:")
    
    def test_note_should_never_be_repitted(self,nt):
        in_memo_repo = InMemoRepo()
        in_memo_repo.exists_ = True
        nt.set_repo(in_memo_repo)
        with pytest.raises(DuplicatedNoteError):
            nt.create_note("hola")
            nt.create_note("hola")
            assert len(in_memo_repo.get_all()) == 1
    
