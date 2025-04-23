def process_message(message):
    print(f"Parsing message {message}", message)
    cleaned = {
        "text": message["text"],
        "user": message["user"],
        "tags": ["projekt"] if "projekt" in message["text"].lower() else [],
        "platform": message["platform"],
        "channel": message["channel"]
    }
    print(f"Cleaned message:, {cleaned}", cleaned)
    return cleaned
