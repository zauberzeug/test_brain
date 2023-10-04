import logging

import rosys
from nicegui import ui

from .module import Module


class OogoirV02(Module):
    def __init__(self, socket: int, robot_brain: rosys.hardware.RobotBrain) -> None:
        super().__init__(socket, robot_brain)
        self.in_1_status = False
        self.out_1_value = False
        self.out_2_value = False
        self.out_3_value = False
        self.log = logging.getLogger('test_brain.oogoir_v02')

        with ui.card():
            ui.markdown(f'**Socket {self.socket}: oogoir_v02**')
            with ui.row():
                with ui.column():
                    with ui.row():
                        ui.label('out_1')
                        ui.switch(value=False, on_change=self.send_out_1).bind_value(self, 'out_1_value')
                    with ui.row():
                        ui.label('out_2')
                        ui.switch(value=False, on_change=self.send_out_2).bind_value(self, 'out_2_value')
                    with ui.row():
                        ui.label('out_3 pin')
                        ui.switch(value=False, on_change=self.send_out_3).bind_value(self, 'out_3_value')
                    with ui.row():
                        ui.label('in_1 pin')
                        ui.icon('highlight_off').classes('text-red').bind_visibility_from(self,
                                                                                          'in_1_status', backward=lambda x: not x)
                        ui.icon('check_circle_outline').classes(
                            'text-green').bind_visibility_from(self, 'in_1_status')

    async def send_out_1(self):
        await self.send_out(1, self.out_1_value)

    async def send_out_2(self):
        await self.send_out(2, self.out_2_value)

    async def send_out_3(self):
        await self.send_out(3, self.out_3_value)
