import logging

import rosys
from nicegui import ui

from .module import Module


class Oogiir(Module):
    def __init__(self, socket: int, robot_brain: rosys.hardware.RobotBrain, *, out_1: int = 0, out_1_p0: bool = False,
                 out_2: int = 0, out_2_p0: bool = False, in_1: int = 0, in_1_p0: bool = False, in_2: int = 0,
                 in_2_p0: bool = False) -> None:
        super().__init__(socket, robot_brain)
        self.out_1 = out_1
        self.out_1_p0 = out_1_p0
        self.out_2 = out_2
        self.out_2_p0 = out_2_p0
        self.in_1 = in_1
        self.in_1_p0 = in_1_p0
        self.in_1_status = False
        self.in_2 = in_2
        self.in_2_p0 = in_2_p0
        self.in_2_status = False
        self.log = logging.getLogger('test_brain.oogiir')

        with ui.card():
            ui.markdown(f'###### Socket {self.socket}: oogiir')
            with ui.row():
                with ui.column():
                    with ui.row():
                        ui.number('out_1 pin', format='%.f', value=0).bind_value(self, 'out_1')
                        ui.switch('p0', on_change=lambda e: ui.notify(
                            'Switched' if e.value else 'Unswitched')).bind_value(self, 'out_1_p0')
                        ui.button('send On', on_click=self.send_out_1)
                    with ui.row():
                        ui.number('out_2 pin', format='%.f', value=0).bind_value(self, 'out_2')
                        ui.switch('p0', on_change=lambda e: ui.notify(
                            'Switched' if e.value else 'Unswitched')).bind_value(self, 'out_2_p0')
                        ui.button('send On', on_click=self.send_out_2)
                    with ui.row():
                        ui.number('in_1 pin', format='%.f', value=0).bind_value(self, 'in_1')
                        ui.switch('p0', on_change=lambda e: ui.notify(
                            'Switched' if e.value else 'Unswitched')).bind_value(self, 'in_1_p0')
                        ui.icon('highlight_off').classes('text-red').bind_visibility_from(self,
                                                                                          'in_1_status', backward=lambda x: not x)
                        ui.icon('check_circle_outline').classes(
                            'text-green').bind_visibility_from(self, 'in_1_status')
                    with ui.row():
                        ui.number('in_2 pin', format='%.f', value=0).bind_value(self, 'in_2')
                        ui.switch('p0', on_change=lambda e: ui.notify(
                            'Switched' if e.value else 'Unswitched')).bind_value(self, 'in_2_p0')
                        ui.icon('highlight_off').classes('text-red').bind_visibility_from(self,
                                                                                          'in_2_status', backward=lambda x: not x)
                        ui.icon('check_circle_outline').classes(
                            'text-green').bind_visibility_from(self, 'in_2_status')

    async def send_out_1(self):
        self.log.info('send output')

        await self.send_output(round(self.out_1), self.out_1_p0)

    async def send_out_2(self):
        self.log.info('send output')

        await self.send_output(round(self.out_2), self.out_2_p0)
