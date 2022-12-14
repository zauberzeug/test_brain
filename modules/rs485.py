import logging

import rosys
from nicegui import ui

from .module import Module


class Rs485(Module):
    def __init__(self, socket: int, robot_brain: rosys.hardware.RobotBrain):
        super().__init__(socket, robot_brain)
        self.rx = None
        self.tx = None
        self.out_1: int = 0
        self.out_1_p0 = False
        self.in_1: int = 0
        self.in_1_status = False
        self.log = logging.getLogger('test_brain.rs485')

        with ui.card():
            ui.markdown(f'###### Socket {self.socket}: rs485')
            with ui.row():
                with ui.column():
                    ui.number('rx pin', format='%.f', value=0).bind_value_to(self, 'rx')
                    ui.switch('p0', on_change=lambda e: ui.notify('Switched' if e.value else 'Unswitched'))
                    ui.number('tx pin', format='%.f', value=0).bind_value_to(self, 'tx')
                    ui.switch('p0', on_change=lambda e: ui.notify('Switched' if e.value else 'Unswitched'))
                    with ui.row():
                        ui.number('out_1 pin', format='%.f', value=0).bind_value_to(self, 'out_1')
                        ui.switch('p0', on_change=lambda e: ui.notify(
                            'Switched' if e.value else 'Unswitched')).bind_value_to(self, 'out_1_p0')
                        ui.button('send On', on_click=self.send_out_1)
                    with ui.row():
                        ui.number('in_1 pin', format='%.f', value=0).bind_value_to(self, 'in_1')
                        ui.switch('p0', on_change=lambda e: ui.notify('Switched' if e.value else 'Unswitched'))
                        ui.icon('highlight_off').classes('text-red').bind_visibility_from(self,
                                                                                          'in_1_status', backward=lambda x: not x)
                        ui.icon('check_circle_outline').classes(
                            'text-green').bind_visibility_from(self, 'in_1_status')

    async def send_out_1(self):
        self.log.info('send output')

        await self.send_output(round(self.out_1), self.out_1_p0)
