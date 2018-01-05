# tests/test_coros.py
import asyncio


def test_coro(loop):
    @asyncio.coroutine
    def do_test():
        yield from asyncio.sleep(0.1, loop=loop)
        assert 0  # onoes!

    loop.run_until_complete(do_test())
