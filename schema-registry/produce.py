from confluent_kafka import SerializingProducer
from confluent_kafka.schema_registry.avro import AvroSerializer
from confluent_kafka.schema_registry import SchemaRegistryClient
from pathlib import Path

"""
Topic: orders
Event structure:
{"order_id": "123", "amount": 10.0, "status": "PAID", "edd": "2024-12-31"}
==> after serialization
iuergfjheqg
"""

schema_path = Path(__file__).parent / "order.avsc"
with open(schema_path) as f:
    schema_str = f.read()

schema_registry = SchemaRegistryClient({"url": "http://localhost:8082"})
avro_serializer = AvroSerializer(schema_registry, schema_str)

p = SerializingProducer({
    "bootstrap.servers": "localhost:9092",
    "value.serializer": avro_serializer
})

p.produce("orders", value={"order_id": "123", "amount": 10.0, "status": "PAID", "edd": "2024-12-31"})
p.produce("orders", value={"order_id": "124", "amount": 12.0, "status": "UNPAID", "edd": "2024-12-31"})
p.flush()
