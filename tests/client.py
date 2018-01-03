import asyncio
import aiogrpc
import functools
import logging
#
from service_pb2 import StandardRequest, StreamRequest
from service_pb2_grpc import TestServiceStub
from server import create_server


logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.DEBUG,
    )

logger = logging.getLogger('aiogrpc.test.client')


loop = asyncio.get_event_loop()
channel = aiogrpc.insecure_channel('ipv4:///127.0.0.1:9901', loop=loop)
stub = TestServiceStub(channel)


def asynctest(f):
    @functools.wraps(f)
    def _test():
        return loop.run_until_complete(f())

    return _test


@asynctest
async def testUnaryUnary():
    logger.debug("")

    #
    result = await stub.NormalMethod(StandardRequest(name='test1'))
    logger.debug("result.message: {}".format(result.message))

    logger.debug("")

    #
    result, call = await stub.NormalMethod.with_call(StandardRequest(name='test2'))
    logger.debug("result.message: {}".format(result.message))
    logger.debug("await call.code(): {}".format(await call.code()))
    logger.debug("await call.details(): {}".format(await call.details()))
    logger.debug("call.is_active(): {}".format(call.is_active()))

    logger.debug("")

    #
    fut = stub.NormalMethod.future(StandardRequest(name='test3'))
    logger.debug("fut.is_active(): {}".format(fut.is_active()))
    logger.debug("fut.done(): {}".format(fut.is_active()))
    logger.debug("await fut.code(): {}".format(await fut.code()))
    logger.debug("(await fut).message: {}".format((await fut).message))
    logger.debug("fut.is_active(): {}".format(fut.is_active()))
    logger.debug("fut.done(): {}".format(fut.is_active()))


@asynctest
async def testCancel():
    logger.debug("")

    fut = stub.DelayedMethod.future(StandardRequest(name='test1'))
    logger.debug("fut.is_active(): {}".format(fut.is_active()))
    #
    fut.cancel()
    #
    logger.debug("await fut.code(): {}".format(await fut.code()))
    # self.assertEqual(await fut.code(), aiogrpc.StatusCode.CANCELLED)
    logger.debug("fut.done(): {}".format(fut.is_active()))


@asynctest
async def testUnaryStream():
    r = stub.StreamMethod(StreamRequest(name='test1', count=4))

    count = 0
    logger.debug("async for v in r: ...")
    async for v in r:
        # self.assertEqual(v.message, 'test1')
        logger.debug("\tv.message: {}".format(v.message))
        count += 1

    # self.assertEqual(count, 4)
    logger.debug("=> count: {}".format(count))
    # self.assertEqual(r.is_active(), False)
    logger.debug("r.is_active(): {}".format(r.is_active()))
    # self.assertEqual(await r.code(), aiogrpc.StatusCode.OK)
    logger.debug("await r.code(): {}".format(await r.code()))

    async with stub.StreamMethod.with_scope(StreamRequest(name='test1', count=4)) as r:
        count = 0
        async for v in r:
            # self.assertEqual(v.message, 'test1')
            logger.debug("v.message: {}".format(v.message))
            count += 1
            if count >= 2:
                break
    # self.assertEqual(await r.code(), aiogrpc.StatusCode.CANCELLED)
    logger.debug("await r.code(): {}".format(await r.code()))
    # self.assertEqual(r.is_active(), False)
    logger.debug("r.is_active(): {}".format(r.is_active()))

    # r = self.stub.StreamMethod(StreamRequest(name='test1', count=4), standalone_pool=True)
    # count = 0
    # async for v in r:
    #     self.assertEqual(v.message, 'test1')
    #     count += 1
    # self.assertEqual(count, 4)
    # self.assertEqual(r.is_active(), False)
    # self.assertEqual(await r.code(), aiogrpc.StatusCode.OK)
    # async with self.stub.StreamMethod.with_scope(StreamRequest(name='test1', count=4), standalone_pool=True) as r:
    #     count = 0
    #     async for v in r:
    #         self.assertEqual(v.message, 'test1')
    #         count += 1
    #         if count >= 2:
    #             break
    # self.assertEqual(await r.code(), aiogrpc.StatusCode.CANCELLED)
    # self.assertEqual(r.is_active(), False)


def main():
    testUnaryUnary()
    #
    testCancel()
    #
    testUnaryStream()


if __name__ == '__main__':
    s = create_server(['127.0.0.1:9901'])
    s.start()

    try:
        main()
    finally:
        waiter = s.stop(None)
        waiter.wait()
