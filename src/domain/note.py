class Note:
    def __init__(self,note:str):
        self._note = note
        self._id = self.generate_id(note)

    def note(self) -> str:
        return self._note

    def id(self) -> int:
        return self._id

    @staticmethod
    def generate_id(note:str):
        return hash(note)

