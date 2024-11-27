#!/usr/bin/env python3
import os

import rosys
from nicegui import app, ui
from rosys.hardware import EspPins

import log
from hardware import RobotBrains, TestBrain
from modules import *

log = log.configure()


async def startup() -> None:

    rosys.hardware.SerialCommunication.search_paths.insert(0, '/dev/ttyTHS0')
    is_real = rosys.hardware.SerialCommunication.is_possible()
    if is_real:
        communication = rosys.hardware.SerialCommunication()
        robot_brain = rosys.hardware.RobotBrain(communication)
        robot_brains = RobotBrains(robot_brain)
        test_brain = robot_brains.current_brain

    @ui.page('/')
    async def main_page():
        # ui
        ui.colors(primary='#6E93D6', secondary='#53B689', accent='#111B1E', positive='#53B689')

        # navigation bar
        with ui.header().props('elevated').classes('q-pa-xs q-pt-sm', remove='q-pa-md items-start gap-4') as header:

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
                    ui.button(on_click=menu.open).classes(
                        'text-white').props('icon=settings size=sm dense unelevated flat')

        # Main content area
        module_container = ui.column().classes('w-full')

        def update_module_ui():
            module_container.clear()
            print(f"Updating UI with {len(test_brain.modules)} modules")
            with module_container:
                with ui.row().classes('items-stretch justify-start').style('gap: 1rem; flex-wrap: wrap'):
                    if not test_brain.modules:
                        ui.label('No modules configured for this brain').classes('text-h6')
                    else:
                        for module in test_brain.modules:
                            print(f"Creating UI for module: {type(module).__name__}")
                            module.create_ui()

        def update_test_brain(new_brain_name):
            nonlocal test_brain
            brain_name = str(new_brain_name.value)
            print(f"Switching to brain: {brain_name}")
            test_brain = robot_brains.get_robot_brain(brain_name)
            print(f"New test_brain has {len(test_brain.modules)} modules")
            update_module_ui()

        with ui.column().classes('w-full no-wrap items-stretch q-px-md'):
            # Select element
            with ui.row().classes('items-stretch justify-items-stretch q-pb-md').style('flex-wrap:nowrap'):
                ui.select(robot_brains.get_robot_brain_list(), on_change=update_test_brain).bind_value(robot_brains, 'current_brain_name')

            # Initial update of module UI
            update_module_ui()

            # Development tools below modules
            with ui.row().classes('items-stretch justify-items-stretch').style('flex-wrap:nowrap'):
                with ui.card():
                    if is_real:
                        with ui.row():
                            with ui.column():
                                robot_brain.developer_ui()
                            with ui.column():
                                robot_brain.communication.debug_ui()
                            with ui.column():
                                ui.markdown('**Hardware Manager**').classes('col-grow')
                                robot_status = ui.markdown()

                                ui.label('heap:').classes('col-grow').bind_text_from(test_brain, 'heap')
                                ui.switch(
                                    'en3', value=True, on_change=test_brain.set_en3).bind_value_to(
                                    test_brain, 'en3')
                                ui.switch(
                                    'rdyp', value=True, on_change=test_brain.set_rdyp).bind_value_to(
                                    test_brain, 'rdyp')
                                ui.button('Reset Lizard', on_click=robot_brain.restart)
                        ui.timer(1, lambda: robot_status.set_content(
                            f'rdyp: {test_brain.rdyp_status}<br>vdp: {test_brain.vdp_status}'
                        ))
            with ui.row():
                with ui.card().style('min-width: 200px;'):
                    esp_pins_core = EspPins(name='core', robot_brain=robot_brain)
                    esp_pins_core.developer_ui()
                with ui.card().style('min-width: 200px;'):
                    esp_pins_p0 = EspPins(name='p0', robot_brain=robot_brain)
                    esp_pins_p0.developer_ui()


app.on_startup(startup)

ui.run(title='Test Brain', port=80)
