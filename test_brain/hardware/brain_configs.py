from dataclasses import dataclass

from .modules import (
    BumperV02,
    BumperV03,
    CanV03,
    CanV04,
    CanV05,
    CanV06,
    IigiirV01,
    IigiirV02,
    Oiio,
    OogiirV02mod,
    OogiirV05,
    OogiirV06,
    OogiirV07,
    OogoorV01,
    Rs485V03,
    Rs485V04,
    Rs485V05,
    Rs485V051,
)
from .test_brain import TestBrain


@dataclass
class ModuleConfig:
    module_type: str
    socket: int
    pin1: int
    pin2: int
    pin3: int
    pin4: int
    pin1_on_expander: bool = False
    pin2_on_expander: bool = False
    pin3_on_expander: bool = False
    pin4_on_expander: bool = False

@dataclass
class BrainConfig:
    flags: list[str]
    modules: list[ModuleConfig]


class BrainConfigs:
    def __init__(self, robot_brain):
        self._robot_brain = robot_brain
        self._brain_configs = {
            'rb11': BrainConfig(
                flags=[],
                modules=[
                    ModuleConfig('Rs485V03', socket=1, pin1=26, pin1_on_expander=False, pin2=27, pin2_on_expander=False, pin3=13, pin3_on_expander=True, pin4=15, pin4_on_expander=True),
                    ModuleConfig('OogiirV05', socket=2, pin1=4, pin1_on_expander=False, pin2=13, pin2_on_expander=False, pin3=36, pin3_on_expander=False, pin4=5, pin4_on_expander=False),
                    ModuleConfig('CanV03', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=14, pin3_on_expander=True, pin4=2, pin4_on_expander=True),
                    ModuleConfig('Oiio', socket=6, pin1=12, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=36, pin3_on_expander=True, pin4=39, pin4_on_expander=True),
                ]
            ),
            'rb19': BrainConfig(
                flags=['nand'],
                modules=[
                    ModuleConfig('Rs485V05', socket=1, pin1=26, pin1_on_expander=False, pin2=27, pin2_on_expander=False, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=2, pin1=5, pin1_on_expander=False, pin2=4, pin2_on_expander=False, pin3=36, pin3_on_expander=False, pin4=13, pin4_on_expander=False),
                    ModuleConfig('CanV06', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                    ModuleConfig('OogoorV01', socket=4, pin1=33, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=5, pin4_on_expander=True),
                    ModuleConfig('IigiirV02', socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True),
                    ModuleConfig('CanV04', socket=6, pin1=22, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=12, pin3_on_expander=True, pin4=25, pin4_on_expander=True)
                ]
            ),
        }
        self.old_brain_configs = {
            'rb11': TestBrain(robot_brain, [], [
                Rs485V03(robot_brain=robot_brain, socket=1, pin1=26, pin2=27, pin3=13, pin3_on_expander=True, pin4=15, pin4_on_expander=True),
                OogiirV05(robot_brain=robot_brain, socket=2, pin1=4, pin2=13, pin3=36, pin4=5),
                CanV03(robot_brain=robot_brain, socket=3, pin1=32, pin2=33, pin3=14, pin3_on_expander=True, pin4=2, pin4_on_expander=True),
                Oiio(robot_brain=robot_brain, socket=6, pin1=12, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=36, pin3_on_expander=True, pin4=39, pin4_on_expander=True)
            ]),
            'rb12': TestBrain(robot_brain, ['nand'],[
                Rs485V03(robot_brain=robot_brain, socket=1, pin1=26, pin2=27, pin3=34, pin4=35),
                BumperV02(robot_brain=robot_brain, socket=2, pin1=5, pin2=36, pin3=13, pin4=4),
                CanV03(robot_brain=robot_brain, socket=3, pin1=32, pin2=33, pin3=14, pin3_on_expander=True, pin4=2, pin4_on_expander=True)
            ]),
            'rb13': TestBrain(robot_brain, [], [
                Rs485V03(robot_brain=robot_brain, socket=1, pin1=26, pin2=27, pin3=13, pin3_on_expander=True, pin4=15, pin4_on_expander=True),
                CanV03(robot_brain=robot_brain, socket=3, pin1=32, pin2=33, pin3=14, pin3_on_expander=True, pin4=2, pin4_on_expander=True),
                Oiio(robot_brain=robot_brain, socket=4, pin1=5, pin1_on_expander=True, pin2=32, pin2_on_expander=True, pin3=33, pin3_on_expander=True, pin4=4, pin4_on_expander=True),
                Oiio(robot_brain=robot_brain, socket=5, pin1=19, pin1_on_expander=True, pin2=34, pin2_on_expander=True, pin3=35, pin3_on_expander=True, pin4=18, pin4_on_expander=True)
            ]),
            'rb14': TestBrain(robot_brain, [], [
                OogoorV01(robot_brain=robot_brain, socket=1, pin1=26, pin1_on_expander=True, pin2=27, pin2_on_expander=True, pin3=13, pin3_on_expander=True, pin4=15, pin4_on_expander=True),
                OogiirV05(robot_brain=robot_brain, socket=2, pin1=4, pin2=13, pin3=36, pin4=5),
                CanV03(robot_brain=robot_brain, socket=3, pin1=32, pin2=33, pin3=14, pin3_on_expander=True, pin4=2, pin4_on_expander=True),
                OogoorV01(robot_brain=robot_brain, socket=4, pin1=33, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=5, pin4_on_expander=True),
                OogiirV06(robot_brain=robot_brain, socket=5, pin1=19, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=34, pin3_on_expander=True, pin4=35, pin4_on_expander=True),
                CanV03(robot_brain=robot_brain, socket=6, pin1=39, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=36, pin3_on_expander=True, pin4=12, pin4_on_expander=True)
            ]),
            'rb17': TestBrain(robot_brain, [], [
                Rs485V05(robot_brain=robot_brain, socket=1, pin1=26, pin2=27, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                IigiirV02(robot_brain=robot_brain, socket=2, pin1=13, pin2=4, pin3=36, pin4=5),
                CanV04(robot_brain=robot_brain, socket=3, pin1=32, pin2=33, pin3=2, pin4=4),
                IigiirV02(robot_brain=robot_brain, socket=4, pin1=33, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=5, pin4_on_expander=True),
                OogiirV07(robot_brain=robot_brain, socket=5, pin1=19, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=35, pin4_on_expander=True),
                OogiirV07(robot_brain=robot_brain, socket=6, pin1=12, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=25, pin3_on_expander=True, pin4=22, pin4_on_expander=True)
            ]),
            'rb19': TestBrain(robot_brain, ['nand'], [
                Rs485V05(robot_brain=robot_brain, socket=1, pin1=26, pin2=27, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                OogiirV07(robot_brain=robot_brain, socket=2, pin1=5, pin2=4, pin3=36, pin4=13),
                CanV06(robot_brain=robot_brain, socket=3, pin1=32, pin2=33, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                OogoorV01(robot_brain=robot_brain, socket=4, pin1=33, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=5, pin4_on_expander=True),
                IigiirV02(robot_brain=robot_brain, socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True),
                CanV04(robot_brain=robot_brain, socket=6, pin1=22, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=12, pin3_on_expander=True, pin4=25, pin4_on_expander=True)
            ]),
            'rb20': TestBrain(robot_brain, [], [
                Rs485V03(robot_brain=robot_brain, socket=1, pin1=26, pin2=27, pin3=13, pin3_on_expander=True, pin4=15, pin4_on_expander=True),
                BumperV02(robot_brain=robot_brain, socket=2, pin1=5, pin2=36, pin3=13, pin4=4),
                CanV04(robot_brain=robot_brain, socket=3, pin1=32, pin2=33, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                OogiirV06(robot_brain=robot_brain, socket=4, pin1=5, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=33, pin4_on_expander=True),
                CanV03(robot_brain=robot_brain, socket=6, pin1=22, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=25, pin3_on_expander=True, pin4=12, pin4_on_expander=True)
            ]),
            'rb22': TestBrain(robot_brain, [], [
                Rs485V04(robot_brain=robot_brain, socket=1, pin1=26, pin2=27, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                BumperV02(robot_brain=robot_brain, socket=2, pin1=5, pin2=36, pin3=13, pin4=4),
                CanV04(robot_brain=robot_brain, socket=3, pin1=32, pin2=33, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                OogiirV06(robot_brain=robot_brain, socket=4, pin1=5, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=33, pin4_on_expander=True),
                CanV04(robot_brain=robot_brain, socket=6, pin1=22, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=12, pin3_on_expander=True, pin4=25, pin4_on_expander=True)
            ]),
            'rb26': TestBrain(robot_brain, [], [
                Rs485V04(robot_brain=robot_brain, socket=1, pin1=26, pin2=27, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                OogiirV06(robot_brain=robot_brain, socket=2, pin1=5, pin2=4, pin3=36, pin4=13),
                CanV05(robot_brain=robot_brain, socket=3, pin1=32, pin2=33, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                OogiirV06(robot_brain=robot_brain, socket=4, pin1=5, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=33, pin4_on_expander=True),
                OogiirV06(robot_brain=robot_brain, socket=5, pin1=19, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=35, pin4_on_expander=True),
                OogiirV06(robot_brain=robot_brain, socket=6, pin1=12, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=25, pin3_on_expander=True, pin4=22, pin4_on_expander=True)
            ]),
            'rb27': TestBrain(robot_brain, ['nand', 'orin', 'v05'], [
                Rs485V04(robot_brain=robot_brain, socket=1, pin1=26, pin2=27, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                OogiirV02mod(robot_brain=robot_brain, socket=2, pin1=13, pin2=4, pin3=5, pin4=36),
                CanV05(robot_brain=robot_brain, socket=3, pin1=32, pin2=33, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                OogiirV02mod(robot_brain=robot_brain, socket=4, pin1=33, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=5, pin3_on_expander=True, pin4=32, pin4_on_expander=True),
                OogiirV06(robot_brain=robot_brain, socket=5, pin1=19, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=35, pin4_on_expander=True),
                OogiirV05(robot_brain=robot_brain, socket=6, pin1=23, pin1_on_expander=True, pin2=22, pin2_on_expander=True, pin3=25, pin3_on_expander=True, pin4=12, pin4_on_expander=True)
            ]),
            'rb28': TestBrain(robot_brain, ['nand', 'orin', 'v05'], [
                Rs485V04(robot_brain=robot_brain, socket=1, pin1=26, pin2=27, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                OogiirV06(robot_brain=robot_brain, socket=2, pin1=5, pin2=4, pin3=36, pin4=13),
                CanV04(robot_brain=robot_brain, socket=3, pin1=32, pin2=33, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                IigiirV01(robot_brain=robot_brain, socket=4, pin1=33, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=5, pin4_on_expander=True),
                IigiirV01(robot_brain=robot_brain, socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True),
                BumperV02(robot_brain=robot_brain, socket=6, pin1=12, pin1_on_expander=True, pin2=25, pin2_on_expander=True, pin3=22, pin3_on_expander=True, pin4=23, pin4_on_expander=True)
            ]),
            'rb30': TestBrain(robot_brain, ['nand', 'orin', 'v05'], [
                Rs485V04(robot_brain=robot_brain, socket=1, pin1=26, pin2=27, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                OogiirV06(robot_brain=robot_brain, socket=2, pin1=5, pin2=4, pin3=36, pin4=13),
                CanV05(robot_brain=robot_brain, socket=3, pin1=32, pin2=33, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                IigiirV01(robot_brain=robot_brain, socket=4, pin1=33, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=5, pin4_on_expander=True),
                OogiirV06(robot_brain=robot_brain, socket=5, pin1=19, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=35, pin4_on_expander=True),
                OogiirV06(robot_brain=robot_brain, socket=6, pin1=12, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=25, pin3_on_expander=True, pin4=22, pin4_on_expander=True)
            ]),
            'rb31': TestBrain(robot_brain, ['nand', 'orin', 'v05'], [
                Rs485V04(robot_brain=robot_brain, socket=1, pin1=26, pin2=27, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                Rs485V051(robot_brain=robot_brain, socket=2, pin1=13, pin2=4, pin3=5, pin4=15),
                CanV05(robot_brain=robot_brain, socket=3, pin1=32, pin2=33, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                OogiirV06(robot_brain=robot_brain, socket=4, pin1=5, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=33, pin4_on_expander=True),
                BumperV02(robot_brain=robot_brain, socket=5, pin1=19, pin1_on_expander=True, pin2=21, pin2_on_expander=True, pin3=35, pin3_on_expander=True, pin4=18, pin4_on_expander=True),
                OogiirV07(robot_brain=robot_brain, socket=6, pin1=12, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=25, pin3_on_expander=True, pin4=22, pin4_on_expander=True)
            ]),
            'rb32': TestBrain(robot_brain, ['nand', 'orin', 'v05'], [
                Rs485V04(robot_brain=robot_brain, socket=1, pin1=26, pin2=27, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                OogiirV06(robot_brain=robot_brain, socket=2, pin1=5, pin2=4, pin3=36, pin4=13),
                CanV05(robot_brain=robot_brain, socket=3, pin1=32, pin2=33, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                IigiirV01(robot_brain=robot_brain, socket=4, pin1=33, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=5, pin4_on_expander=True),
                IigiirV01(robot_brain=robot_brain, socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True),
                BumperV02(robot_brain=robot_brain, socket=6, pin1=12, pin1_on_expander=True, pin2=25, pin2_on_expander=True, pin3=22, pin3_on_expander=True, pin4=23, pin4_on_expander=True)
            ]),
            'rb33': TestBrain(robot_brain, ['nand', 'orin', 'v05'], [
                Rs485V05(robot_brain=robot_brain, socket=1, pin1=26, pin2=27, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                OogiirV06(robot_brain=robot_brain, socket=2, pin1=5, pin2=4, pin3=36, pin4=13),
                CanV05(robot_brain=robot_brain, socket=3, pin1=32, pin2=33, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                OogiirV06(robot_brain=robot_brain, socket=4, pin1=5, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=33, pin4_on_expander=True),
                BumperV02(robot_brain=robot_brain, socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True),
                IigiirV01(robot_brain=robot_brain, socket=6, pin1=22, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=25, pin3_on_expander=True, pin4=12, pin4_on_expander=True)
            ]),
            'rb35': TestBrain(robot_brain, ['nand', 'orin', 'v05'], [
                CanV05(robot_brain=robot_brain, socket=1, pin1=26, pin1_on_expander=True, pin2=27, pin2_on_expander=True, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                OogiirV07(robot_brain=robot_brain, socket=2, pin1=5, pin2=4, pin3=36, pin4=13),
                CanV05(robot_brain=robot_brain, socket=3, pin1=32, pin2=33, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
            ]),
            'rb36': TestBrain(robot_brain, ['nand', 'orin', 'v05'], [
                Rs485V05(robot_brain=robot_brain, socket=1, pin1=26, pin2=27, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                IigiirV02(robot_brain=robot_brain, socket=2, pin1=13, pin2=4, pin3=36, pin4=5),
                CanV06(robot_brain=robot_brain, socket=3, pin1=32, pin2=33, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                IigiirV02(robot_brain=robot_brain, socket=4, pin1=33, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=5, pin4_on_expander=True),
                BumperV03(robot_brain=robot_brain, socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True),
                OogoorV01(robot_brain=robot_brain, socket=6, pin1=22, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=25, pin3_on_expander=True, pin4=12, pin4_on_expander=True)
            ]),
            'rb37': TestBrain(robot_brain, ['nand', 'orin', 'v05'], [
                Rs485V05(robot_brain=robot_brain, socket=1, pin1=26, pin2=27, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                OogiirV07(robot_brain=robot_brain, socket=2, pin1=5, pin2=4, pin3=36, pin4=13),
                CanV06(robot_brain=robot_brain, socket=3, pin1=32, pin2=33, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                OogiirV07(robot_brain=robot_brain, socket=4, pin1=5, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=33, pin4_on_expander=True),
                BumperV03(robot_brain=robot_brain, socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True),
                OogiirV07(robot_brain=robot_brain, socket=6, pin1=12, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=25, pin3_on_expander=True, pin4=22, pin4_on_expander=True)
            ]),
            'rb38': TestBrain(robot_brain, ['nand', 'orin', 'v05'], [
                Rs485V05(robot_brain=robot_brain, socket=1, pin1=26, pin2=27, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                BumperV03(robot_brain=robot_brain, socket=2, pin1=13, pin2=4, pin3=36, pin4=5),
                CanV03(robot_brain=robot_brain, socket=3, pin1=32, pin2=33, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                OogiirV07(robot_brain=robot_brain, socket=4, pin1=5, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=33, pin4_on_expander=True),
                IigiirV02(robot_brain=robot_brain, socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True),
                CanV06(robot_brain=robot_brain, socket=6, pin1=22, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=12, pin3_on_expander=True, pin4=25, pin4_on_expander=True)
            ]),
            'rb39': TestBrain(robot_brain, ['nand', 'orin', 'v05'], [
                Rs485V05(robot_brain=robot_brain, socket=1, pin1=26, pin2=27, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                OogiirV07(robot_brain=robot_brain, socket=2, pin1=5, pin2=4, pin3=36, pin4=13),
                CanV06(robot_brain=robot_brain, socket=3, pin1=32, pin2=33, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                OogiirV07(robot_brain=robot_brain, socket=4, pin1=5, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=33, pin4_on_expander=True),
                BumperV03(robot_brain=robot_brain, socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True),
                OogiirV07(robot_brain=robot_brain, socket=6, pin1=12, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=25, pin3_on_expander=True, pin4=22, pin4_on_expander=True)
            ]),
            'rb40': TestBrain(robot_brain, ['nand', 'orin', 'v05'], [
                Rs485V05(robot_brain=robot_brain, socket=1, pin1=26, pin2=27, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                OogiirV07(robot_brain=robot_brain, socket=2, pin1=5, pin2=4, pin3=36, pin4=13),
                CanV06(robot_brain=robot_brain, socket=3, pin1=32, pin2=33, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                OogiirV07(robot_brain=robot_brain, socket=4, pin1=5, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=33, pin4_on_expander=True),
                BumperV03(robot_brain=robot_brain, socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True),
                CanV06(robot_brain=robot_brain, socket=6, pin1=22, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=12, pin3_on_expander=True, pin4=25, pin4_on_expander=True)
            ]),
            'rb41': TestBrain(robot_brain, ['nand', 'orin', 'v05'], [
               Rs485V05(robot_brain=robot_brain, socket=1, pin1=26, pin2=27, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                OogiirV07(robot_brain=robot_brain, socket=2, pin1=5, pin2=4, pin3=36, pin4=13),
                CanV06(robot_brain=robot_brain, socket=3, pin1=32, pin2=33, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                OogiirV07(robot_brain=robot_brain, socket=4, pin1=5, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=33, pin4_on_expander=True),
                BumperV03(robot_brain=robot_brain, socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True),
                CanV06(robot_brain=robot_brain, socket=6, pin1=22, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=12, pin3_on_expander=True, pin4=25, pin4_on_expander=True)
            ]),
            'rb42': TestBrain(robot_brain, ['nand', 'orin', 'v05'], [
                Rs485V05(robot_brain=robot_brain, socket=1, pin1=26, pin2=27, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                OogiirV07(robot_brain=robot_brain, socket=2, pin1=5, pin2=4, pin3=36, pin4=13),
                CanV06(robot_brain=robot_brain, socket=3, pin1=32, pin2=33, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                OogiirV07(robot_brain=robot_brain, socket=4, pin1=5, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=33, pin4_on_expander=True),
                BumperV03(robot_brain=robot_brain, socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True),
                CanV06(robot_brain=robot_brain, socket=6, pin1=22, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=12, pin3_on_expander=True, pin4=25, pin4_on_expander=True)
            ]),
            'rb43': TestBrain(robot_brain, ['nand', 'orin', 'v05'], [
                Rs485V05(robot_brain=robot_brain, socket=1, pin1=26, pin2=27, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                OogiirV07(robot_brain=robot_brain, socket=2, pin1=5, pin2=4, pin3=36, pin4=13),
                CanV06(robot_brain=robot_brain, socket=3, pin1=32, pin2=33, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                IigiirV02(robot_brain=robot_brain, socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True)
            ]),
            'rb44': TestBrain(robot_brain, ['nand', 'orin', 'v05'], [
                Rs485V05(robot_brain=robot_brain, socket=1, pin1=26, pin2=27, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                OogiirV07(robot_brain=robot_brain, socket=2, pin1=5, pin2=4, pin3=36, pin4=13),
                CanV06(robot_brain=robot_brain, socket=3, pin1=32, pin2=33, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                IigiirV02(robot_brain=robot_brain, socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True)
            ]),
            'rb45': TestBrain(robot_brain, ['nand', 'orin', 'v05'], [
                Rs485V05(robot_brain=robot_brain, socket=1, pin1=26, pin2=27, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                OogiirV07(robot_brain=robot_brain, socket=2, pin1=5, pin2=4, pin3=36, pin4=13),
                CanV06(robot_brain=robot_brain, socket=3, pin1=32, pin2=33, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                IigiirV02(robot_brain=robot_brain, socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True)
            ]),
        }

    @property
    def brain_names(self):
        return list(self._brain_configs.keys())

    def get_brain(self, robot_brain_name: str) -> TestBrain:
        assert robot_brain_name in self._brain_configs
        config = self._brain_configs[robot_brain_name]
        brain_modules = []
        for module_config in config.modules:
            ModuleClass = globals()[module_config.module_type]
            module = ModuleClass(
                robot_brain=self._robot_brain,
                socket=module_config.socket,
                pin1=module_config.pin1,
                pin2=module_config.pin2,
                pin3=module_config.pin3,
                pin4=module_config.pin4,
                pin1_on_expander=module_config.pin1_on_expander,
                pin2_on_expander=module_config.pin2_on_expander,
                pin3_on_expander=module_config.pin3_on_expander,
                pin4_on_expander=module_config.pin4_on_expander,
            )
            brain_modules.append(module)
        brain = TestBrain(self._robot_brain, config.flags, brain_modules)
        return brain
