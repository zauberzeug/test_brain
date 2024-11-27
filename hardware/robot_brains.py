from modules import *

from .testbrain_hardware import TestBrain


class RobotBrains:
    def __init__(self, robot_brain):
        self.robot_brain = robot_brain
        
        self.brain_configs = {
            'placeholder': TestBrain(robot_brain, [], []),
            'rb12': TestBrain(robot_brain, ['nand'],[
                Rs485V03(robot_brain=robot_brain,socket=1,pin1=26,pin2=27,pin3=34,pin4=35),
                BumperV02(robot_brain=robot_brain,socket=2,pin1=5,pin2=36,pin3=13,pin4=4),
                CanV03(robot_brain=robot_brain,socket=3,pin1=32,pin2=33,pin3=14,pin3_on_exander=True,pin4=2,pin4_on_exander=True)
            ]),
            'rb13': TestBrain(robot_brain, [], []),
            'rb14': TestBrain(robot_brain, [], []),
            'rb28': TestBrain(robot_brain, ['nand','orin','v05'], [
                Rs485V04(robot_brain=robot_brain,socket=1,pin1=26,pin2=27,pin3=15,pin3_on_exander=True,pin4=13,pin4_on_exander=True),
                OogiirV06(robot_brain=robot_brain,socket=2,pin1=5,pin2=4,pin3=36,pin4=13),
                CanV04(robot_brain=robot_brain,socket=3,pin1=32,pin2=33,pin3=2,pin3_on_exander=True,pin4=14,pin4_on_exander=True),
                IigiirV01(robot_brain=robot_brain,socket=4,pin1=33,pin1_on_exander=True,pin2=4,pin2_on_exander=True,pin3=32,pin3_on_exander=True,pin4=5,pin4_on_exander=True),
                IigiirV01(robot_brain=robot_brain,socket=5,pin1=35,pin1_on_exander=True,pin2=18,pin2_on_exander=True,pin3=21,pin3_on_exander=True,pin4=19,pin4_on_exander=True),
                BumperV02(robot_brain=robot_brain,socket=6,pin1=12,pin1_on_exander=True,pin2=25,pin2_on_exander=True,pin3=22,pin3_on_exander=True,pin4=23,pin4_on_exander=True)
            ]),
        }
        self.current_brain_name = 'placeholder'
        self.current_brain = self._switch_brain('placeholder')

    def _switch_brain(self, brain_name: str):
        brain = self.brain_configs[brain_name]
        print(f'brain: {brain}')
        print(f"Creating brain '{brain_name}' with {len(brain.modules)} modules")
        for module in brain.modules:
            print(f"  Module: {type(module).__name__}")
        brain.update_lizard()
        return brain

    def get_robot_brain_list(self):
        return list(self.brain_configs.keys())
    
    def get_robot_brain(self, robot_brain_name: str):

        self.current_brain = self._switch_brain(robot_brain_name)
        return self.current_brain
