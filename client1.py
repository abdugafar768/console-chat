import websocket
import threading

def on_message(ws, message):
    print(f"Received message: {message}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws):
    print("Connection closed")

def on_open(ws):
    print("Connection opened")

    def send_message():
        target_id = input('Who do you want to send a message to (ID)? : ')
        while True:
            message = input('Message: ')
            ws.send(f"{target_id}:{message}")

    threading.Thread(target=send_message, daemon=True).start()

if __name__ == "__main__":
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp("ws://localhost:12345/",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
