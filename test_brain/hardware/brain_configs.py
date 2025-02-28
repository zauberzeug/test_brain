# pylint: disable=W0611
from dataclasses import dataclass

from .modules import (  # noqa: F401  needs to be imported for get_brains to work
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
            'rb12': BrainConfig(
                flags=['nand'],
                modules=[
                    ModuleConfig('Rs485V03', socket=1, pin1=26, pin1_on_expander=False, pin2=27, pin2_on_expander=False, pin3=34, pin3_on_expander=False, pin4=35, pin4_on_expander=False),
                    ModuleConfig('BumperV02', socket=2, pin1=5, pin1_on_expander=False, pin2=36, pin2_on_expander=False, pin3=13, pin3_on_expander=False, pin4=4, pin4_on_expander=False),
                    ModuleConfig('CanV03', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=14, pin3_on_expander=True, pin4=2, pin4_on_expander=True),
                ]
            ),
            'rb13': BrainConfig(
                flags=[],
                modules=[
                    ModuleConfig('Rs485V03', socket=1, pin1=26, pin1_on_expander=False, pin2=27, pin2_on_expander=False, pin3=13, pin3_on_expander=True, pin4=15, pin4_on_expander=True),
                    ModuleConfig('CanV03', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=14, pin3_on_expander=True, pin4=2, pin4_on_expander=True),
                    ModuleConfig('Oiio', socket=4, pin1=5, pin1_on_expander=True, pin2=32, pin2_on_expander=True, pin3=33, pin3_on_expander=True, pin4=4, pin4_on_expander=True),
                    ModuleConfig('Oiio', socket=5, pin1=19, pin1_on_expander=True, pin2=34, pin2_on_expander=True, pin3=35, pin3_on_expander=True, pin4=18, pin4_on_expander=True),
                ]
            ),
            'rb14': BrainConfig(
                flags=[],
                modules=[
                    ModuleConfig('OogoorV01', socket=1, pin1=26, pin1_on_expander=True, pin2=27, pin2_on_expander=True, pin3=13, pin3_on_expander=True, pin4=15, pin4_on_expander=True),
                    ModuleConfig('OogiirV05', socket=2, pin1=4, pin1_on_expander=False, pin2=13, pin2_on_expander=False, pin3=36, pin3_on_expander=False, pin4=5, pin4_on_expander=False),
                    ModuleConfig('CanV03', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=14, pin3_on_expander=True, pin4=2, pin4_on_expander=True),
                    ModuleConfig('OogoorV01', socket=4, pin1=33, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=5, pin4_on_expander=True),
                    ModuleConfig('OogiirV06', socket=5, pin1=19, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=34, pin3_on_expander=True, pin4=35, pin4_on_expander=True),
                    ModuleConfig('CanV03', socket=6, pin1=39, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=36, pin3_on_expander=True, pin4=12, pin4_on_expander=True),
                ]
            ),
            'rb17': BrainConfig(
                flags=[],
                modules=[
                    ModuleConfig('Rs485V05', socket=1, pin1=26, pin1_on_expander=False, pin2=27, pin2_on_expander=False, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                    ModuleConfig('IigiirV02', socket=2, pin1=13, pin1_on_expander=False, pin2=4, pin2_on_expander=False, pin3=36, pin3_on_expander=False, pin4=5, pin4_on_expander=False),
                    ModuleConfig('CanV04', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=2, pin3_on_expander=False, pin4=4, pin4_on_expander=False),
                    ModuleConfig('IigiirV02', socket=4, pin1=33, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=5, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=5, pin1=19, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=35, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=6, pin1=12, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=25, pin3_on_expander=True, pin4=22, pin4_on_expander=True)
                ]
            ),
            'rb19': BrainConfig(
                flags=['nand'],
                modules=[
                    # ModuleConfig('Rs485V05', socket=1, pin1=26, pin1_on_expander=False, pin2=27, pin2_on_expander=False, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=2, pin1=5, pin1_on_expander=False, pin2=4, pin2_on_expander=False, pin3=36, pin3_on_expander=False, pin4=13, pin4_on_expander=False),
                    ModuleConfig('CanV06', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                    ModuleConfig('OogoorV01', socket=4, pin1=33, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=5, pin4_on_expander=True),
                    ModuleConfig('IigiirV02', socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True),
                    ModuleConfig('Rs485V05', socket=6, pin1=22, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=12, pin3_on_expander=True, pin4=25, pin4_on_expander=True)
                ]
            ),
            'rb20': BrainConfig(
                flags=[],
                modules=[
                    ModuleConfig('Rs485V03', socket=1, pin1=26, pin1_on_expander=False, pin2=27, pin2_on_expander=False, pin3=13, pin3_on_expander=True, pin4=15, pin4_on_expander=True),
                    ModuleConfig('BumperV02', socket=2, pin1=5, pin1_on_expander=False, pin2=36, pin2_on_expander=False, pin3=13, pin3_on_expander=False, pin4=4, pin4_on_expander=False),
                    ModuleConfig('CanV04', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                    ModuleConfig('OogiirV06', socket=4, pin1=5, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=33, pin4_on_expander=True),
                    ModuleConfig('CanV03', socket=6, pin1=22, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=25, pin3_on_expander=True, pin4=12, pin4_on_expander=True)
                ]
            ),
            'rb22': BrainConfig(
                flags=[],
                modules=[
                    ModuleConfig('Rs485V04', socket=1, pin1=26, pin1_on_expander=False, pin2=27, pin2_on_expander=False, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                    ModuleConfig('BumperV02', socket=2, pin1=5, pin1_on_expander=False, pin2=36, pin2_on_expander=False, pin3=13, pin3_on_expander=False, pin4=4, pin4_on_expander=False),
                    ModuleConfig('CanV04', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                    ModuleConfig('OogiirV06', socket=4, pin1=5, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=33, pin4_on_expander=True),
                    ModuleConfig('CanV04', socket=6, pin1=22, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=12, pin3_on_expander=True, pin4=25, pin4_on_expander=True)
                ]
            ),
            'rb26': BrainConfig(
                flags=[],
                modules=[
                    ModuleConfig('Rs485V04', socket=1, pin1=26, pin1_on_expander=False, pin2=27, pin2_on_expander=False, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                    ModuleConfig('OogiirV06', socket=2, pin1=5, pin1_on_expander=False, pin2=4, pin2_on_expander=False, pin3=36, pin3_on_expander=False, pin4=13, pin4_on_expander=False),
                    ModuleConfig('CanV05', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                    ModuleConfig('OogiirV06', socket=4, pin1=5, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=33, pin4_on_expander=True),
                    ModuleConfig('OogiirV06', socket=5, pin1=19, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=35, pin4_on_expander=True),
                    ModuleConfig('OogiirV06', socket=6, pin1=12, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=25, pin3_on_expander=True, pin4=22, pin4_on_expander=True)
                ]
            ),
            'rb27': BrainConfig(
                flags=['nand', 'orin', 'v05'],
                modules=[
                    ModuleConfig('Rs485V04', socket=1, pin1=26, pin1_on_expander=False, pin2=27, pin2_on_expander=False, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                    ModuleConfig('OogiirV02mod', socket=2, pin1=13, pin1_on_expander=False, pin2=4, pin2_on_expander=False, pin3=5, pin3_on_expander=False, pin4=36, pin4_on_expander=False),
                    ModuleConfig('CanV05', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                    ModuleConfig('OogiirV02mod', socket=4, pin1=33, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=5, pin3_on_expander=True, pin4=32, pin4_on_expander=True),
                    ModuleConfig('OogiirV06', socket=5, pin1=19, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=35, pin4_on_expander=True),
                    ModuleConfig('OogiirV05', socket=6, pin1=23, pin1_on_expander=True, pin2=22, pin2_on_expander=True, pin3=25, pin3_on_expander=True, pin4=12, pin4_on_expander=True)
                ]
            ),
            'rb28': BrainConfig(
                flags=['nand', 'orin', 'v05'],
                modules=[
                    ModuleConfig('Rs485V04', socket=1, pin1=26, pin1_on_expander=False, pin2=27, pin2_on_expander=False, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                    ModuleConfig('OogiirV06', socket=2, pin1=5, pin1_on_expander=False, pin2=4, pin2_on_expander=False, pin3=36, pin3_on_expander=False, pin4=13, pin4_on_expander=False),
                    ModuleConfig('CanV04', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                    ModuleConfig('IigiirV01', socket=4, pin1=33, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=5, pin4_on_expander=True),
                    ModuleConfig('IigiirV01', socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True),
                    ModuleConfig('BumperV02', socket=6, pin1=12, pin1_on_expander=True, pin2=25, pin2_on_expander=True, pin3=22, pin3_on_expander=True, pin4=23, pin4_on_expander=True)
                ]
            ),
            'rb30': BrainConfig(
                flags=['nand', 'orin', 'v05'],
                modules=[
                    ModuleConfig('Rs485V04', socket=1, pin1=26, pin1_on_expander=False, pin2=27, pin2_on_expander=False, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                    ModuleConfig('OogiirV06', socket=2, pin1=5, pin1_on_expander=False, pin2=4, pin2_on_expander=False, pin3=36, pin3_on_expander=False, pin4=13, pin4_on_expander=False),
                    ModuleConfig('CanV05', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                    ModuleConfig('IigiirV01', socket=4, pin1=33, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=5, pin4_on_expander=True),
                    ModuleConfig('OogiirV06', socket=5, pin1=19, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=35, pin4_on_expander=True),
                    ModuleConfig('OogiirV06', socket=6, pin1=12, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=25, pin3_on_expander=True, pin4=22, pin4_on_expander=True)
                ]
            ),
            'rb31': BrainConfig(
                flags=['nand', 'orin', 'v05'],
                modules=[
                    ModuleConfig('Rs485V04', socket=1, pin1=26, pin1_on_expander=False, pin2=27, pin2_on_expander=False, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                    ModuleConfig('Rs485V051', socket=2, pin1=13, pin1_on_expander=False, pin2=4, pin2_on_expander=False, pin3=5, pin3_on_expander=False, pin4=15, pin4_on_expander=False),
                    ModuleConfig('CanV05', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                    ModuleConfig('OogiirV06', socket=4, pin1=5, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=33, pin4_on_expander=True),
                    ModuleConfig('BumperV02', socket=5, pin1=19, pin1_on_expander=True, pin2=21, pin2_on_expander=True, pin3=35, pin3_on_expander=True, pin4=18, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=6, pin1=12, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=25, pin3_on_expander=True, pin4=22, pin4_on_expander=True)
                ]
            ),
            'rb32': BrainConfig(
                flags=['nand', 'orin', 'v05'],
                modules=[
                    ModuleConfig('Rs485V04', socket=1, pin1=26, pin1_on_expander=False, pin2=27, pin2_on_expander=False, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                    ModuleConfig('OogiirV06', socket=2, pin1=5, pin1_on_expander=False, pin2=4, pin2_on_expander=False, pin3=36, pin3_on_expander=False, pin4=13, pin4_on_expander=False),
                    ModuleConfig('CanV05', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                    ModuleConfig('IigiirV01', socket=4, pin1=33, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=5, pin4_on_expander=True),
                    ModuleConfig('IigiirV01', socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True),
                    ModuleConfig('BumperV02', socket=6, pin1=12, pin1_on_expander=True, pin2=25, pin2_on_expander=True, pin3=22, pin3_on_expander=True, pin4=23, pin4_on_expander=True)
                ]
            ),
            'rb33': BrainConfig(
                flags=['nand', 'orin', 'v05'],
                modules=[
                    ModuleConfig('Rs485V05', socket=1, pin1=26, pin1_on_expander=False, pin2=27, pin2_on_expander=False, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                    ModuleConfig('OogiirV06', socket=2, pin1=5, pin1_on_expander=False, pin2=4, pin2_on_expander=False, pin3=36, pin3_on_expander=False, pin4=13, pin4_on_expander=False),
                    ModuleConfig('CanV05', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                    ModuleConfig('OogiirV06', socket=4, pin1=5, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=33, pin4_on_expander=True),
                    ModuleConfig('BumperV02', socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True),
                    ModuleConfig('IigiirV01', socket=6, pin1=22, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=25, pin3_on_expander=True, pin4=12, pin4_on_expander=True)
                ]
            ),
            'rb35': BrainConfig(
                flags=['nand', 'orin', 'v05'],
                modules=[
                    ModuleConfig('CanV05', socket=1, pin1=26, pin1_on_expander=True, pin2=27, pin2_on_expander=True, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=2, pin1=5, pin1_on_expander=False, pin2=4, pin2_on_expander=False, pin3=36, pin3_on_expander=False, pin4=13, pin4_on_expander=False),
                    ModuleConfig('CanV05', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                ]
            ),
            'rb36': BrainConfig(
                flags=['nand', 'orin', 'v05'],
                modules=[
                    ModuleConfig('Rs485V05', socket=1, pin1=26, pin1_on_expander=False, pin2=27, pin2_on_expander=False, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                    ModuleConfig('IigiirV02', socket=2, pin1=13, pin1_on_expander=False, pin2=4, pin2_on_expander=False, pin3=36, pin3_on_expander=False, pin4=5, pin4_on_expander=False),
                    ModuleConfig('CanV06', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                    ModuleConfig('IigiirV02', socket=4, pin1=33, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=5, pin4_on_expander=True),
                    ModuleConfig('BumperV03', socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True),
                    ModuleConfig('OogoorV01', socket=6, pin1=22, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=25, pin3_on_expander=True, pin4=12, pin4_on_expander=True)
                ]
            ),
            'rb37': BrainConfig(
                flags=['nand', 'orin', 'v05'],
                modules=[
                    ModuleConfig('Rs485V05', socket=1, pin1=26, pin1_on_expander=False, pin2=27, pin2_on_expander=False, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=2, pin1=5, pin1_on_expander=False, pin2=4, pin2_on_expander=False, pin3=36, pin3_on_expander=False, pin4=13, pin4_on_expander=False),
                    ModuleConfig('CanV06', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=4, pin1=5, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=33, pin4_on_expander=True),
                    ModuleConfig('BumperV03', socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=6, pin1=12, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=25, pin3_on_expander=True, pin4=22, pin4_on_expander=True)
                ]
            ),
            'rb38': BrainConfig(
                flags=['nand', 'orin', 'v05'],
                modules=[
                    ModuleConfig('Rs485V05', socket=1, pin1=26, pin1_on_expander=False, pin2=27, pin2_on_expander=False, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                    ModuleConfig('BumperV03', socket=2, pin1=13, pin1_on_expander=False, pin2=4, pin2_on_expander=False, pin3=36, pin3_on_expander=False, pin4=5, pin4_on_expander=False),
                    ModuleConfig('CanV03', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=4, pin1=5, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=33, pin4_on_expander=True),
                    ModuleConfig('IigiirV02', socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True),
                    ModuleConfig('CanV06', socket=6, pin1=22, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=12, pin3_on_expander=True, pin4=25, pin4_on_expander=True)
                ]
            ),
            'rb39': BrainConfig(
                flags=['nand', 'orin', 'v05'],
                modules=[
                    ModuleConfig('Rs485V05', socket=1, pin1=26, pin1_on_expander=False, pin2=27, pin2_on_expander=False, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=2, pin1=5, pin1_on_expander=False, pin2=4, pin2_on_expander=False, pin3=36, pin3_on_expander=False, pin4=13, pin4_on_expander=False),
                    ModuleConfig('CanV06', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=4, pin1=5, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=33, pin4_on_expander=True),
                    ModuleConfig('BumperV03', socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=6, pin1=12, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=25, pin3_on_expander=True, pin4=22, pin4_on_expander=True)
                ]
            ),
            'rb40': BrainConfig(
                flags=['nand', 'orin', 'v05'],
                modules=[
                    ModuleConfig('Rs485V05', socket=1, pin1=26, pin1_on_expander=False, pin2=27, pin2_on_expander=False, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=2, pin1=5, pin1_on_expander=False, pin2=4, pin2_on_expander=False, pin3=36, pin3_on_expander=False, pin4=13, pin4_on_expander=False),
                    ModuleConfig('CanV06', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=4, pin1=5, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=33, pin4_on_expander=True),
                    ModuleConfig('BumperV03', socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True),
                    ModuleConfig('CanV06', socket=6, pin1=22, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=12, pin3_on_expander=True, pin4=25, pin4_on_expander=True)
                ]
            ),
            'rb41': BrainConfig(
                flags=['nand', 'orin', 'v05'],
                modules=[
                    ModuleConfig('Rs485V05', socket=1, pin1=26, pin1_on_expander=False, pin2=27, pin2_on_expander=False, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=2, pin1=5, pin1_on_expander=False, pin2=4, pin2_on_expander=False, pin3=36, pin3_on_expander=False, pin4=13, pin4_on_expander=False),
                    ModuleConfig('CanV06', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=4, pin1=5, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=33, pin4_on_expander=True),
                    ModuleConfig('BumperV03', socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True),
                    ModuleConfig('CanV06', socket=6, pin1=22, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=12, pin3_on_expander=True, pin4=25, pin4_on_expander=True)
                ]
            ),
            'rb42': BrainConfig(
                flags=['nand', 'orin', 'v05'],
                modules=[
                    ModuleConfig('Rs485V05', socket=1, pin1=26, pin1_on_expander=False, pin2=27, pin2_on_expander=False, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=2, pin1=5, pin1_on_expander=False, pin2=4, pin2_on_expander=False, pin3=36, pin3_on_expander=False, pin4=13, pin4_on_expander=False),
                    ModuleConfig('CanV06', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=4, pin1=5, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=33, pin4_on_expander=True),
                    ModuleConfig('BumperV03', socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True),
                    ModuleConfig('CanV06', socket=6, pin1=22, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=12, pin3_on_expander=True, pin4=25, pin4_on_expander=True)
                ]
            ),
            'rb43': BrainConfig(
                flags=['nand', 'orin', 'v05'],
                modules=[
                    ModuleConfig('Rs485V05', socket=1, pin1=26, pin1_on_expander=False, pin2=27, pin2_on_expander=False, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=2, pin1=5, pin1_on_expander=False, pin2=4, pin2_on_expander=False, pin3=36, pin3_on_expander=False, pin4=13, pin4_on_expander=False),
                    ModuleConfig('CanV06', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                    ModuleConfig('IigiirV02', socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True)
                ]
            ),
            'rb44': BrainConfig(
                flags=['nand', 'orin', 'v05'],
                modules=[
                    ModuleConfig('Rs485V05', socket=1, pin1=26, pin1_on_expander=False, pin2=27, pin2_on_expander=False, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=2, pin1=5, pin1_on_expander=False, pin2=4, pin2_on_expander=False, pin3=36, pin3_on_expander=False, pin4=13, pin4_on_expander=False),
                    ModuleConfig('CanV06', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                    ModuleConfig('IigiirV02', socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True)
                ]
            ),
            'rb45': BrainConfig(
                flags=['nand', 'orin', 'v05'],
                modules=[
                    ModuleConfig('Rs485V05', socket=1, pin1=26, pin1_on_expander=False, pin2=27, pin2_on_expander=False, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=2, pin1=5, pin1_on_expander=False, pin2=4, pin2_on_expander=False, pin3=36, pin3_on_expander=False, pin4=13, pin4_on_expander=False),
                    ModuleConfig('CanV06', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                    ModuleConfig('IigiirV02', socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True)
                ]
            ),
            'rb46': BrainConfig(
                flags=['nand', 'orin', 'v05'],
                modules=[
                    ModuleConfig('Rs485V05', socket=1, pin1=26, pin1_on_expander=True, pin2=27, pin2_on_expander=True, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=2, pin1=5, pin1_on_expander=False, pin2=4, pin2_on_expander=False, pin3=36, pin3_on_expander=False, pin4=13, pin4_on_expander=False),
                    ModuleConfig('CanV06', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=4, pin1=5, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=33, pin4_on_expander=True),
                    ModuleConfig('BumperV03', socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=6, pin1=12, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=25, pin3_on_expander=True, pin4=22, pin4_on_expander=True)
                ]
            ),
            'rb47': BrainConfig(
                flags=['nand', 'orin', 'v05'],
                modules=[
                    ModuleConfig('Rs485V05', socket=1, pin1=26, pin1_on_expander=True, pin2=27, pin2_on_expander=True, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=2, pin1=5, pin1_on_expander=False, pin2=4, pin2_on_expander=False, pin3=36, pin3_on_expander=False, pin4=13, pin4_on_expander=False),
                    ModuleConfig('CanV06', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=4, pin1=5, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=33, pin4_on_expander=True),
                    ModuleConfig('BumperV03', socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=6, pin1=12, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=25, pin3_on_expander=True, pin4=22, pin4_on_expander=True)
                ]
            ),
            'rb48': BrainConfig(
                flags=['nand', 'orin', 'v05'],
                modules=[
                    ModuleConfig('Rs485V05', socket=1, pin1=26, pin1_on_expander=True, pin2=27, pin2_on_expander=True, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=2, pin1=5, pin1_on_expander=False, pin2=4, pin2_on_expander=False, pin3=36, pin3_on_expander=False, pin4=13, pin4_on_expander=False),
                    ModuleConfig('CanV06', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=4, pin1=5, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=33, pin4_on_expander=True),
                    ModuleConfig('BumperV03', socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=6, pin1=12, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=25, pin3_on_expander=True, pin4=22, pin4_on_expander=True)
                ]
            ),
            'rb49': BrainConfig(
                flags=['nand', 'orin', 'v05'],
                modules=[
                    ModuleConfig('Rs485V05', socket=1, pin1=26, pin1_on_expander=True, pin2=27, pin2_on_expander=True, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=2, pin1=5, pin1_on_expander=False, pin2=4, pin2_on_expander=False, pin3=36, pin3_on_expander=False, pin4=13, pin4_on_expander=False),
                    #ModuleConfig('CanV06', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=4, pin1=5, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=33, pin4_on_expander=True),
                    ModuleConfig('BumperV03', socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True),
                    ModuleConfig('CanV06', socket=6, pin1=22, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=12, pin3_on_expander=True, pin4=25, pin4_on_expander=True)
                ]
            ),
            'rb50': BrainConfig(
                flags=['nand', 'orin', 'v05'],
                modules=[
                    ModuleConfig('Rs485V05', socket=1, pin1=26, pin1_on_expander=True, pin2=27, pin2_on_expander=True, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=2, pin1=5, pin1_on_expander=False, pin2=4, pin2_on_expander=False, pin3=36, pin3_on_expander=False, pin4=13, pin4_on_expander=False),
                    ModuleConfig('CanV06', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=4, pin1=5, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=33, pin4_on_expander=True),
                    ModuleConfig('BumperV03', socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True),
                    # ModuleConfig('CanV06', socket=6, pin1=22, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=12, pin3_on_expander=True, pin4=25, pin4_on_expander=True)
                ]
            ),
            'rb51': BrainConfig(
                flags=['nand', 'orin', 'v05'],
                modules=[
                    ModuleConfig('Rs485V05', socket=1, pin1=26, pin1_on_expander=True, pin2=27, pin2_on_expander=True, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=2, pin1=5, pin1_on_expander=False, pin2=4, pin2_on_expander=False, pin3=36, pin3_on_expander=False, pin4=13, pin4_on_expander=False),
                    # ModuleConfig('CanV06', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=4, pin1=5, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=33, pin4_on_expander=True),
                    ModuleConfig('BumperV03', socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True),
                    ModuleConfig('CanV06', socket=6, pin1=22, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=12, pin3_on_expander=True, pin4=25, pin4_on_expander=True)
                ]
            ),
            'rb52': BrainConfig(
                flags=['nand', 'orin', 'v05'],
                modules=[
                    ModuleConfig('Rs485V05', socket=1, pin1=26, pin1_on_expander=True, pin2=27, pin2_on_expander=True, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=2, pin1=5, pin1_on_expander=False, pin2=4, pin2_on_expander=False, pin3=36, pin3_on_expander=False, pin4=13, pin4_on_expander=False),
                    ModuleConfig('CanV06', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=4, pin1=5, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=33, pin4_on_expander=True),
                    ModuleConfig('BumperV03', socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=6, pin1=12, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=25, pin3_on_expander=True, pin4=22, pin4_on_expander=True)
                ]
            ),
            'rb53': BrainConfig(
                flags=['nand', 'orin', 'v05'],
                modules=[
                    ModuleConfig('Rs485V05', socket=1, pin1=26, pin1_on_expander=True, pin2=27, pin2_on_expander=True, pin3=15, pin3_on_expander=True, pin4=13, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=2, pin1=5, pin1_on_expander=False, pin2=4, pin2_on_expander=False, pin3=36, pin3_on_expander=False, pin4=13, pin4_on_expander=False),
                    ModuleConfig('CanV06', socket=3, pin1=32, pin1_on_expander=False, pin2=33, pin2_on_expander=False, pin3=2, pin3_on_expander=True, pin4=14, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=4, pin1=5, pin1_on_expander=True, pin2=4, pin2_on_expander=True, pin3=32, pin3_on_expander=True, pin4=33, pin4_on_expander=True),
                    ModuleConfig('BumperV03', socket=5, pin1=35, pin1_on_expander=True, pin2=18, pin2_on_expander=True, pin3=21, pin3_on_expander=True, pin4=19, pin4_on_expander=True),
                    ModuleConfig('OogiirV07', socket=6, pin1=12, pin1_on_expander=True, pin2=23, pin2_on_expander=True, pin3=25, pin3_on_expander=True, pin4=22, pin4_on_expander=True)
                ]
            ),
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
        brain = TestBrain(robot_brain_name, self._robot_brain, config.flags, brain_modules)
        return brain
