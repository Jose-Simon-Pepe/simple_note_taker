from simple_note_taker.src.domain.note import Note
import os, shutil
"""
Repo adapter for CrUD notes repository
Entity: Note
Methods: 
    - get(id:int)-> A note  
    - get(name:str)-> A list of string pattern matching notes
    - save(note_dto)-> Boolean depending on op status
    - update(id:int)-> Boolean depending on op status
    - get_all()-> A list of all existing notes
"""

class RepoNotesOs:
    def get(id:int)-> Note:  
        pass

    def get(name:str)-> list:
        pass

    def get_all(self,location_path:str)-> list:
        notes_list = list()
        for filename in os.listdir(location_path):
            with open(os.path.join(location_path, filename), "r") as f:
                note_lines = f.readlines()
                note = note_lines[0].split("# ")[1].removesuffix("\n")
                id = int(note_lines[1].split("- ID: ")[1])
                tags = note_lines[2].removesuffix("\n").split(" ")[0:]
                obtained_note = Note(note,tags).set_id(id)
                print(obtained_note)
                notes_list.append(obtained_note)
        print(notes_list)
        return notes_list

    def create_from_templ(self,template:str,target:str):
        target = target.replace(" ", "_")   
        shutil.copyfile(template, target)

    def save(self,note_dto:Note,target:str)-> bool:
        lines = list()
        note_lines = note_dto.ordered_lines()
        lines.append(str(note_lines[0])+"\n")
        lines.append(str(note_lines[1])+"\n")
        tags = " ".join([tag for tag in note_lines[2]])
        lines.append(tags+"\n")
        with open(target,mode='w') as note:
            note.writelines(lines)

    def exists(self,name:str) -> bool:
        pass

    def update(id:int)-> bool:
        pass
