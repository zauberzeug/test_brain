import logging

import rosys
from nicegui import ui

from .module import Module


class Bumper(Module):
    def __init__(self, socket: int, robot_brain: rosys.hardware.RobotBrain, *, in_1: int = 0, in_1_p0: bool = False,
                 in_2: int = 0, in_2_p0: bool = False, in_3: int = 0, in_3_p0: bool = False, in_4: int = 0,
                 in_4_p0: bool = False) -> None:
        super().__init__(socket, robot_brain)
        self.in_1 = in_1
        self.in_1_p0 = in_1_p0
        self.in_1_status = False
        self.in_2 = in_2
        self.in_2_p0 = in_2_p0
        self.in_2_status = False
        self.in_3 = in_3
        self.in_3_p0 = in_3_p0
        self.in_3_status = False
        self.in_4 = in_4
        self.in_4_p0 = in_4_p0
        self.in_4_status = False
        self.log = logging.getLogger('test_brain.bumper')
        with ui.card():
            ui.markdown(f'###### Socket {self.socket}: bumber')
            with ui.row():
                with ui.column():
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
                    with ui.row():
                        ui.number('in_3 pin', format='%.f', value=0).bind_value(self, 'in_3')
                        ui.switch('p0', on_change=lambda e: ui.notify(
                            'Switched' if e.value else 'Unswitched')).bind_value(self, 'in_3_p0')
                        ui.icon('highlight_off').classes('text-red').bind_visibility_from(self,
                                                                                          'in_3_status', backward=lambda x: not x)
                        ui.icon('check_circle_outline').classes(
                            'text-green').bind_visibility_from(self, 'in_3_status')
                    with ui.row():
                        ui.number('in_4 pin', format='%.f', value=0).bind_value(self, 'in_4')
                        ui.switch('p0', on_change=lambda e: ui.notify(
                            'Switched' if e.value else 'Unswitched')).bind_value(self, 'in_4_p0')
                        ui.icon('highlight_off').classes('text-red').bind_visibility_from(self,
                                                                                          'in_4_status', backward=lambda x: not x)
                        ui.icon('check_circle_outline').classes(
                            'text-green').bind_visibility_from(self, 'in_4_status')
