# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from wgtwo.mms.v0 import mms_pb2 as wgtwo_dot_mms_dot_v0_dot_mms__pb2


class MmsServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendMessageToSubscriber = channel.unary_unary(
                '/wgtwo.mms.v0.MmsService/SendMessageToSubscriber',
                request_serializer=wgtwo_dot_mms_dot_v0_dot_mms__pb2.SendMessageToSubscriberRequest.SerializeToString,
                response_deserializer=wgtwo_dot_mms_dot_v0_dot_mms__pb2.SendResponse.FromString,
                )
        self.SendMessageFromSubscriber = channel.unary_unary(
                '/wgtwo.mms.v0.MmsService/SendMessageFromSubscriber',
                request_serializer=wgtwo_dot_mms_dot_v0_dot_mms__pb2.SendMessageFromSubscriberRequest.SerializeToString,
                response_deserializer=wgtwo_dot_mms_dot_v0_dot_mms__pb2.SendResponse.FromString,
                )


class MmsServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendMessageToSubscriber(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendMessageFromSubscriber(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MmsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendMessageToSubscriber': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMessageToSubscriber,
                    request_deserializer=wgtwo_dot_mms_dot_v0_dot_mms__pb2.SendMessageToSubscriberRequest.FromString,
                    response_serializer=wgtwo_dot_mms_dot_v0_dot_mms__pb2.SendResponse.SerializeToString,
            ),
            'SendMessageFromSubscriber': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMessageFromSubscriber,
                    request_deserializer=wgtwo_dot_mms_dot_v0_dot_mms__pb2.SendMessageFromSubscriberRequest.FromString,
                    response_serializer=wgtwo_dot_mms_dot_v0_dot_mms__pb2.SendResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'wgtwo.mms.v0.MmsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MmsService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendMessageToSubscriber(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wgtwo.mms.v0.MmsService/SendMessageToSubscriber',
            wgtwo_dot_mms_dot_v0_dot_mms__pb2.SendMessageToSubscriberRequest.SerializeToString,
            wgtwo_dot_mms_dot_v0_dot_mms__pb2.SendResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendMessageFromSubscriber(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wgtwo.mms.v0.MmsService/SendMessageFromSubscriber',
            wgtwo_dot_mms_dot_v0_dot_mms__pb2.SendMessageFromSubscriberRequest.SerializeToString,
            wgtwo_dot_mms_dot_v0_dot_mms__pb2.SendResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
