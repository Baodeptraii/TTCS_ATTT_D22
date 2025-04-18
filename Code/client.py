import socket 
import hashlib

def start_client():
    print("Client started")  # Indicate that the client has started
    
    host = socket.gethostname()  # Get the local machine name
    port = 17202  # Port to connect to
    client_socket = socket.socket()  # Create a socket object
    client_socket.connect((host, port))  # Connect to the server
    
    key = "TruongQuocBao-B22DCAT034-123"  # Define a key for the server
    message = "Hello, I'm B22DCAT034 client!"  # Message to send to the server
    hashed_message = hashlib.sha256(message.encode("utf-8") + key.encode("utf-8")).hexdigest()  # Hash the message with the key

    print("Sending to server:", message)  # Print the data being sent
    client_socket.send(message.encode())  # Send data to the server
    
    print("Hashed Message:", hashed_message)  # Print the hashed message
    client_socket.send(hashed_message.encode())  # Send the hashed message to the server

    data = client_socket.recv(1024).decode()  # Receive response from the server
    print("Received from server:", data)  # Print the received response

    client_socket.close()  # Close the connection

    
start_client()