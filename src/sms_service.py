from wgtwo.sms.v0 import sms_pb2_grpc, sms_pb2
from wgtwo.common.v0.phonenumber_pb2 import PhoneNumber, TextAddress
import grpc


def send_grpc_sms(number: str, token: str):
    # print("token is ",token)
    call = grpc.access_token_call_credentials(token)
    channel = grpc.ssl_channel_credentials()
    combined = grpc.composite_channel_credentials(channel, call)
    channel = grpc.secure_channel('api.wgtwo.com:443', combined)

    stub = sms_pb2_grpc.SmsServiceStub(channel)

    def sendWithText(text):
        x = stub.SendTextToSubscriber(
            sms_pb2.SendTextToSubscriberRequest(
                content=text,
                from_text_address=TextAddress(textAddress='Dumbphone C'),
                to_subscriber=PhoneNumber(e164=number)))
        print(x)

    return sendWithText
    # mainMenu('', sendWithText)
