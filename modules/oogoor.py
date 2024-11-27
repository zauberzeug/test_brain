import logging

import rosys
from nicegui import ui
from rosys.hardware import remove_indentation

from .module import Module


class Oogoor(Module):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.out_1_value = False
        self.out_2_value = False
        self.out_3_value = False
        self.out_4_value = False
        self.log = logging.getLogger('test_brain.oogoor')
        self.lizard_code = remove_indentation(f'''
        s{self.socket}_out_1 = {"p0." if self.pin1_on_exander else ""}Output({self.pin1})
        s{self.socket}_out_2 = {"p0." if self.pin2_on_exander else ""}Output({self.pin2})
        s{self.socket}_out_3 = {"p0." if self.pin3_on_exander else ""}Output({self.pin3})
        s{self.socket}_out_4 = {"p0." if self.pin4_on_exander else ""}Output({self.pin4})
        ''')


        with ui.card():
            ui.markdown(f'**Socket {self.socket}: oogoor**')
            with ui.row():
                with ui.column():
                    with ui.row():
                        ui.label('out_1')
                        ui.switch(value=False, on_change=self.send_out_1).bind_value(self, 'out_1_value')
                    with ui.row():
                        ui.label('out_2')
                        ui.switch(value=False, on_change=self.send_out_2).bind_value(self, 'out_2_value')
                    with ui.row():
                        ui.label('out_3')
                        ui.switch(value=False, on_change=self.send_out_3).bind_value(self, 'out_3_value')
                    with ui.row():
                        ui.label('out_4')
                        ui.switch(value=False, on_change=self.send_out_4).bind_value(self, 'out_4_value')


    async def send_out_1(self):
        await self.send_out(1, self.out_1_value)

    async def send_out_2(self):
        await self.send_out(2, self.out_2_value)

    async def send_out_3(self):
        await self.send_out(3, self.out_3_value)

    async def send_out_4(self):
        await self.send_out(4, self.out_4_value)

class OogoorV01(Oogoor):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
