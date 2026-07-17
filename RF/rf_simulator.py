import random

DEVICES = [
    "WiFi",
    "Bluetooth",
    "ZigBee",
    "RF Remote",
    "Unknown"
]


def generate_signal(node_id):
    return {
        "node_id": node_id,
        "device": random.choice(DEVICES),
        "frequency": random.randint(2400, 2500),
        "rssi": random.randint(-90, -20)
    }


def generate_signals(count=10):

    signals = []

    for _ in range(count):
        node = random.randint(1, 3)
        signals.append(generate_signal(node))

    return signals