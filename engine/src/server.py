from datetime import datetime

from asgi_cors import asgi_cors
from flight.v1.flight_connect import FlightService, FlightServiceASGIApplication
from flight.v1.flight_pb2 import FlightEventRequest, FlightEventResponse


class Flight(FlightService):
    async def flight_event(self, request: FlightEventRequest, ctx):
        print(request.message)
        now = datetime.now()
        response = FlightEventResponse(
            acknowledgment="Python said: my final message, goodbye.", received_at=now
        )
        return response


app = asgi_cors(
    FlightServiceASGIApplication(Flight()),
    hosts=["http://localhost:4000"],
    methods=["GET", "POST"],
    headers=[
        "content-type",
        "connect-protocol-version",
        "connect-timeout-ms",
        "x-user-agent",
    ],
)
