from confluent_kafka import Producer
import json
import sys
import random
from datetime import datetime, timedelta

"""
Topic: orders_noschema
Event structre:
{
    "order_id": order_id,
    "amount": amount,
    "status": status,
    "edd": edd
}
"""

# Get number of messages from command line argument, default to 10
n = int(sys.argv[1]) if len(sys.argv) > 1 else 5

p = Producer({
    "bootstrap.servers": "localhost:9092"
})

statuses = ["PAID", "PENDING", "SHIPPED", "DELIVERED", "CANCELLED"]

for i in range(n):
    order_id = str(random.randint(1000, 9999))
    amount = round(random.uniform(10.0, 1000.0), 2)
    status = random.choice(statuses)
    edd = (datetime.now() + timedelta(days=random.randint(1, 30))).strftime("%Y-%m-%d")
    
    value = {
        "order_id": order_id,
        "amount": amount,
        "status": status,
        "edd": edd
    }
    
    p.produce("orders_noschema", value=json.dumps(value).encode('utf-8'))
    print(f"Produced message {i+1}/{n}: {value}")

p.flush()
print(f"\nSuccessfully produced {n} messages")
