#!/usr/bin/python3
from datetime import datetime
import csv
import requests
from pyngsi.ngsi import DataModel
from pyngsi.sink import SinkOrion, SinkStdout
from pyngsi.agent import NgsiAgent
from pyngsi.sources.more_sources import SourceSampleOrion

# URI = "jp.nagoya-u.mdg.gifu.takayama.congestion.dev001"
URI = "jp.gifu.takayama.flow.crowd.00001"
TYPE = "CrowdFlowObserved"
ORION_HOST = "localhost"
ORION_SECURE = False
ORION_SERVICE = "mdg"
ORION_SERVICEPATH = "/gifu/takayama"
AUTH_TOKEN = "0c8cb25d993d7891bd2d62e0528d540647fd4150"

sink = SinkOrion(
    hostname=ORION_HOST,
    port="3000",
    secure=ORION_SECURE,
    baseurl='/',
    post_endpoint='/v2/entities',
    post_query='options=upsert',
    status_endpoint='/version',
    useragent='NgsiAgent v2.1.7',
    proxy=None,
    token=AUTH_TOKEN,
    service=ORION_SERVICE,
    servicepath=ORION_SERVICEPATH
)

peopleCount = 30
dateObserved = datetime.utcnow()

m = DataModel(id=URI, type=TYPE)
m.add("dateObserved", dateObserved)
m.add("peopleCount", peopleCount)

sink.write(m.json())