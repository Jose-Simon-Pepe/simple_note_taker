import pytest
import os
from simple_note_taker.src.infra.editor_nvim import Nvim
from simple_note_taker.src.note_taker.create_note import NoteTaker

notes_path = "/home/peace/notes/"
notes_templ = os.getcwd()+"/tests/template_demo.md"

@pytest.mark.integration
def test_app_should_open_neovim():
    nt = NoteTaker(notes_path,notes_templ)
    nv = Nvim(False)
    nt.set_editor(nv)
    nt.create_note("nota prueba neovim")
    assert nv.env=="nvim "+notes_path+"nota_prueba_neovim.md"
    # How nasty this... isn't it?
    



