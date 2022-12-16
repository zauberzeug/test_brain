import abc

import rosys


class Module(abc.ABC):
    def __init__(self, socket: int, robot_brain: rosys.hardware.RobotBrain) -> None:
        self.socket = socket
        self.robot_brain = robot_brain

    async def send_out(self, pin: int, value: bool):
        self.log.info(f'send {"on" if value else "off"} socket {self.socket} out_{pin}')
        await self.robot_brain.send(f's{self.socket}_out_{pin}.{"on" if value else "off"}()')
