import random


class TelemetryClient(object):
    ''' 
    The communication with the server is simulated in this implementation.
    Because the focus of the exercise is on the other class.
    '''
    DIAGNOSTIC_MESSAGE = "AT#UD"

    def __init__(self) -> None:
        self._online_status = False
        self._diagnosticMessageJustSent = False

    @property
    def online_status(self) -> bool:
        return self._online_status

    def connect(self, telemetry_server_connection_string: str) -> None:
        if (telemetry_server_connection_string is None or telemetry_server_connection_string == ""):
            raise Exception()
        success = random.randint(1, 10) <= 2
        self._online_status = success

    def disconnect(self) -> None:
        self._online_status = False

    def send(self, message: str) -> None:
        if (message is None or message == ""):
            raise Exception()
        if (message == TelemetryClient.DIAGNOSTIC_MESSAGE):
            self._diagnosticMessageJustSent = True
        else:
            self._diagnosticMessageJustSent = False

    def receive(self) -> str:
        if (self._diagnosticMessageJustSent):
            with open('message.txt') as file:
                message = "\n".join(file.readlines())
            self._diagnosticMessageJustSent = False
        else:
            message = ""
            messageLength = random.randint(0, 50) + 60
            i = messageLength
            while (i >= 0):
                message += chr((random.randint(0, 40) + 86))
                i -= 1
        return message
