import os 
import pytest
from simple_note_taker.src.infra.adapters.repo_notes_os import RepoNotesOs
from simple_note_taker.src.note_taker.create_note import NoteTaker

"""
This is testing both repo notes os adapter and create note service integration
"""

notes_path = os.getcwd()+"/tests/notes/"
notes_templ = os.getcwd()+"/tests/template_demo.md"

@pytest.fixture(autouse=True)
def remove_test_notes():
    if os.path.isdir(notes_path):
        os.system("rm -rf "+notes_path)
    os.mkdir(notes_path)
    yield
    os.system("rm -rf "+notes_path)

def test_create_note_should_persist_a_note_throught_repo_into_choosen_path():
    repo = RepoNotesOs()
    nt = NoteTaker(notes_path,notes_templ).set_repo(repo)
    nt.create_note("nueva nota")
    assert os.path.isfile(notes_path+"nueva_nota.md")

def test_repo_get_all_should_return_a_list_of_existing_notes():
    pass


@pytest.mark.integration
def test_note_taker_should_create_a_note_from_a_string_in_path_with_backslash():
    repo = RepoNotesOs()
    nt = NoteTaker(notes_path,notes_templ).set_repo(repo)
    note_name = "this is an empty test note"
    note_expected = notes_path+"this_is_an_empty_test_note.md"
    nt.create_note(note_name)
    assert os.path.isfile(note_expected)

#TODO: this
#def test_repo_should_return_if_a_note_already_exists_in_path():


