import pytest
from simple_note_taker.src.domain.note import Note
from simple_note_taker.tests.helpers.spy_editor import Editor
import filecmp
import os
from simple_note_taker.src.note_taker.create_note import NoteTaker, DuplicatedNoteError

# TODO: Implementar repository o capa de persistencia para create_note
# TODO: Si almaceno la nota en proceso como una lista de lineas entonces puedo testear mejor y modularizar mas el codigo
# TODO: deberia crear una factoria de take notes?
# TODO: Testear si toma la ruta de templates para crear la nota
# TODO: define NoteDTO for persistence and use it in service note taker
# TODO: desacouple note taker of note modification

# TODO: Reemplazar os lib por repository e implementar un adaptador de repo mediante os lib


notes_path = os.getcwd()+"/tests/notes/"
notes_templ = os.getcwd()+"/tests/template_demo.md"
#eliminar duplicacion de fixture entre testeos
@pytest.fixture(autouse=True)
def remove_test_notes():
    if os.path.isdir(notes_path):
        os.system("rm -rf "+notes_path)
    os.mkdir(notes_path)
    yield
    os.system("rm -rf "+notes_path)

@pytest.fixture
def nt():
    return NoteTaker(notes_path, notes_templ)


class InMemoRepo():

    def __init__(self):
        self._all = list()

    def save(self,note_dto):
        self._all.append(note_dto)

    def get_all(self):
        return self._all

class TestNoteTaker:

    def test_note_taker_should_exist_by_the_note_folder_paths_and_a_template_path(self,nt):
        assert nt.notes_path() == notes_path
        assert nt.notes_templ() == notes_templ
    
    @pytest.mark.integration
    def test_note_taker_should_create_a_note_from_a_string_in_path_with_backslash(self,nt):
        note_name = "this is an empty test note"
        note_expected = notes_path+"this_is_an_empty_test_note.md"
        repo = InMemoRepo()
        nt.set_repo(repo)
        nt.create_note(note_name)
        assert repo.get_all()[0].note() == note_name
        assert os.path.isfile(note_expected)
    
    @pytest.mark.integration
    def test_note_taker_should_allow_set_tags_from_note_name_using_middle_dash(self,nt):
        note_name = "note with tags -this_is_a_tag"
        nt.create_note(note_name)
        with open(notes_path+"note_with_tags.md",mode='r') as f:
            last_line = f.readlines()[len(f.readlines())-1]
            assert last_line=="#this_is_a_tag"
        
    @pytest.mark.integration
    def test_note_taker_should_open_editor_for_edit_note(self,nt):
        editor = Editor()
        nt.set_editor(editor)
        nt.create_note("edited note with my editor -this_is_great")
        assert editor.was_called 
     
    def test_note_taker_should_generate_a_unique_id_for_note(self,nt):
        """Genera IDS basados en el contenido"""    
        nt.create_note("note with id -i_have_id")
        id1= nt.id()
        nt.create_note("another note with different id -i_have_id")
        id2=nt.id()
        assert id1 != id2
    
    @pytest.mark.integration    
    def test_note_taker_should_print_note_name_as_a_header_in_first_line____(self,nt):
        nt.create_note("note with title -i_have_title")
        with open(notes_path+"note_with_title.md") as f:
            assert f.readlines()[0] == "# note with title\n"

    @pytest.mark.integration    
    def test_note_taker_should_print_note_id_as_second_line(self,nt):
        nt.create_note("note with id impressed -i_have_id")
        with open(notes_path+"note_with_id_impressed.md") as f:
            assert f.readlines()[1].startswith("- ID:")
    
    def test_note_should_never_be_repitted(self,nt):
        in_memo_repo = InMemoRepo()
        nt.set_repo(in_memo_repo)
        with pytest.raises(DuplicatedNoteError):
            nt.create_note("")
            nt.create_note("")
            assert len(in_memo_repo.get_all()) == 1
    
