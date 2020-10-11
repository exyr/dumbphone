function generate-python {
    python3 -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. wgtwo/**/*.proto
}

function curl {
    grpcurl \
        -H "Authorization: Basic <base64token>"\
        -import-path . \
        -proto wgtwo/sms/v0/sms.proto \
        api.wgtwo.com:443 \
        wgtwo.sms.v0.SmsService/ReceiveText
}
