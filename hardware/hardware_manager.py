import logging

import rosys

from modules import Module


class HardwareManager():
    def __init__(self, robot_brain: rosys.hardware.RobotBrain, *,
                 socket_1: Module = None,
                 socket_2: Module = None,
                 socket_3: Module = None,
                 socket_4: Module = None,
                 socket_5: Module = None,
                 socket_6: Module = None
                 ) -> None:

        self.UPDATED = rosys.event.Event()
        '''the hardware state has been updated'''

        self.robot_brain = robot_brain
        self.sockets = {
            'socket_1': socket_1,
            'socket_2': socket_2,
            'socket_3': socket_3,
            'socket_4': socket_4,
            'socket_5': socket_5,
            'socket_6': socket_6,
        }

        self.log = logging.getLogger('test_brain.hardware_manager')

        rosys.on_repeat(self.update, 0.01)

    async def update(self) -> None:

        for time, line in await self.robot_brain.read_lines():
            words = line.split()

            # core
            if words[0] == 'core':
                words.pop(0)
                words.pop(0)

            for socket, module in self.sockets.items():
                if words[0] == '"rs485"':
                    words.pop(0)
                    module.in_1_status = int(words.pop(0)) == 1

                elif words[0] == '"oogoor"':
                    words.pop(0)

                elif words[0] == '"oogiir"':
                    words.pop(0)
                    module.in_1_status = int(words.pop(0)) == 1
                    module.in_2_status = int(words.pop(0)) == 1

                elif words[0] == '"can"':
                    words.pop(0)
                    module.in_1_status = int(words.pop(0)) == 1

                elif words[0] == '"bumper"':
                    words.pop(0)
                    module.in_1_status = int(words.pop(0)) == 1
                    module.in_2_status = int(words.pop(0)) == 1
                    module.in_3_status = int(words.pop(0)) == 1
                    module.in_4_status = int(words.pop(0)) == 1

                elif words[0] == '"none"':
                    words.pop(0)

        self.UPDATED.emit()
