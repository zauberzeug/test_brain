import abc

import rosys


class Module(rosys.hardware.Module, abc.ABC):
    def __init__(self,*, robot_brain: rosys.hardware.RobotBrain, 
                 pin1: int, pin1_on_exander: bool, 
                 pin2: int, pin2_on_exander: bool, 
                 pin3: int, pin3_on_exander: bool, 
                 pin4: int, pin4_on_exander: bool,
                 socket:int) -> None:
        self.robot_brain = robot_brain
        self.pin1 = pin1
        self.pin1_on_exander = pin1_on_exander
        self.pin2 = pin2
        self.pin2_on_exander = pin2_on_exander
        self.pin3 = pin3
        self.pin3_on_exander = pin3_on_exander
        self.pin4 = pin4
        self.pin4_on_exander = pin4_on_exander
        self.socket = socket
        self.lizard_code = ''
        self.core_message_fields = []

    def handle_core_output(self,words:list[str]):
        pass
    
    async def send_out(self, pin: int, value: bool):
        self.log.info(f'send {"on" if value else "off"} socket {self.socket} out_{pin}')
        await self.robot_brain.send(f's{self.socket}_out_{pin}.{"on" if value else "off"}()')

    async def send_can(self):
        await self.robot_brain.send(f's{self.socket}_can.send(0x{self.socket}00, 1, 2, 3, 4, 5, 6, 7, 8)')

    async def send_rs485(self):
        await self.robot_brain.send(f's{self.socket}_rs485.send(0xdd, 0xa5, 0x03, 0x00, 0xff, 0xfd, 0x77)')


class EmptyModule(Module):
    def __init__(self,*, robot_brain: rosys.hardware.RobotBrain,
                 pin1: int=0, pin1_on_exander: bool=False, 
                 pin2: int=0, pin2_on_exander: bool=False, 
                 pin3: int=0, pin3_on_exander: bool=False, 
                 pin4: int=0, pin4_on_exander: bool=False,
                 socket:int) -> None:
        super().__init__(robot_brain=robot_brain,
                         pin1=pin1, pin1_on_exander=pin1_on_exander, 
                         pin2=pin2, pin2_on_exander=pin2_on_exander, 
                         pin3=pin3, pin3_on_exander=pin3_on_exander, 
                         pin4=pin4, pin4_on_exander=pin4_on_exander, 
                         socket=socket)
