import logging

import rosys
from nicegui import ui
from rosys.hardware import remove_indentation

from .module import Module


class Rs485(Module):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.log = logging.getLogger('test_brain.rs485')


    async def read_rs485(self, msg: str):
        self.rs485_log.push(msg)

class Rs485V03(Rs485):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.in_1_status = False
        self.in_2_status = False
        self.lizard_code = remove_indentation(f'''
        s{self.socket}_rs485 = p0.Serial({self.pin1}, {self.pin2}, 9600, 2)
        s{self.socket}_rs485.unmute()
        s{self.socket}_in_1 = {"p0." if self.pin3_on_exander else ""}Input({self.pin3})
        s{self.socket}_in_2 = {"p0." if self.pin4_on_exander else ""}Input({self.pin4})
                ''')
        
        self.core_message_fields = ['s{self.socket}_in_1.level', 's{self.socket}_in_2.level']

        with ui.card():
            ui.markdown(f'**Socket {self.socket}: rs485_v03**')
            with ui.row():
                with ui.column():
                    with ui.row():
                        ui.button('send rs485 message', on_click=self.send_rs485)
                    with ui.row():
                        ui.label('rs485 log:')
                        self.rs485_log = ui.log(max_lines=10).classes('w-full h-20')
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
        self.in_1_status = words.pop(0) == 1
        self.in_2_status = words.pop(0) == 1

class Rs485V04(Rs485):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.out_1_value = False
        self.in_1_status = False
        self.log = logging.getLogger('test_brain.rs485_v05')
        self.lizard_code = remove_indentation(f'''
        s{self.socket}_rs485 = p0.Serial({self.pin1}, {self.pin2}, 9600, 2)
        s{self.socket}_rs485.unmute()
        s{self.socket}_out_1 = {"p0." if self.pin3_on_exander else ""}Output({self.pin3})
        s{self.socket}_in_1 = {"p0." if self.pin4_on_exander else ""}Input({self.pin4})
                ''')
        self.core_message_fields = ['s{self.socket}_in_1.level']

        with ui.card():
            ui.markdown(f'**Socket {self.socket}: rs485_v05**')
            with ui.row():
                with ui.column():
                    with ui.row():
                        ui.button('send rs485 message', on_click=self.send_rs485)
                    with ui.row():
                        ui.label('rs485 log:')
                        self.rs485_log = ui.log(max_lines=10).classes('w-full h-20')
                    with ui.row():
                        ui.label('out_1')
                        ui.switch(value=False, on_change=self.send_out_1).bind_value(self, 'out_1_value')
                    with ui.row():
                        ui.label('in_1 pin')
                        ui.icon('highlight_off').classes('text-red').bind_visibility_from(self,
                                                                                          'in_1_status', backward=lambda x: not x)
                        ui.icon('check_circle_outline').classes(
                            'text-green').bind_visibility_from(self, 'in_1_status')

    async def send_out_1(self):
        await self.send_out(1, self.out_1_value)

    async def read_rs485(self, msg: str):
        self.rs485_log.push(msg)
    
class Rs485V05(Rs485V04):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
