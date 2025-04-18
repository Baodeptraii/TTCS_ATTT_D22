import socket
import hashlib

def start_server():
    print("Server started")  # Indicate that the server has started
    
    host = socket.gethostname()  # Get the local machine name
    port = 17202
    server_socket = socket.socket()
    server_socket.bind((host, port))  # Bind to the port
    server_socket.listen(1)  # Listen for incoming connections
    conn, addr = server_socket.accept()  # Accept a connection
    
    key = "TruongQuocBao-B22DCAT034"  # Define a key for the server
    
    data = conn.recv(1024).decode()  # Receive data from the client
    tmp_data = conn.recv(1024).decode()  # Receive the hashed data from the client
    
    print("Received from client:", data)  # Print the received data
    print("Received hashed data:", tmp_data)  # Print the received hashed data
    
    hashed_data = hashlib.sha256(data.encode("utf-8") + key.encode("utf-8")).hexdigest()  # Hash the data with the key
    message = "Encrypted Successfully B22DCAT034!!! "
    
    print("Sending to client:", message)  # Print the data being sent
    print("Hashed Data:", hashed_data)  # Print the hashed data
    
    if tmp_data != hashed_data:
        message = "“The received message has lost its integrity.”"
    
    conn.send(message.encode())  # Send the response to the client
    conn.close()  # Close the connection
    
start_server()
    