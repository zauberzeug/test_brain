import logging

import rosys
from nicegui import ui

from .module import Module


class Oogoor(Module):
    def __init__(self, socket: int, robot_brain: rosys.hardware.RobotBrain):
        super().__init__(socket, robot_brain)
        self.out_1: int = 0
        self.out_1_p0 = False
        self.out_2: int = 0
        self.out_2_p0 = False
        self.out_3: int = 0
        self.out_3_p0 = False
        self.out_4: int = 0
        self.out_4_p0 = False
        self.log = logging.getLogger('test_brain.oogoor')
        with ui.card():
            ui.markdown(f'###### Socket {self.socket}: oogoor')
            with ui.row():
                with ui.column():
                    with ui.row():
                        ui.number('out_1 pin', format='%.f', value=0).bind_value_to(self, 'out_1')
                        ui.switch('p0', on_change=lambda e: ui.notify(
                            'Switched' if e.value else 'Unswitched')).bind_value_to(self, 'out_1_p0')
                        ui.button('send On', on_click=self.send_out_1)
                    with ui.row():
                        ui.number('out_2 pin', format='%.f', value=0).bind_value_to(self, 'out_2')
                        ui.switch('p0', on_change=lambda e: ui.notify(
                            'Switched' if e.value else 'Unswitched')).bind_value_to(self, 'out_2_p0')
                        ui.button('send On', on_click=self.send_out_2)
                    with ui.row():
                        ui.number('out_3 pin', format='%.f', value=0).bind_value_to(self, 'out_3')
                        ui.switch('p0', on_change=lambda e: ui.notify(
                            'Switched' if e.value else 'Unswitched')).bind_value_to(self, 'out_3_p0')
                        ui.button('send On', on_click=self.send_out_3)
                    with ui.row():
                        ui.number('out_4 pin', format='%.f', value=0).bind_value_to(self, 'out_4')
                        ui.switch('p0', on_change=lambda e: ui.notify(
                            'Switched' if e.value else 'Unswitched')).bind_value_to(self, 'out_4_p0')
                        ui.button('send On', on_click=self.send_out_4)

    async def send_out_1(self):
        self.log.info('send output')

        await self.send_output(round(self.out_1), self.out_1_p0)

    async def send_out_2(self):
        self.log.info('send output')

        await self.send_output(round(self.out_2), self.out_2_p0)

    async def send_out_3(self):
        self.log.info('send output')

        await self.send_output(round(self.out_3), self.out_3_p0)

    async def send_out_4(self):
        self.log.info('send output')

        await self.send_output(round(self.out_4), self.out_4_p0)
