from hardware import TestBrain
from modules import *


class RobotBrains:
    def __init__(self, robot_brain):
        self.dict_robot_brains = {
            'placeholder': TestBrain(robot_brain, [], []),
            'rb12':TestBrain(robot_brain, [], 
                             [Rs485V03(robot_brain=robot_brain,socket=1,pin1=26,pin2=27,pin3=34,pin4=35),
                             BumperV02(robot_brain=robot_brain,socket=2,pin1=5,pin2=36,pin3=13,pin4=4),
                             CanV03(robot_brain=robot_brain,socket=3,pin1=32,pin2=33,pin3=14,pin3_on_exander=True,pin4=2,pin4_on_exander=True)]),
            'rb13': TestBrain(robot_brain, [], []),
            'rb14': TestBrain(robot_brain, [], []),
        }
    def get_robot_brain_list(self):
        return list(self.dict_robot_brains.keys())
    
    def get_robot_brain(self,robot_brain_name:str):
        return self.dict_robot_brains[robot_brain_name]
