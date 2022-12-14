import logging

import rosys
from nicegui import ui

from .module import Module


class Can(Module):
    def __init__(self, socket: int, robot_brain: rosys.hardware.RobotBrain):
        super().__init__(socket, robot_brain)
        self.rx = None
        self.tx = None
        self.out_1 = None
        self.in_1 = None
        self.in_1_status = False
        with ui.card():
            ui.markdown(f'###### Socket {self.socket}: can')
            with ui.row():
                with ui.column():
                    ui.number('rx pin').bind_value_to(self, 'rx')
                    ui.switch('p0', on_change=lambda e: ui.notify('Switched' if e.value else 'Unswitched'))
                    ui.number('tx pin').bind_value_to(self, 'tx')
                    ui.switch('p0', on_change=lambda e: ui.notify('Switched' if e.value else 'Unswitched'))
                    with ui.row():
                        ui.number('out_1 pin').bind_value_to(self, 'out_1')
                        ui.switch('p0', on_change=lambda e: ui.notify('Switched' if e.value else 'Unswitched'))
                        ui.button('send On', on_click=lambda: ui.notify(f'You clicked me!'))
                    with ui.row():
                        ui.number('in_1 pin').bind_value_to(self, 'in_1')
                        ui.switch('p0', on_change=lambda e: ui.notify('Switched' if e.value else 'Unswitched'))
                        ui.icon('highlight_off').classes('text-red').bind_visibility_from(self,
                                                                                          'in_1_status', backward=lambda x: not x)
                        ui.icon('check_circle_outline').classes(
                            'text-green').bind_visibility_from(self, 'in_1_status')
