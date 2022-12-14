import logging

import rosys
from nicegui import ui

from .module import Module


class Bumper(Module):
    def __init__(self, socket: int, robot_brain: rosys.hardware.RobotBrain):
        super().__init__(socket, robot_brain)
        self.in_1 = None
        self.in_1_status = False
        self.in_2 = None
        self.in_2_status = False
        self.in_3 = None
        self.in_3_status = False
        self.in_4 = None
        self.in_4_status = False
        with ui.card():
            ui.markdown(f'###### Socket {self.socket}: bumber')
            with ui.row():
                with ui.column():
                    with ui.row():
                        ui.number('in_1 pin').bind_value_to(self, 'in_1')
                        ui.switch('p0', on_change=lambda e: ui.notify('Switched' if e.value else 'Unswitched'))
                        ui.icon('highlight_off').classes('text-red').bind_visibility_from(self,
                                                                                          'in_1_status', backward=lambda x: not x)
                        ui.icon('check_circle_outline').classes(
                            'text-green').bind_visibility_from(self, 'in_1_status')
                    with ui.row():
                        ui.number('in_2 pin').bind_value_to(self, 'in_2')
                        ui.switch('p0', on_change=lambda e: ui.notify('Switched' if e.value else 'Unswitched'))
                        ui.icon('highlight_off').classes('text-red').bind_visibility_from(self,
                                                                                          'in_2_status', backward=lambda x: not x)
                        ui.icon('check_circle_outline').classes(
                            'text-green').bind_visibility_from(self, 'in_2_status')
                    with ui.row():
                        ui.number('in_3 pin').bind_value_to(self, 'in_3')
                        ui.switch('p0', on_change=lambda e: ui.notify('Switched' if e.value else 'Unswitched'))
                        ui.icon('highlight_off').classes('text-red').bind_visibility_from(self,
                                                                                          'in_3_status', backward=lambda x: not x)
                        ui.icon('check_circle_outline').classes(
                            'text-green').bind_visibility_from(self, 'in_3_status')
                    with ui.row():
                        ui.number('in_4 pin').bind_value_to(self, 'in_4')
                        ui.switch('p0', on_change=lambda e: ui.notify('Switched' if e.value else 'Unswitched'))
                        ui.icon('highlight_off').classes('text-red').bind_visibility_from(self,
                                                                                          'in_4_status', backward=lambda x: not x)
                        ui.icon('check_circle_outline').classes(
                            'text-green').bind_visibility_from(self, 'in_4_status')
