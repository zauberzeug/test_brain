import logging

import rosys
from nicegui import ui

from .module import Module


class OogoorV01(Module):
    def __init__(self, socket: int, robot_brain: rosys.hardware.RobotBrain) -> None:
        super().__init__(socket, robot_brain)
        self.out_1_value = False
        self.out_2_value = False
        self.out_3_value = False
        self.out_4_value = False
        self.log = logging.getLogger('test_brain.oogoor_v01')
        with ui.card():
            ui.markdown(f'###### Socket {self.socket}: oogoor_v01')
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
