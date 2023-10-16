class NoteTaker:
    def notes_path(self):
        return "/home/peace/notes/"

    def notes_templ(self):
        return "/home/peace/notes/template.md"

        return
def test_note_taker_should_exist_by_the_note_folder_paths_and_a_template_path():
    notes_path = "/home/peace/notes/"
    notes_templ = "/home/peace/notes/template.md"
    nt = NoteTaker()
    assert nt.notes_path() == notes_path
    assert nt.notes_templ() == notes_templ
