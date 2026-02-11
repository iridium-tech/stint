import time
from datetime import datetime
from typing import TYPE_CHECKING

import psutil
from google.protobuf.timestamp_pb2 import Timestamp  # ty:ignore[unresolved-import]
from starlette.middleware.cors import CORSMiddleware

from api.flight.v1.flight_connect import FlightService, FlightServiceASGIApplication
from api.flight.v1.flight_pb2 import ProbeRequest, ProbeResponse

if TYPE_CHECKING:
    from google.protobuf.internal.well_known_types import Timestamp


class Flight(FlightService):
    def _now(self) -> Timestamp:
        ts = Timestamp()
        ts.FromDatetime(datetime.now())
        return ts

    async def probe(self, request: ProbeRequest, ctx) -> ProbeResponse:
        return ProbeResponse(
            client_sent_at=request.client_sent_at,
            server_processed_at=self._now(),
            cpu_percent=psutil.cpu_percent(interval=None),
            memory_percent=psutil.virtual_memory().percent,
            uptime_seconds=int(time.time() - psutil.boot_time()),
        )


connect_app = FlightServiceASGIApplication(Flight())

app = CORSMiddleware(
    connect_app,
    allow_origins=["http://localhost:3000"],
    allow_methods=["POST"],
    allow_headers=[
        "content-type",
        "connect-protocol-version",
        "connect-timeout-ms",
        "connect-accept-encoding",
        "connect-content-encoding",
        "x-user-agent",
    ],
    allow_credentials=True,
)
