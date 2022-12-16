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
    robot_brain = rosys.hardware.RobotBrain(communication)
    hardware_manager = HardwareManager(robot_brain)
    if communication.device_path == '/dev/ttyTHS0':
        robot_brain.lizard_firmware.flash_params = ['xavier']


tester_brain_modules = {
    '1': 'rs485',
    '2': 'oogiir',
    '3': 'can',
    '4': 'oogoor',
    '5': 'none',
    '6': 'bumper'
}
tested_brain_modules = {
    '1': 'none',
    '2': 'none',
    '3': 'none',
    '4': 'none',
    '5': 'none',
    '6': 'none'
}
available_modules = ['none', 'rs485', 'bumper', 'can', 'oogiir', 'oogoor']


@ui.page('/', shared=True)
async def index():

    def update_modules(value, key):
        tested_brain_modules[key] = value
        ui.notify(f'Socket {key} changed to {value}')

    def set_modules():
        module_row.clear()
        if test_brain_type.value != 'Tester':
            with module_row:
                for key, value in tested_brain_modules.items():
                    if value != 'none':
                        if value == 'rs485':
                            rs485_test = modules.Rs485(int(key), robot_brain)
                            hardware_manager.sockets[key] = rs485_test
                        if value == 'oogiir':
                            oogiir_test = modules.Oogiir(int(key), robot_brain)
                            hardware_manager.sockets[key] = oogiir_test
                        if value == 'oogoor':
                            oogoor_test = modules.Oogoor(int(key), robot_brain)
                            hardware_manager.sockets[key] = oogoor_test
                        if value == 'can':
                            can_test = modules.Can(int(key), robot_brain)
                            hardware_manager.sockets[key] = can_test
                        if value == 'bumper':
                            bumper_test = modules.Bumper(int(key), robot_brain)
                            hardware_manager.sockets[key] = bumper_test
                    else:
                        hardware_manager.sockets[key] = None
        else:
            with module_row:
                rs485_tester = modules.Rs485(1, robot_brain, rx=26, rx_p0=True, tx=27, tx_p0=True,
                                             out_1=13, out_1_p0=True, in_1=15, in_1_p0=True)
                oogiir_tester = modules.Oogiir(2, robot_brain, out_1=5, out_2=4, in_1=36, in_2=13)
                can_tester = modules.Can(3, robot_brain, rx=32, tx=33, out_1=2, out_1_p0=True, in_1=14, in_1_p0=True)
                oogoor_tester = modules.Oogoor(4, robot_brain, out_1=33, out_1_p0=True, out_2=4,
                                               out_2_p0=True, out_3=32, out_3_p0=True, out_4=5, out_4_p0=True)
                bumper_tester = modules.Bumper(6, robot_brain, in_1=12, in_1_p0=True, in_2=25,
                                               in_2_p0=True, in_3=22, in_3_p0=True, in_4=23, in_4_p0=True)
            hardware_manager.sockets = {
                '1': rs485_tester,
                '2': oogiir_tester,
                '3': can_tester,
                '4': oogoor_tester,
                '5': None,
                '6': bumper_tester
            }
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
                        test_brain_type = ui.radio(['Tester', 'To be tested'], value='Tester',
                                                   on_change=lambda e: ui.notify(e.value)).props('inline')
                        ui.button('Set Modules', on_click=set_modules)

                    # fix selection for TesteR Brain
                    with ui.row().bind_visibility_from(test_brain_type, 'value', value='Tester'):
                        for key, value in tester_brain_modules.items():
                            with ui.column():
                                ui.markdown(f'###### Socket {key}')
                                ui.select(
                                    [value], label=f'{key}', value=f'{value}',
                                    on_change=lambda e: ui.notify(e.value)
                                )

                    # selection for TesteD brain
                    with ui.row().bind_visibility_from(test_brain_type, 'value', value='To be tested'):
                        with ui.column():
                            ui.markdown(f'###### Socket 1')
                            select_socket1 = ui.select(
                                available_modules, value=f'none',
                                on_change=lambda: update_modules(select_socket1.value, '1')
                            )
                        with ui.column():
                            ui.markdown(f'###### Socket 2')
                            select_socket2 = ui.select(
                                available_modules, value=f'none',
                                on_change=lambda: update_modules(select_socket2.value, '2')
                            )
                        with ui.column():
                            ui.markdown(f'###### Socket 3')
                            select_socket3 = ui.select(
                                available_modules, value=f'none',
                                on_change=lambda: update_modules(select_socket3.value, '3')
                            )
                        with ui.column():
                            ui.markdown(f'###### Socket 4')
                            select_socket4 = ui.select(
                                available_modules, value=f'none',
                                on_change=lambda: update_modules(select_socket4.value, '4')
                            )
                        with ui.column():
                            ui.markdown(f'###### Socket 5')
                            select_socket5 = ui.select(
                                available_modules, value=f'none',
                                on_change=lambda: update_modules(select_socket5.value, '5')
                            )
                        with ui.column():
                            ui.markdown(f'###### Socket 6')
                            select_socket6 = ui.select(
                                available_modules, value=f'none',
                                on_change=lambda: update_modules(select_socket6.value, '6')
                            )

        # pin Selection for TesteD Brain
        with ui.row() as module_row:
            set_modules()

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
                            ui.markdown(f'**Hardware Manager of "{test_brain_type.value}"**').classes('col-grow')
                            robot_status = ui.markdown()
                    ui.timer(1, lambda: robot_status.set_content(
                        f'Empty Sockets:{hardware_manager.sockets}\
                            <br>rdyp: {hardware_manager.rdyp_status}<br>vdp: {hardware_manager.vdp_status}'
                    ))

ui.run(title='Test Brain', port=80 if is_real else 8080)
