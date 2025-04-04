import logging

import rosys
from nicegui import ui
from rosys.helpers import remove_indentation

from .module import Module


class Bumper(Module):
    def __init__(self, *,
                 robot_brain: rosys.hardware.RobotBrain,
                 socket: int,
                 pin1: int, pin1_on_expander: bool = False,
                 pin2: int, pin2_on_expander: bool = False,
                 pin3: int, pin3_on_expander: bool = False,
                 pin4: int, pin4_on_expander: bool = False) -> None:
        super().__init__(robot_brain=robot_brain,
                         socket=socket,
                         pin1=pin1, pin1_on_expander=pin1_on_expander,
                         pin2=pin2, pin2_on_expander=pin2_on_expander,
                         pin3=pin3, pin3_on_expander=pin3_on_expander,
                         pin4=pin4, pin4_on_expander=pin4_on_expander)
        self.in_1_status = False
        self.in_2_status = False
        self.in_3_status = False
        self.in_4_status = False
        self.log = logging.getLogger('test_brain.bumper_v02')
        self.lizard_code = remove_indentation(
        f'''
        s{self.socket}_in_1 = {"p0." if self.pin1_on_expander else ""}Input({self.pin1})
        s{self.socket}_in_2 = {"p0." if self.pin2_on_expander else ""}Input({self.pin2})
        s{self.socket}_in_3 = {"p0." if self.pin3_on_expander else ""}Input({self.pin3})
        s{self.socket}_in_4 = {"p0." if self.pin4_on_expander else ""}Input({self.pin4})
        ''')
        self.core_message_fields = [
            f's{self.socket}_in_1.level',
            f's{self.socket}_in_2.level',
            f's{self.socket}_in_3.level',
            f's{self.socket}_in_4.level']

    def developer_ui(self):
        with ui.card():
            ui.label(f'Socket {self.socket}: Bumper').classes('text-bold')
            with ui.column():
                with ui.row():
                    ui.label('in_1 pin')
                    ui.icon('highlight_off').classes('text-red') \
                        .bind_visibility_from(self, 'in_1_status', backward=lambda x: not x)
                    ui.icon('check_circle_outline').classes(
                            'text-green').bind_visibility_from(self, 'in_1_status')
                with ui.row():
                    ui.label('in_2 pin')
                    ui.icon('highlight_off').classes('text-red') \
                        .bind_visibility_from(self, 'in_2_status', backward=lambda x: not x)
                    ui.icon('check_circle_outline').classes(
                        'text-green').bind_visibility_from(self, 'in_2_status')
                with ui.row():
                    ui.label('in_3 pin')
                    ui.icon('highlight_off').classes('text-red') \
                        .bind_visibility_from(self, 'in_3_status', backward=lambda x: not x)
                    ui.icon('check_circle_outline').classes(
                        'text-green').bind_visibility_from(self, 'in_3_status')
                with ui.row():
                    ui.label('in_4 pin')
                    ui.icon('highlight_off').classes('text-red') \
                        .bind_visibility_from(self, 'in_4_status', backward=lambda x: not x)
                    ui.icon('check_circle_outline').classes(
                        'text-green').bind_visibility_from(self, 'in_4_status')

    def handle_core_output(self,words:list[str]):
        self.in_1_status = int(words.pop(0)) == 1
        self.in_2_status = int(words.pop(0)) == 1
        self.in_3_status = int(words.pop(0)) == 1
        self.in_4_status = int(words.pop(0)) == 1


class BumperV02(Bumper):
    ...

class BumperV03(Bumper):
    ...
