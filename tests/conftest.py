# tests/conftest.py

import asyncio
import pytest


@pytest.yield_fixture
def loop():
    # Set-up
    aio_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(aio_loop)
    yield aio_loop

    # Clean-up
    aio_loop.close()
