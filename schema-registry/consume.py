from confluent_kafka.avro import AvroConsumer

consumer = AvroConsumer({
    "bootstrap.servers": "localhost:9092",
    "schema.registry.url": "http://localhost:8082",
    "group.id": "order-readers",
    "auto.offset.reset": "earliest"
})

consumer.subscribe(["orders"])

while True:
    msg = consumer.poll(1)
    if msg is None:
        continue
    print("Received:", msg.value())
