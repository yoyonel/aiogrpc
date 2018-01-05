# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import service_pb2 as service__pb2


class TestServiceStub(object):
  """Test service
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.NormalMethod = channel.unary_unary(
        '/TestService/NormalMethod',
        request_serializer=service__pb2.StandardRequest.SerializeToString,
        response_deserializer=service__pb2.StandardReply.FromString,
        )
    self.StreamMethod = channel.unary_stream(
        '/TestService/StreamMethod',
        request_serializer=service__pb2.StreamRequest.SerializeToString,
        response_deserializer=service__pb2.StandardReply.FromString,
        )
    self.StreamInputMethod = channel.stream_unary(
        '/TestService/StreamInputMethod',
        request_serializer=service__pb2.StandardRequest.SerializeToString,
        response_deserializer=service__pb2.StreamReply.FromString,
        )
    self.StreamStreamMethod = channel.stream_stream(
        '/TestService/StreamStreamMethod',
        request_serializer=service__pb2.StandardRequest.SerializeToString,
        response_deserializer=service__pb2.StandardReply.FromString,
        )
    self.DelayedMethod = channel.unary_unary(
        '/TestService/DelayedMethod',
        request_serializer=service__pb2.StandardRequest.SerializeToString,
        response_deserializer=service__pb2.StandardReply.FromString,
        )
    self.ExceptionMethod = channel.unary_unary(
        '/TestService/ExceptionMethod',
        request_serializer=service__pb2.StandardRequest.SerializeToString,
        response_deserializer=service__pb2.StandardReply.FromString,
        )
    self.DelayedStream = channel.unary_stream(
        '/TestService/DelayedStream',
        request_serializer=service__pb2.StreamRequest.SerializeToString,
        response_deserializer=service__pb2.StandardReply.FromString,
        )


class TestServiceServicer(object):
  """Test service
  """

  def NormalMethod(self, request, context):
    """UnaryUnary
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamMethod(self, request, context):
    """UnaryStream
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamInputMethod(self, request_iterator, context):
    """StreamUnary
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamStreamMethod(self, request_iterator, context):
    """StreamStream
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DelayedMethod(self, request, context):
    """Delayed
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ExceptionMethod(self, request, context):
    """Exception
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DelayedStream(self, request, context):
    """Delayed Stream
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TestServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'NormalMethod': grpc.unary_unary_rpc_method_handler(
          servicer.NormalMethod,
          request_deserializer=service__pb2.StandardRequest.FromString,
          response_serializer=service__pb2.StandardReply.SerializeToString,
      ),
      'StreamMethod': grpc.unary_stream_rpc_method_handler(
          servicer.StreamMethod,
          request_deserializer=service__pb2.StreamRequest.FromString,
          response_serializer=service__pb2.StandardReply.SerializeToString,
      ),
      'StreamInputMethod': grpc.stream_unary_rpc_method_handler(
          servicer.StreamInputMethod,
          request_deserializer=service__pb2.StandardRequest.FromString,
          response_serializer=service__pb2.StreamReply.SerializeToString,
      ),
      'StreamStreamMethod': grpc.stream_stream_rpc_method_handler(
          servicer.StreamStreamMethod,
          request_deserializer=service__pb2.StandardRequest.FromString,
          response_serializer=service__pb2.StandardReply.SerializeToString,
      ),
      'DelayedMethod': grpc.unary_unary_rpc_method_handler(
          servicer.DelayedMethod,
          request_deserializer=service__pb2.StandardRequest.FromString,
          response_serializer=service__pb2.StandardReply.SerializeToString,
      ),
      'ExceptionMethod': grpc.unary_unary_rpc_method_handler(
          servicer.ExceptionMethod,
          request_deserializer=service__pb2.StandardRequest.FromString,
          response_serializer=service__pb2.StandardReply.SerializeToString,
      ),
      'DelayedStream': grpc.unary_stream_rpc_method_handler(
          servicer.DelayedStream,
          request_deserializer=service__pb2.StreamRequest.FromString,
          response_serializer=service__pb2.StandardReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'TestService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
