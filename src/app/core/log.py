from byebyelogger import single_logger

from byebyelogger.style.format import SQUARE_BRACKETS
from byebyelogger.style.color import LIGHTCYAN_EX, LIGHTBLUE_EX, LIGHTRED_EX, LIGHTMAGENTA_EX


class LighRedLogger:
    
    def __init__(self, level:str):
        self.level = level
    
    def __call__(self, msg:str) :
        return single_logger(color=LIGHTRED_EX, level=self.level, format=SQUARE_BRACKETS).log(msg=msg)  
    

MessageOutput = LighRedLogger("INFO")

