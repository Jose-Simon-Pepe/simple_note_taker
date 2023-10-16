import pytest
import os
from src.note_taker.create_note import NoteTaker


notes_path = "/home/peace/notes/"
notes_templ = "/home/peace/notes/template.md"

def test_note_taker_should_exist_by_the_note_folder_paths_and_a_template_path():
    nt = NoteTaker(notes_path, notes_templ)
    assert nt.notes_path() == notes_path
    assert nt.notes_templ() == notes_templ

@pytest.mark.integration
def test_note_taker_should_create_a_note_from_a_string_in_path_with_backslash():
    nt = NoteTaker(notes_path, notes_templ)
    note_name = "this is an empty test note"
    nt.create_note(note_name)
    note_name_parsed = note_name.replace(" ", "_")+".md"
    assert os.path.isfile(notes_path+note_name_parsed)
