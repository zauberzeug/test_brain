import logging
import os

import rosys
from nicegui import ui
from rosys.hardware import EspPins

from .hardware import BrainConfigs, TestBrain


class System:
    def __init__(self, brain_id: str):
        super().__init__()
        self.log = logging.getLogger('test_brain.system')
        rosys.hardware.SerialCommunication.search_paths.insert(0, '/dev/ttyTHS0')
        self.is_real = rosys.hardware.SerialCommunication.is_possible()
        if not self.is_real:
            return
        self.communication = rosys.hardware.SerialCommunication()
        self.robot_brain = rosys.hardware.RobotBrain(self.communication)
        self.test_brain: TestBrain = BrainConfigs(self.robot_brain).get_brain(brain_id)
        self.test_brain.active = True
        self.test_brain.update_lizard()

    def developer_ui(self) -> None:
        with ui.header().props('elevated').classes('q-pa-xs q-pt-sm', remove='q-pa-md items-start gap-4'):
            with ui.row().classes('col-7 justify-end q-pr-md'):
                ui.icon('hardware').classes('text-white')
                ui.label('Hardware').classes('text-white')
                with ui.row():
                    with ui.menu() as menu:
                        ui.menu_item('Rosys Neustarten', on_click=lambda: os.utime('main.py'))
                    ui.button(on_click=menu.open).classes('text-white') \
                        .props('icon=settings size=sm dense unelevated flat')

        with ui.column().classes('w-full no-wrap items-stretch q-px-md'):
            self.test_brain.developer_ui()
            with ui.row().classes('items-stretch justify-items-stretch').style('flex-wrap:nowrap'):
                with ui.card():
                    with ui.row():
                        with ui.column():
                            self.robot_brain.developer_ui()
                        with ui.column():
                            self.robot_brain.communication.debug_ui()
                        with ui.column():
                            ui.markdown('**Hardware Manager**').classes('col-grow')
                            robot_status = ui.markdown()

                            ui.label('heap:').classes('col-grow').bind_text_from(self.test_brain, 'heap')
                            ui.switch(
                                'en3', value=True, on_change=self.test_brain.set_en3) \
                                    .bind_value_to(self.test_brain, 'en3')
                            ui.switch(
                                'rdyp', value=True, on_change=lambda e: self.test_brain.set_rdyp()) \
                                    .bind_value_to(self.test_brain, 'rdyp')
                            ui.button('Reset Lizard', on_click=self.robot_brain.restart)
                    ui.timer(1, lambda: robot_status \
                             .set_content(f'rdyp: {self.test_brain.rdyp_status}<br>vdp: {self.test_brain.vdp_status}'
                    ))
            with ui.row():
                with ui.card().style('min-width: 200px;'):
                    esp_pins_core = EspPins(name='core', robot_brain=self.robot_brain)
                    esp_pins_core.developer_ui()
                with ui.card().style('min-width: 200px;'):
                    esp_pins_p0 = EspPins(name='p0', robot_brain=self.robot_brain)
                    esp_pins_p0.developer_ui()
