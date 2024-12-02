#!/usr/bin/env python3
import os

from dotenv import load_dotenv
from nicegui import app, ui

from test_brain import System, log_configuration

logger = log_configuration.configure()
load_dotenv('.env')
brain_id = os.getenv('BRAIN_ID')
assert brain_id is not None, 'BRAIN_ID is not set'

async def startup() -> None:
    system = System(brain_id)
    ui.colors(primary='#6E93D6', secondary='#53B689', accent='#111B1E', positive='#53B689')
    @ui.page('/')
    def page() -> None:
        system.developer_ui()

app.on_startup(startup)
ui.run(title='Test Brain', port=80)
