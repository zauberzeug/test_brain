import logging

import rosys
from nicegui import ui

from .module import Module


class Oogiir(Module):
    def __init__(self, socket: int, robot_brain: rosys.hardware.RobotBrain):
        super().__init__(socket, robot_brain)
        self.out_1 = None
        self.out_2 = None
        self.in_1 = None
        self.in_1_status = False
        self.in_2 = None
        self.in_2_status = False
        with ui.card():
            ui.markdown(f'###### Socket {self.socket}: oogiir')
            with ui.row():
                with ui.column():
                    with ui.row():
                        ui.number('out_1 pin').bind_value_to(self, 'out_1')
                        ui.switch('p0', on_change=lambda e: ui.notify('Switched' if e.value else 'Unswitched'))
                        ui.button('send On', on_click=lambda: ui.notify(f'You clicked me!'))
                    with ui.row():
                        ui.number('out_2 pin').bind_value_to(self, 'out_2')
                        ui.switch('p0', on_change=lambda e: ui.notify('Switched' if e.value else 'Unswitched'))
                        ui.button('send On', on_click=lambda: ui.notify(f'You clicked me!'))
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
                                                                                          'in_1_status', backward=lambda x: not x)
                        ui.icon('check_circle_outline').classes(
                            'text-green').bind_visibility_from(self, 'in_1_status')
