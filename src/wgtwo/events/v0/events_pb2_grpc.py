# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from wgtwo.events.v0 import events_pb2 as wgtwo_dot_events_dot_v0_dot_events__pb2


class EventsServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Subscribe = channel.unary_stream(
                '/wgtwo.events.v0.EventsService/Subscribe',
                request_serializer=wgtwo_dot_events_dot_v0_dot_events__pb2.SubscribeEventsRequest.SerializeToString,
                response_deserializer=wgtwo_dot_events_dot_v0_dot_events__pb2.SubscribeEventsResponse.FromString,
                )
        self.Ack = channel.unary_unary(
                '/wgtwo.events.v0.EventsService/Ack',
                request_serializer=wgtwo_dot_events_dot_v0_dot_events__pb2.AckRequest.SerializeToString,
                response_deserializer=wgtwo_dot_events_dot_v0_dot_events__pb2.AckResponse.FromString,
                )


class EventsServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Subscribe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Ack(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EventsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Subscribe': grpc.unary_stream_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=wgtwo_dot_events_dot_v0_dot_events__pb2.SubscribeEventsRequest.FromString,
                    response_serializer=wgtwo_dot_events_dot_v0_dot_events__pb2.SubscribeEventsResponse.SerializeToString,
            ),
            'Ack': grpc.unary_unary_rpc_method_handler(
                    servicer.Ack,
                    request_deserializer=wgtwo_dot_events_dot_v0_dot_events__pb2.AckRequest.FromString,
                    response_serializer=wgtwo_dot_events_dot_v0_dot_events__pb2.AckResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'wgtwo.events.v0.EventsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EventsService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/wgtwo.events.v0.EventsService/Subscribe',
            wgtwo_dot_events_dot_v0_dot_events__pb2.SubscribeEventsRequest.SerializeToString,
            wgtwo_dot_events_dot_v0_dot_events__pb2.SubscribeEventsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Ack(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wgtwo.events.v0.EventsService/Ack',
            wgtwo_dot_events_dot_v0_dot_events__pb2.AckRequest.SerializeToString,
            wgtwo_dot_events_dot_v0_dot_events__pb2.AckResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
