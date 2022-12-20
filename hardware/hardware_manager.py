import logging

import rosys
from nicegui import ui

import modules


class HardwareManager():
    def __init__(self, robot_brain: rosys.hardware.RobotBrain) -> None:

        self.UPDATED = rosys.event.Event()
        '''the hardware state has been updated'''

        self.robot_brain = robot_brain
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

    async def set_sockets(self) -> None:
        self.log.info(f'my socket names are {self.sockets}')
        for socket, name in self.sockets.items():
            if name == 'rs485_v04':
                self.modules[socket-1] = modules.Rs485V04(socket, self.robot_brain)
            if name == 'oogoor_v01':
                self.modules[socket-1] = modules.OogoorV01(socket, self.robot_brain)
            if name == 'oogiir_v06':
                self.modules[socket-1] = modules.OogiirV06(socket, self.robot_brain)
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
        self.sockets_set = True
        self.log.info(f'my modules are {self.modules} ')

    async def update(self) -> None:
        for time, line in await self.robot_brain.read_lines():
            words = line.split()

            # core
            if words[0] == 'core':
                words.pop(0)
                words.pop(0)

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

                    elif words[0] == '"oogiir_v01"':
                        self.sockets[socket] = 'oogiir_v06'
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

                    elif words[0] == '"can_v03"':
                        self.sockets[socket] = 'can_v03'
                        words.pop(0)
                        if self.sockets_set:
                            self.modules[socket-1].in_1_status = int(words.pop(0)) == 1
                            self.modules[socket-1].in_2_status = int(words.pop(0)) == 1
                        else:
                            words.pop(0)
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

            if line.startswith('can') or line.startswith('p0: can'):
                for socket, name in self.sockets.items():
                    if name == 'can_v04' or name == 'can_v03':
                        await self.modules[socket-1].read_can(line)
                        return

            if line.startswith('rs485') or line.startswith('p0: rs485'):
                for socket, name in self.sockets.items():
                    if name == 'rs485_v04':
                        await self.modules[socket-1].read_rs485(line)
                        return

        self.UPDATED.emit()
