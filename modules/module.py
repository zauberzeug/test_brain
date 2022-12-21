import abc

import rosys


class Module(abc.ABC):
    def __init__(self, socket: int, robot_brain: rosys.hardware.RobotBrain) -> None:
        self.socket = socket
        self.robot_brain = robot_brain

    async def send_out(self, pin: int, value: bool):
        self.log.info(f'send {"on" if value else "off"} socket {self.socket} out_{pin}')
        await self.robot_brain.send(f's{self.socket}_out_{pin}.{"on" if value else "off"}()')

    async def send_can(self):
        await self.robot_brain.send(f's{self.socket}_can.send(0x{self.socket}00, 1, 2, 3, 4, 5, 6, 7, 8)')

    async def send_rs485(self):
        await self.robot_brain.send(f's{self.socket}_rs485.send(1, 2, 3, 4, 5, 6, 7, 8)')
