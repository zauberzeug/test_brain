import logging

import rosys
from nicegui import ui

from .module import Module


class Rs485V03(Module):
    def __init__(self, socket: int, robot_brain: rosys.hardware.RobotBrain) -> None:
        super().__init__(socket, robot_brain)
        self.in_1_status = False
        self.in_2_status = False
        self.log = logging.getLogger('test_brain.rs485_v03')

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

    async def send_rs485(self):
        await self.robot_brain.send('rs485.send(1, 2, 3, 4, 5, 6, 7, 8)')

    async def read_rs485(self, msg: str):
        self.rs485_log.push(msg)
