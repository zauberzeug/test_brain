import logging

import rosys
from nicegui import ui
from rosys.helpers import remove_indentation

from .module import Module


class Rs485(Module):
    def __init__(self, *,
                 robot_brain: rosys.hardware.RobotBrain,
                 socket: int,
                 pin1: int, pin1_on_expander: bool = False,
                 pin2: int, pin2_on_expander: bool = False,
                 pin3: int, pin3_on_expander: bool = False,
                 pin4: int, pin4_on_expander: bool = False) -> None:
        super().__init__(robot_brain=robot_brain,
                         socket=socket,
                         pin1=pin1, pin1_on_expander=pin1_on_expander,
                         pin2=pin2, pin2_on_expander=pin2_on_expander,
                         pin3=pin3, pin3_on_expander=pin3_on_expander,
                         pin4=pin4, pin4_on_expander=pin4_on_expander)
        self.log = logging.getLogger('test_brain.rs485')
        self.ui_log: ui.log | None = None

    async def read_rs485(self, msg: str):
        pass


class Rs485V03(Rs485):
    def __init__(self, *,
                 robot_brain: rosys.hardware.RobotBrain,
                 socket: int,
                 pin1: int, pin1_on_expander: bool = False,
                 pin2: int, pin2_on_expander: bool = False,
                 pin3: int, pin3_on_expander: bool = False,
                 pin4: int, pin4_on_expander: bool = False) -> None:
        super().__init__(robot_brain=robot_brain,
                         socket=socket,
                         pin1=pin1, pin1_on_expander=pin1_on_expander,
                         pin2=pin2, pin2_on_expander=pin2_on_expander,
                         pin3=pin3, pin3_on_expander=pin3_on_expander,
                         pin4=pin4, pin4_on_expander=pin4_on_expander)
        self.in_1_status = False
        self.in_2_status = False
        self.lizard_code = remove_indentation(f'''
        s{self.socket}_rs485 = p0.Serial({self.pin1}, {self.pin2}, 9600, 2)
        s{self.socket}_rs485.unmute()
        s{self.socket}_in_1 = {"p0." if self.pin3_on_expander else ""}Input({self.pin3})
        s{self.socket}_in_2 = {"p0." if self.pin4_on_expander else ""}Input({self.pin4})
        ''')

        self.core_message_fields = [f's{self.socket}_in_1.level', f's{self.socket}_in_2.level']

    def developer_ui(self):
        with ui.card():
            ui.markdown(f'**Socket {self.socket}: rs485_v03**')
            with ui.row():
                with ui.column():
                    with ui.row():
                        ui.button('send rs485 message', on_click=self.send_rs485)
                    with ui.row():
                        ui.label('rs485 log:')
                        self.ui_log = ui.log(max_lines=10).classes('w-full h-20')
                    with ui.row():
                        ui.label('in_1 pin')
                        ui.icon('highlight_off').classes('text-red').bind_visibility_from(self,
                                                                                          'in_1_status', backward=lambda x: not x)
                        ui.icon('check_circle_outline').classes(
                            'text-green').bind_visibility_from(self, 'in_1_status')
                    with ui.row():
                        ui.label('in_2 pin')
                        ui.icon('highlight_off').classes('text-red').bind_visibility_from(self,
                                                                                          'in_2_status', backward=lambda x: not x)
                        ui.icon('check_circle_outline').classes(
                            'text-green').bind_visibility_from(self, 'in_2_status')

    def handle_core_output(self,words:list[str]):
        self.in_1_status = int(words.pop(0)) == 1
        self.in_2_status = int(words.pop(0)) == 1

    async def read_rs485(self, msg: str):
        assert self.ui_log is not None
        self.log.debug('Rs485V03: %s', msg)
        self.ui_log.push(msg)

class Rs485V04(Rs485):
    def __init__(self, *,
                 robot_brain: rosys.hardware.RobotBrain,
                 socket: int,
                 pin1: int, pin1_on_expander: bool = False,
                 pin2: int, pin2_on_expander: bool = False,
                 pin3: int, pin3_on_expander: bool = False,
                 pin4: int, pin4_on_expander: bool = False) -> None:
        super().__init__(robot_brain=robot_brain,
                         socket=socket,
                         pin1=pin1, pin1_on_expander=pin1_on_expander,
                         pin2=pin2, pin2_on_expander=pin2_on_expander,
                         pin3=pin3, pin3_on_expander=pin3_on_expander,
                         pin4=pin4, pin4_on_expander=pin4_on_expander)
        self.out_1_value = False
        self.in_1_status = False
        self.log = logging.getLogger('test_brain.rs485_v05')
        self.lizard_code = remove_indentation(
        f'''
        s{self.socket}_rs485 = p0.Serial({self.pin1}, {self.pin2}, 9600, 2)
        s{self.socket}_rs485.unmute()
        s{self.socket}_out_1 = {"p0." if self.pin3_on_expander else ""}Output({self.pin3})
        s{self.socket}_in_1 = {"p0." if self.pin4_on_expander else ""}Input({self.pin4})
        ''')
        self.core_message_fields = [f's{self.socket}_in_1.level']

    def developer_ui(self):
        with ui.card():
            ui.markdown(f'**Socket {self.socket}: rs485_v05**')
            with ui.row():
                with ui.column():
                    with ui.row():
                        ui.button('send rs485 message', on_click=self.send_rs485)
                    with ui.row():
                        ui.label('rs485 log:')
                        self.ui_log = ui.log(max_lines=10).classes('w-full h-20')
                    with ui.row():
                        ui.label('out_1')
                        ui.switch(value=False, on_change=self.send_out_1).bind_value(self, 'out_1_value')
                    with ui.row():
                        ui.label('in_1 pin')
                        ui.icon('highlight_off').classes('text-red').bind_visibility_from(self,
                                                                                          'in_1_status', backward=lambda x: not x)
                        ui.icon('check_circle_outline').classes(
                            'text-green').bind_visibility_from(self, 'in_1_status')
    def handle_core_output(self,words:list[str]):
        self.in_1_status = int(words.pop(0)) == 1

    async def send_out_1(self):
        await self.send_out(1, self.out_1_value)

    async def read_rs485(self, msg: str):
        assert self.ui_log is not None
        self.log.debug('Rs485V04: %s', msg)
        self.ui_log.push(msg)


class Rs485V05(Rs485V04):
    ...


class Rs485V051(Rs485):
    def __init__(self, *,
                 robot_brain: rosys.hardware.RobotBrain,
                 socket: int,
                 pin1: int, pin1_on_expander: bool = False,
                 pin2: int, pin2_on_expander: bool = False,
                 pin3: int, pin3_on_expander: bool = False,
                 pin4: int, pin4_on_expander: bool = False) -> None:
        super().__init__(robot_brain=robot_brain,
                         socket=socket,
                         pin1=pin1, pin1_on_expander=pin1_on_expander,
                         pin2=pin2, pin2_on_expander=pin2_on_expander,
                         pin3=pin3, pin3_on_expander=pin3_on_expander,
                         pin4=pin4, pin4_on_expander=pin4_on_expander)
        self.out_1_value = False
        self.in_1_status = False
        self.log = logging.getLogger('test_brain.rs485_v05')
        self.lizard_code = remove_indentation(
        f'''
        s{self.socket}_rs485 = Serial({self.pin1}, {self.pin2}, 9600, 2)
        s{self.socket}_rs485.unmute()
        s{self.socket}_out_1 = {"p0." if self.pin3_on_expander else ""}Output({self.pin3})
        s{self.socket}_in_1 = {"p0." if self.pin4_on_expander else ""}Input({self.pin4})
        ''')
        self.core_message_fields = [f's{self.socket}_in_1.level']

    def developer_ui(self):
        with ui.card():
            ui.markdown(f'**Socket {self.socket}: rs485_v05**')
            with ui.row():
                with ui.column():
                    with ui.row():
                        ui.button('send rs485 message', on_click=self.send_rs485)
                    with ui.row():
                        ui.label('rs485 log:')
                        self.ui_log = ui.log(max_lines=10).classes('w-full h-20')
                    with ui.row():
                        ui.label('out_1')
                        ui.switch(value=False, on_change=self.send_out_1).bind_value(self, 'out_1_value')
                    with ui.row():
                        ui.label('in_1 pin')
                        ui.icon('highlight_off').classes('text-red').bind_visibility_from(self,
                                                                                          'in_1_status', backward=lambda x: not x)
                        ui.icon('check_circle_outline').classes(
                            'text-green').bind_visibility_from(self, 'in_1_status')
    def handle_core_output(self,words:list[str]):
        self.in_1_status = int(words.pop(0)) == 1

    async def send_out_1(self):
        await self.send_out(1, self.out_1_value)

    async def read_rs485(self, msg: str):
        assert self.ui_log is not None
        self.log.debug('Rs485V051: %s', msg)
        self.ui_log.push(msg)