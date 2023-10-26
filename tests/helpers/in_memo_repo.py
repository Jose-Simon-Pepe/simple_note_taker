
class InMemoRepo():

    def __init__(self):
        self._all = list()
        self.exists_ = False

    def save(self,note_dto,path:str):
        self._all.append(note_dto)

    def create_from_templ(self,template,target):
        pass

    def get_all(self):
        return self._all

    def exists(self,name:str,path:str) -> bool:
        return self.exists_

