from typing import Any

from rosys import persistence

from modules import (
    BumperV02,
    CanV03,
    CanV04,
    CanV06,
    IigiirV01,
    IigiirV02,
    OogiirV06,
    OogiirV07,
    OogoorV01,
    Rs485V03,
    Rs485V04,
    Rs485V05,
)

from .testbrain_hardware import TestBrain


class RobotBrains(persistence.PersistentModule):
    def __init__(self, robot_brain):
        print('Initializing RobotBrains')
        super().__init__()
        self.robot_brain = robot_brain
        self.current_brain_name = 'No brain selected'


        self.brain_configs = {
            'No brain selected': TestBrain(robot_brain, [], []),
            'rb12': TestBrain(robot_brain, ['nand'],[
                Rs485V03(robot_brain=robot_brain,socket=1,pin1=26,pin2=27,pin3=34,pin4=35),
                BumperV02(robot_brain=robot_brain,socket=2,pin1=5,pin2=36,pin3=13,pin4=4),
                CanV03(robot_brain=robot_brain,socket=3,pin1=32,pin2=33,pin3=14,pin3_on_exander=True,pin4=2,pin4_on_exander=True)
            ]),
            'rb13': TestBrain(robot_brain, [], []),
            'rb14': TestBrain(robot_brain, [], []),
            'rb19': TestBrain(robot_brain, ['nand'], [
                Rs485V05(robot_brain=robot_brain,socket=1,pin1=26,pin2=27,pin3=15,pin3_on_exander=True,pin4=13,pin4_on_exander=True),
                OogiirV07(robot_brain=robot_brain,socket=2,pin1=5,pin2=4,pin3=36,pin4=13),
                CanV06(robot_brain=robot_brain,socket=3,pin1=32,pin2=33,pin3=2,pin3_on_exander=True,pin4=14,pin4_on_exander=True),
                OogoorV01(robot_brain=robot_brain,socket=4,pin1=33,pin1_on_exander=True,pin2=4,pin2_on_exander=True,pin3=32,pin3_on_exander=True,pin4=5,pin4_on_exander=True),
                IigiirV02(robot_brain=robot_brain,socket=5,pin1=35,pin1_on_exander=True,pin2=18,pin2_on_exander=True,pin3=21,pin3_on_exander=True,pin4=19,pin4_on_exander=True),
                CanV04(robot_brain=robot_brain,socket=6,pin1=22,pin1_on_exander=True,pin2=23,pin2_on_exander=True,pin3=12,pin3_on_exander=True,pin4=25,pin4_on_exander=True)
            ]),
            'rb28': TestBrain(robot_brain, ['nand','orin','v05'], [
                Rs485V04(robot_brain=robot_brain,socket=1,pin1=26,pin2=27,pin3=15,pin3_on_exander=True,pin4=13,pin4_on_exander=True),
                OogiirV06(robot_brain=robot_brain,socket=2,pin1=5,pin2=4,pin3=36,pin4=13),
                CanV04(robot_brain=robot_brain,socket=3,pin1=32,pin2=33,pin3=2,pin3_on_exander=True,pin4=14,pin4_on_exander=True),
                IigiirV01(robot_brain=robot_brain,socket=4,pin1=33,pin1_on_exander=True,pin2=4,pin2_on_exander=True,pin3=32,pin3_on_exander=True,pin4=5,pin4_on_exander=True),
                IigiirV01(robot_brain=robot_brain,socket=5,pin1=35,pin1_on_exander=True,pin2=18,pin2_on_exander=True,pin3=21,pin3_on_exander=True,pin4=19,pin4_on_exander=True),
                BumperV02(robot_brain=robot_brain,socket=6,pin1=12,pin1_on_exander=True,pin2=25,pin2_on_exander=True,pin3=22,pin3_on_exander=True,pin4=23,pin4_on_exander=True)
            ]),
        }

        self.current_brain = self.brain_configs[self.current_brain_name]
        print(f'Initial brain set to: {self.current_brain_name}')

    def restore(self, data: dict[str, Any]) -> None:
        print(f'Restoring data: {data}')
        saved_brain = data.get('current_brain_name', 'placeholder')
        print(f'Found saved brain: {saved_brain}')
        if saved_brain in self.brain_configs:
            self.current_brain_name = saved_brain
            self.current_brain = self._switch_brain(self.current_brain_name)
            print(f'Restored brain to: {self.current_brain_name}')
        else:
            self.current_brain_name = 'placeholder'
            self.current_brain = self._switch_brain('placeholder')
            print('Fallback to placeholder')

    def backup(self) -> dict[str, Any]:
        print(f'Backing up brain: {self.current_brain_name}')
        return {
            'current_brain_name': self.current_brain_name
        }

    def _switch_brain(self, brain_name: str):
        self.current_brain.active = False
        brain = self.brain_configs[brain_name]
        brain.active = True
        brain.update_lizard()
        return brain

    def get_robot_brain_list(self):
        return list(self.brain_configs.keys())


    def get_robot_brain(self, robot_brain_name: str):
        self.current_brain_name = robot_brain_name
        self.current_brain = self._switch_brain(robot_brain_name)
        return self.current_brain
