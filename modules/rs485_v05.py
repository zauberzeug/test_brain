import logging

import rosys
from nicegui import ui

from .module import Module


class Rs485V05(Module):
    def __init__(self, socket: int, robot_brain: rosys.hardware.RobotBrain) -> None:
        super().__init__(socket, robot_brain)
        self.out_1_value = False
        self.in_1_status = False
        self.log = logging.getLogger('test_brain.rs485_v05')

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
