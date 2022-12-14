#!/usr/bin/env python3
import os

import rosys
from nicegui import ui

import log
import modules

log = log.configure()

rosys.hardware.SerialCommunication.search_paths.insert(0, '/dev/ttyTHS0')
is_real = rosys.hardware.SerialCommunication.is_possible()
if is_real:
    communication = rosys.hardware.SerialCommunication()
    robot_brain = rosys.hardware.RobotBrain(communication)
    if communication.device_path == '/dev/ttyTHS0':
        robot_brain.lizard_firmware.flash_params = ['xavier']
    robot = rosys.hardware.WheelsHardware(robot_brain)

test_brain_modules = {
    'Socket 1': 'rs485',
    'Socket 2': 'oogiir',
    'Socket 3': 'can',
    'Socket 4': 'oogoor',
    'Socket 5': 'None',
    'Socket 6': 'bumper'
}
available_modules = ['none', 'rs485', 'bumper', 'can', 'oogiir', 'oogoor']


@ui.page('/', shared=True)
async def index():
    async def start_test():
        ui.notify('Test started')
    # ui
    ui.colors(primary='#6E93D6', secondary='#53B689', accent='#111B1E', positive='#53B689')

    # navigation bar
    with ui.header().props('elevated').classes('q-pa-xs q-pt-sm', remove='q-pa-md items-start gap-4'):
        ui.label('Test Brain').classes(
            'text-white text-weight-bold col-5 q-pl-md')
        with ui.row().classes('col-7 justify-end q-pr-md'):
            if is_real:
                ui.icon('hardware').classes('text-white')
                ui.label('Hardware').classes('text-white')
            else:
                ui.icon('computer').classes('text-white')
                ui.label('Simulation').classes('text-white')
            with ui.row():
                with ui.menu() as menu:
                    ui.menu_item('Rosys Neustarten', on_click=lambda: os.utime('main.py'))
                ui.button(on_click=menu.open).classes('text-white').props('icon=settings size=sm dense unelevated flat')

    with ui.column().classes('w-full no-wrap items-stretch q-px-md'):
        with ui.row().classes('items-stretch justify-items-stretch').style('flex-wrap:nowrap'):

            # Module selection
            with ui.card():
                with ui.column():
                    test_brain = ui.radio(['Test Brain', 'To be tested'], value='Test Brain',
                                          on_change=lambda e: ui.notify(e.value)).props('inline')
                    for key, value in test_brain_modules.items():
                        with ui.row().bind_visibility_from(test_brain, 'value', value='Test Brain'):
                            ui.markdown(f'###### {key}')
                            ui.select(
                                [value], value=f'{value}',
                                on_change=lambda e: ui.notify(e.value)
                            )

            rs485 = modules.Rs485(1, robot_brain)
            oogiir = modules.Oogiir(2, robot_brain)
            can = modules.Can(3, robot_brain)
            oogoor = modules.Oogoor(4, robot_brain)
            bumper = modules.Bumper(6, robot_brain)

        with ui.row().classes('items-stretch justify-items-stretch').style('flex-wrap:nowrap'):
            with ui.card():
                if is_real:
                    with ui.row():
                        with ui.column():
                            robot.robot_brain.developer_ui()
                        with ui.column():
                            robot.robot_brain.communication.debug_ui()

ui.run(title='Test Brain', port=80 if is_real else 8080)
