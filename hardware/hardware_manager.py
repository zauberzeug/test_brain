import logging
from pathlib import Path

import rosys
from nicegui import ui

import modules


class HardwareManager():
    def __init__(self, robot_brain: rosys.hardware.RobotBrain, lizard_startup: str) -> None:

        self.UPDATED = rosys.event.Event()
        '''the hardware state has been updated'''
        self.lizard_startup = Path(lizard_startup)
        self.robot_brain = robot_brain
        self.robot_brain.lizard_code = self.generate_lizard_code()
        self.heap = 0.0
        self.rdyp = True
        self.en3 = True
        self.sockets = {
            1: 'none',
            2: 'none',
            3: 'none',
            4: 'none',
            5: 'none',
            6: 'none',
        }
        self.modules = [
            None,
            None,
            None,
            None,
            None,
            None
        ]

        self.sockets_set: bool = False
        self.rdyp_status: bool = False
        self.vdp_status: bool = False

        self.log = logging.getLogger('test_brain.hardware_manager')

        rosys.on_repeat(self.update, 0.01)

    def generate_lizard_code(self) -> str:
        if not self.lizard_startup.exists():
            rosys.notify('No Lizard startup file found')
            return
        code = self.lizard_startup.read_text()
        return code

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

    async def set_sockets(self) -> None:
        self.log.info(f'my socket names are {self.sockets}')
        for socket, name in self.sockets.items():
            if name == 'rs485_v04':
                self.modules[socket-1] = modules.Rs485V04(socket, self.robot_brain)
            if name == 'oogoor_v01':
                self.modules[socket-1] = modules.OogoorV01(socket, self.robot_brain)
            if name == 'oogiir_v06':
                self.modules[socket-1] = modules.OogiirV06(socket, self.robot_brain)
            if name == 'oogiir_v07':
                self.modules[socket-1] = modules.OogiirV07(socket, self.robot_brain)
            if name == 'can_v04':
                self.modules[socket-1] = modules.CanV04(socket, self.robot_brain)
            if name == 'bumper_v02':
                self.modules[socket-1] = modules.BumperV02(socket, self.robot_brain)
            if name == 'none':
                self.modules[socket-1] = None
            if name == 'can_v03':
                self.modules[socket-1] = modules.CanV03(socket, self.robot_brain)
            if name == 'oogiir_v05':
                self.modules[socket-1] = modules.OogiirV05(socket, self.robot_brain)
            if name == 'oiio':
                self.modules[socket-1] = modules.Oiio(socket, self.robot_brain)
            if name == 'rs485_v03':
                self.modules[socket-1] = modules.Rs485V03(socket, self.robot_brain)
            if name == 'oogoir_v02':
                self.modules[socket-1] = modules.OogoirV02(socket, self.robot_brain)
            if name == 'iigiir_v01':
                self.modules[socket-1] = modules.IigiirV01(socket, self.robot_brain)
        self.sockets_set = True
        self.log.info(f'my modules are {self.modules} ')

    async def update(self) -> None:
        for time, line in await self.robot_brain.read_lines():
            words = line.split()

            # core
            if words[0] == 'core' or words[0] == 'p0':
                words.pop(0)
                words.pop(0)

                self.heap = float(words.pop(0))

                self.rdyp_status = int(words.pop(0)) == 0
                self.vdp_status = int(words.pop(0)) == 0

                for socket, name in self.sockets.items():
                    if words[0] == '"rs485_v04"':
                        self.sockets[socket] = 'rs485_v04'
                        words.pop(0)
                        if self.sockets_set:
                            self.modules[socket-1].in_1_status = int(words.pop(0)) == 1
                        else:
                            words.pop(0)

                    elif words[0] == '"oogoor_v01"':
                        self.sockets[socket] = 'oogoor_v01'
                        words.pop(0)

                    elif words[0] == '"oogiir_v06"':
                        self.sockets[socket] = 'oogiir_v06'
                        words.pop(0)
                        if self.sockets_set:
                            self.modules[socket-1].in_1_status = int(words.pop(0)) == 1
                            self.modules[socket-1].in_2_status = int(words.pop(0)) == 1
                        else:
                            words.pop(0)
                            words.pop(0)

                    elif words[0] == '"oogiir_v07"':
                        self.sockets[socket] = 'oogiir_v07'
                        words.pop(0)
                        if self.sockets_set:
                            self.modules[socket-1].in_1_status = int(words.pop(0)) == 1
                            self.modules[socket-1].in_2_status = int(words.pop(0)) == 1
                        else:
                            words.pop(0)
                            words.pop(0)

                    elif words[0] == '"can_v03"':
                        self.sockets[socket] = 'can_v03'
                        words.pop(0)
                        if self.sockets_set:
                            self.modules[socket-1].in_1_status = int(words.pop(0)) == 1
                            self.modules[socket-1].in_2_status = int(words.pop(0)) == 1
                        else:
                            words.pop(0)
                            words.pop(0)

                    elif words[0] == '"can_v04"':
                        self.sockets[socket] = 'can_v04'
                        words.pop(0)
                        if self.sockets_set:
                            self.modules[socket-1].in_1_status = int(words.pop(0)) == 1
                        else:
                            words.pop(0)

                    elif words[0] == '"bumper_v02"':
                        self.sockets[socket] = 'bumper_v02'
                        words.pop(0)
                        if self.sockets_set:
                            self.modules[socket-1].in_1_status = int(words.pop(0)) == 1
                            self.modules[socket-1].in_2_status = int(words.pop(0)) == 1
                            self.modules[socket-1].in_3_status = int(words.pop(0)) == 1
                            self.modules[socket-1].in_4_status = int(words.pop(0)) == 1
                        else:
                            words.pop(0)
                            words.pop(0)
                            words.pop(0)
                            words.pop(0)

                    elif words[0] == '"none"':
                        self.sockets[socket] = 'none'
                        words.pop(0)

                    elif words[0] == '"oogiir_v05"':
                        self.sockets[socket] = 'oogiir_v05'
                        words.pop(0)
                        if self.sockets_set:
                            self.modules[socket-1].in_1_status = int(words.pop(0)) == 1
                            self.modules[socket-1].in_2_status = int(words.pop(0)) == 1
                        else:
                            words.pop(0)
                            words.pop(0)

                    elif words[0] == '"oiio"':
                        self.sockets[socket] = 'oiio'
                        words.pop(0)
                        if self.sockets_set:
                            self.modules[socket-1].in_1_status = int(words.pop(0)) == 1
                            self.modules[socket-1].in_2_status = int(words.pop(0)) == 1
                        else:
                            words.pop(0)
                            words.pop(0)

                    elif words[0] == '"rs485_v03"':
                        self.sockets[socket] = 'rs485_v03'
                        words.pop(0)
                        if self.sockets_set:
                            self.modules[socket-1].in_1_status = int(words.pop(0)) == 1
                            self.modules[socket-1].in_2_status = int(words.pop(0)) == 1
                        else:
                            words.pop(0)
                            words.pop(0)

                    elif words[0] == '"oogoir_v02"':
                        self.sockets[socket] = 'oogoir_v02'
                        words.pop(0)
                        if self.sockets_set:
                            self.modules[socket-1].in_1_status = int(words.pop(0)) == 1
                        else:
                            words.pop(0)

                    elif words[0] == '"iigiir_v01"':
                        self.sockets[socket] = 'iigiir_v01'
                        words.pop(0)
                        if self.sockets_set:
                            self.modules[socket-1].in_1_status = int(words.pop(0)) == 1
                            self.modules[socket-1].in_2_status = int(words.pop(0)) == 1
                            self.modules[socket-1].in_3_status = int(words.pop(0)) == 1
                            self.modules[socket-1].in_4_status = int(words.pop(0)) == 1
                        else:
                            words.pop(0)
                            words.pop(0)
                            words.pop(0)
                            words.pop(0)

            if line.startswith('can', 3) or line.startswith('can', 7):
                for socket, name in self.sockets.items():
                    if name == 'can_v04' or name == 'can_v03':
                        await self.modules[socket-1].read_can(line)

            if line.startswith('rs485', 3) or line.startswith('rs485', 7):
                for socket, name in self.sockets.items():
                    if socket == int(line[1]) or socket == int(line[5]):
                        await self.modules[socket-1].read_rs485(line)

        self.UPDATED.emit()
