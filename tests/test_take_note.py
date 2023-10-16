import pytest
import os
from src.note_taker.create_note import NoteTaker

class FakeNoteTaker:
    def __init__(self,note_path:str,note_templ:str):
        self._notes_path = note_path
        self._notes_templ = note_templ

    def notes_path(self):
        return self._notes_path

    def notes_templ(self):
        return self._notes_templ

def test_note_taker_should_exist_by_the_note_folder_paths_and_a_template_path():
    notes_path = "/home/peace/notes/"
    notes_templ = "/home/peace/notes/template.md"
    nt = NoteTaker(notes_path, notes_templ)
    assert nt.notes_path() == notes_path
    assert nt.notes_templ() == notes_templ
