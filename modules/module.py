import abc

import rosys


class Module(abc.ABC):
    def __init__(self, socket: int, robot_brain: rosys.hardware.RobotBrain) -> None:
        self.socket = socket
        self.robot_brain = robot_brain

    async def send_output(self, pin: int, p0: bool) -> None:
        pin_str = f'output_p0_{pin}' if p0 else f'output_{pin}'
        await self.robot_brain.send(f'{pin_str}.on()')
