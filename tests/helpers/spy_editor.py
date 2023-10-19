from simple_note_taker.src.infra.ports.editor import EDITOR
class Editor(EDITOR):

    was_called:bool = False
    
    def open(self,target:str):
        self.was_called = True
