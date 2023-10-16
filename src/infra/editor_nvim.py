from simple_note_taker.src.infra.editor import EDITOR
import os

class Nvim(EDITOR):

    def __init__(self,env:bool=True):
        self.env = env

    def open(self,target:str):
        """Opens choosen editor with target note"""
        command = "nvim "+target 
        if self.env:
            os.system(command)
        else:
            self.env=command


        
