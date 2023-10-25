class Note:
    def __init__(self,note:str,tags:list=["#Untagged"]):
        self._note = note
        self._ordered_lines:list = list()
        self._id = self.generate_id(note)
        #ordenar atributos
        self._ordered_lines.append(note)
        self._ordered_lines.append("- ID: "+str(self._id))
        self._ordered_lines.append(tags)

    def ordered_lines(self) -> list:
        return self._ordered_lines
    
    def set_title(self,title:str):
        self._title = title
        return self

    def set_tags(self,tags:list):
        self._tags= tags
        return self

    def note(self) -> str:
        return self._note

    def tags(self) -> list:
        return self._tags

    def id(self) -> int:
        return self._id

    @staticmethod
    def generate_id(note:str):
        return hash(note)

