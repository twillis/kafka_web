import json
from pykafka import KafkaClient
import logging
log = logging.getLogger(__name__)

def serialize(data, key):
    return (json.dumps(data).encode('utf-8'), key)


client = KafkaClient(hosts="localhost:9092", broker_version='0.12.2')
producer = client.topics["test-topic"].get_producer(serializer=serialize)


def includeme(config):
    config.add_tween('.kafka.analytics_tween')


def analytics_tween(handler, registry):
    def analytics(request):
        response = handler(request)
        log.info("producing kafka message")
        producer.produce(dict(message="request received"))
        return response

    return analytics
