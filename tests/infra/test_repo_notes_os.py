import os 
import pytest
from simple_note_taker.src.infra.adapters.repo_notes_os import RepoNotesOs
from simple_note_taker.src.note_taker.create_note import NoteTaker

"""
This is testing both repo notes os adapter and create note service integration
"""

# TODO: Refactor repo notes os: create a "instantiate note" function which creates a note instance from a path

notes_path = os.getcwd()+"/tests/notes/"
notes_templ = os.getcwd()+"/tests/template_demo.md"

@pytest.fixture(autouse=True)
def remove_test_notes():
    if os.path.isdir(notes_path):
        os.system("rm -rf "+notes_path)
    os.mkdir(notes_path)
    yield
    os.system("rm -rf "+notes_path)

@pytest.mark.integration
def test_repo_should_create_a_note_from_template():
    repo = RepoNotesOs()
    nt = NoteTaker(notes_path,notes_templ).set_repo(repo)
    note_name = "this is an empty test note"
    nt.create_note(note_name)
    with open(notes_path+note_name.replace(" ", "_")+".md") as f:
        lines = f.readlines()
        assert lines[0] == "# "+note_name+"\n"
        assert lines[1].startswith("- ID:")
        assert lines[2] == "#Untagged\n"



#def test_repo_get_all_should_return_a_list_of_existing_notes():
#    repo = RepoNotesOs()
#    nt = NoteTaker(notes_path,notes_templ).set_repo(repo)
#    note_name = "this is an empty test note"
#    note_2_name = "this is an empty test note but 2"
#    nt.create_note(note_name)
#    nt.create_note(note_2_name)
#    assert repo.get_all(notes_path)[0].note()==note_name
#    assert repo.get_all(notes_path)[1].note()==note_2_name

              #
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

