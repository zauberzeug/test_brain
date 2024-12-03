import abc

import rosys


class Module(rosys.hardware.Module, abc.ABC):
    def __init__(self, *, robot_brain: rosys.hardware.RobotBrain,
                 pin1: int, pin1_on_expander: bool = False,
                 pin2: int, pin2_on_expander: bool = False,
                 pin3: int, pin3_on_expander: bool = False,
                 pin4: int, pin4_on_expander: bool = False,
                 socket:int) -> None:
        super().__init__()
        self.robot_brain = robot_brain
        self.pin1 = pin1
        self.pin1_on_expander = pin1_on_expander
        self.pin2 = pin2
        self.pin2_on_expander = pin2_on_expander
        self.pin3 = pin3
        self.pin3_on_expander = pin3_on_expander
        self.pin4 = pin4
        self.pin4_on_expander = pin4_on_expander
        self.socket = socket
        self.lizard_code = ''
        self.core_message_fields: list[str] = []

    def developer_ui(self):
        pass

    def handle_core_output(self,words:list[str]):
        pass

    async def send_out(self, pin: int, value: bool):
        self.log.info(f'send {"on" if value else "off"} socket {self.socket} out_{pin}')
        await self.robot_brain.send(f's{self.socket}_out_{pin}.{"on" if value else "off"}()')

    async def send_can(self):
        await self.robot_brain.send(f's{self.socket}_can.send(0x{self.socket}00, 1, 2, 3, 4, 5, 6, 7, 8)')

    async def send_rs485(self):
        await self.robot_brain.send(f's{self.socket}_rs485.send(0xdd, 0xa5, 0x03, 0x00, 0xff, 0xfd, 0x77)')
