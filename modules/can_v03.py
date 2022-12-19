import logging

import rosys
from nicegui import ui

from .module import Module


class CanV03(Module):
    def __init__(self, socket: int, robot_brain: rosys.hardware.RobotBrain) -> None:
        super().__init__(socket, robot_brain)
        self.in_1_status = False
        self.in_2_status = False
        self.log = logging.getLogger('test_brain.can_v03')

        with ui.card():
            ui.markdown(f'###### Socket {self.socket}: can_v03')
            with ui.row():
                with ui.column():
                    with ui.row():
                        ui.label('rx pin')
                        ui.button('send can massage', on_click=self.send_can)
                    with ui.row():
                        ui.label('tx pin')

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

    async def send_can(self):
        await self.robot_brain.send('can.send(1,2,3,4,5,6,7,8)')
