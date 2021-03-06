# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from wgtwo.voicemail.v0 import voicemail_pb2 as wgtwo_dot_voicemail_dot_v0_dot_voicemail__pb2


class VoicemailMediaServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAllVoicemailMetadata = channel.unary_unary(
                '/wgtwo.voicemail.v0.VoicemailMediaService/GetAllVoicemailMetadata',
                request_serializer=wgtwo_dot_voicemail_dot_v0_dot_voicemail__pb2.GetAllVoicemailMetadataRequest.SerializeToString,
                response_deserializer=wgtwo_dot_voicemail_dot_v0_dot_voicemail__pb2.GetAllVoicemailMetadataResponse.FromString,
                )
        self.GetVoicemail = channel.unary_unary(
                '/wgtwo.voicemail.v0.VoicemailMediaService/GetVoicemail',
                request_serializer=wgtwo_dot_voicemail_dot_v0_dot_voicemail__pb2.GetVoicemailRequest.SerializeToString,
                response_deserializer=wgtwo_dot_voicemail_dot_v0_dot_voicemail__pb2.GetVoicemailResponse.FromString,
                )
        self.MarkVoicemailAsRead = channel.unary_unary(
                '/wgtwo.voicemail.v0.VoicemailMediaService/MarkVoicemailAsRead',
                request_serializer=wgtwo_dot_voicemail_dot_v0_dot_voicemail__pb2.MarkVoicemailAsReadRequest.SerializeToString,
                response_deserializer=wgtwo_dot_voicemail_dot_v0_dot_voicemail__pb2.MarkVoicemailAsReadResponse.FromString,
                )
        self.DeleteVoicemail = channel.unary_unary(
                '/wgtwo.voicemail.v0.VoicemailMediaService/DeleteVoicemail',
                request_serializer=wgtwo_dot_voicemail_dot_v0_dot_voicemail__pb2.DeleteVoicemailRequest.SerializeToString,
                response_deserializer=wgtwo_dot_voicemail_dot_v0_dot_voicemail__pb2.DeleteVoicemailResponse.FromString,
                )


class VoicemailMediaServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAllVoicemailMetadata(self, request, context):
        """*
        Receive metadata for each voicemail available for a given MSISDN.
        The metadata contains information about the corresponding voicemail including its ID,
        allowing the user to fetch the voicemail media file.

        Client-side errors:
        - INVALID ARGUMENT: Invalid MSISDN
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVoicemail(self, request, context):
        """*
        Receive voicemail media file corresponding to the given voicemail ID.

        Client-side errors:
        - INVALID ARGUMENT: Invalid voicemail ID
        - NOT FOUND: Voicemail not found

        Server-side errors:
        - INTERNAL: Voicemail file is too big to be returned
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MarkVoicemailAsRead(self, request, context):
        """*
        Mark as read the voicemail corresponding to the given voicemail ID.
        This updates the "played" metadata of the voicemail to true.

        Client-side errors:
        - INVALID ARGUMENT: Invalid voicemail ID
        - NOT FOUND: Voicemail not found
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteVoicemail(self, request, context):
        """*
        Delete the voicemail corresponding to the given voicemail ID.
        The voicemail media file and its metadata will be deleted.

        Client-side errors:
        - INVALID ARGUMENT: Invalid voicemail ID
        - NOT FOUND: Voicemail not found
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VoicemailMediaServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAllVoicemailMetadata': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllVoicemailMetadata,
                    request_deserializer=wgtwo_dot_voicemail_dot_v0_dot_voicemail__pb2.GetAllVoicemailMetadataRequest.FromString,
                    response_serializer=wgtwo_dot_voicemail_dot_v0_dot_voicemail__pb2.GetAllVoicemailMetadataResponse.SerializeToString,
            ),
            'GetVoicemail': grpc.unary_unary_rpc_method_handler(
                    servicer.GetVoicemail,
                    request_deserializer=wgtwo_dot_voicemail_dot_v0_dot_voicemail__pb2.GetVoicemailRequest.FromString,
                    response_serializer=wgtwo_dot_voicemail_dot_v0_dot_voicemail__pb2.GetVoicemailResponse.SerializeToString,
            ),
            'MarkVoicemailAsRead': grpc.unary_unary_rpc_method_handler(
                    servicer.MarkVoicemailAsRead,
                    request_deserializer=wgtwo_dot_voicemail_dot_v0_dot_voicemail__pb2.MarkVoicemailAsReadRequest.FromString,
                    response_serializer=wgtwo_dot_voicemail_dot_v0_dot_voicemail__pb2.MarkVoicemailAsReadResponse.SerializeToString,
            ),
            'DeleteVoicemail': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteVoicemail,
                    request_deserializer=wgtwo_dot_voicemail_dot_v0_dot_voicemail__pb2.DeleteVoicemailRequest.FromString,
                    response_serializer=wgtwo_dot_voicemail_dot_v0_dot_voicemail__pb2.DeleteVoicemailResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'wgtwo.voicemail.v0.VoicemailMediaService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class VoicemailMediaService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetAllVoicemailMetadata(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wgtwo.voicemail.v0.VoicemailMediaService/GetAllVoicemailMetadata',
            wgtwo_dot_voicemail_dot_v0_dot_voicemail__pb2.GetAllVoicemailMetadataRequest.SerializeToString,
            wgtwo_dot_voicemail_dot_v0_dot_voicemail__pb2.GetAllVoicemailMetadataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetVoicemail(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wgtwo.voicemail.v0.VoicemailMediaService/GetVoicemail',
            wgtwo_dot_voicemail_dot_v0_dot_voicemail__pb2.GetVoicemailRequest.SerializeToString,
            wgtwo_dot_voicemail_dot_v0_dot_voicemail__pb2.GetVoicemailResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MarkVoicemailAsRead(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wgtwo.voicemail.v0.VoicemailMediaService/MarkVoicemailAsRead',
            wgtwo_dot_voicemail_dot_v0_dot_voicemail__pb2.MarkVoicemailAsReadRequest.SerializeToString,
            wgtwo_dot_voicemail_dot_v0_dot_voicemail__pb2.MarkVoicemailAsReadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteVoicemail(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wgtwo.voicemail.v0.VoicemailMediaService/DeleteVoicemail',
            wgtwo_dot_voicemail_dot_v0_dot_voicemail__pb2.DeleteVoicemailRequest.SerializeToString,
            wgtwo_dot_voicemail_dot_v0_dot_voicemail__pb2.DeleteVoicemailResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
