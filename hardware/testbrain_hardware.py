import logging

import rosys
import rosys.hardware
from rosys.helpers import remove_indentation

from modules import *


class TestBrain():
    def __init__(self, robot_brain: rosys.hardware.RobotBrain, flash_params: list[str], modules: list[Module]) -> None:
        self.robot_brain = robot_brain
        self.flash_params = flash_params
        self.modules = modules
        print(f"TestBrain initialized with {len(modules)} modules")  # Debug-Ausgabe
        for module in modules:
            print(f"  Module: {type(module).__name__}")  # Debug-Ausgabe für jedes Modul
        
        self.lizard_code = self.generate_lizard_code()
        self.robot_brain.lizard_code = self.lizard_code
        self.robot_brain.lizard_firmware.flash_params = self.flash_params
        self.active = False
        self.heap = 0.0
        self.rdyp = True
        self.en3 = True
        self.sockets_set: bool = False
        self.rdyp_status: bool = False
        self.vdp_status: bool = False

        self.log = logging.getLogger('test_brain.testbrain_hardware')
        
        rosys.on_repeat(self.update, 0.01)


    def update_lizard(self) -> None:
        self.lizard_code = self.generate_lizard_code()
        self.robot_brain.lizard_code = self.lizard_code
        self.robot_brain.lizard_firmware.flash_params = self.flash_params

    def generate_lizard_code(self) -> str:
        output_fields = ['core.millis','core.heap', 'rdyp_status.level', 'vdp_status.level']
        code = remove_indentation('''
            rdyp = Output(15)
            en3 = Output(12)
            bluetooth = Bluetooth("Test Brain")
            serial = Serial(26, 27, 115200, 1)
            p0 = Expander(serial, 25, 14)
            #imu = Imu()
            ''')
        for module in self.modules:
            if module is None:
                continue
            code += module.lizard_code
            output_fields.extend(module.core_message_fields)
        code += remove_indentation(f'''
            rdyp_status = Input(39)
            vdp_status = p0.Input(39)
            core.output("{' '.join(output_fields)}")
            rdyp.on()
            en3.on()
            ''')    
        return code

    def get_flash_params(self) -> list[str]:
        return self.flash_params

    async def set_en3(self) -> None:
        if self.en3 == True:
            self.log.info('en3 on')
            await self.robot_brain.send('en3.on()')
        else:
            self.log.info('en3 off')
            await self.robot_brain.send('en3.off()')

    async def set_rdyp(self, value: bool) -> None:
        if self.rdyp == True:
            self.log.info('rdyp on')
            await self.robot_brain.send('rdyp.on()')
        else:
            self.log.info('rdyp off')
            await self.robot_brain.send('rdyp.off()')


    async def update(self) -> None:
        if not self.active:
            return
        for time, line in await self.robot_brain.read_lines():
            words = line.split()

            if line.startswith('core'):
                words.pop(0) #pop core.output
                words.pop(0) #pop core.millis
                self.heap = float(words.pop(0))
                self.rdyp_status = int(words.pop(0)) == 1
                self.vdp_status = int(words.pop(0)) == 1

                for module in self.modules:
                    module.handle_core_output(words)
                return
            
            if line.startswith('can', 3) or line.startswith('can', 7):
                for module in self.modules:
                    if module is Can:
                        await module.read_can(line)
                        return

            if line.startswith('rs485', 3) or line.startswith('rs485', 7):
                for module in self.modules:
                    if module is Rs485:
                        await module.read_rs485(line)
                        return
                    