#!/usr/bin/env python3
import os

import rosys
from nicegui import ui

import log
import modules
from hardware import HardwareManager

log = log.configure()

rosys.hardware.SerialCommunication.search_paths.insert(0, '/dev/ttyTHS0')
is_real = rosys.hardware.SerialCommunication.is_possible()
if is_real:
    communication = rosys.hardware.SerialCommunication()
    robot_brain = rosys.hardware.RobotBrain(communication, lizard_startup='hardware/startup_rb14.liz')
    hardware_manager = HardwareManager(robot_brain)
    if communication.device_path == '/dev/ttyTHS0':
        robot_brain.lizard_firmware.flash_params = ['xavier']


@ui.page('/', shared=True)
async def index():

    async def set_modules():
        module_row.clear()
        with module_row:
            await hardware_manager.set_sockets()

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

            # module selection
            with ui.card():
                with ui.row():
                    with ui.column():
                        ui.button('Get Modules', on_click=set_modules)

        # pin Selection for TesteD Brain
        with ui.row() as module_row:
            ui.label('Get Modules with the button above')

        # development tools
        with ui.row().classes('items-stretch justify-items-stretch').style('flex-wrap:nowrap'):
            with ui.card():
                if is_real:
                    with ui.row():
                        with ui.column():
                            robot_brain.developer_ui()
                        with ui.column():
                            robot_brain.communication.debug_ui()
                        with ui.column():
                            ui.markdown(f'**Hardware Manager**').classes('col-grow')
                            robot_status = ui.markdown()
                            ui.button('Reset Lizard', on_click=robot_brain.restart)
                    ui.timer(1, lambda: robot_status.set_content(
                        f'rdyp: {hardware_manager.rdyp_status}<br>vdp: {hardware_manager.vdp_status}'
                    ))

ui.run(title='Test Brain', port=80 if is_real else 8080)
