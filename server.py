from websocket_server import WebsocketServer


def new_client(client, server):
    print(f"New client connected: {client['id']}")
    server.send_message_to_all(f"Client {client['id']} has joined the chat")


def client_left(client, server):
    print(f"Client disconnected: {client['id']}")
    server.send_message_to_all(f"Client {client['id']} has left the chat")


def message_received(client, server, message):
        parts = message.split(":", 1)
        if len(parts) != 2:
            raise ValueError("message")
        
        target_id = int(parts[0])
        client_msg = parts[1]

        target_client = next(c for c in server.clients if c['id'] == target_id)
        server.send_message(target_client, f"{client['id']}: {client_msg}")
    

server = WebsocketServer(host='0.0.0.0', port=12345)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
print("Server started.")
server.run_forever()
