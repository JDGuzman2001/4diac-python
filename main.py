#!/usr/bin/env python3
import socket
import struct
import time
import logging
import binascii

class FORDIAC_Client:
    def __init__(self, host='localhost', port=61499):
        """Initialize the 4DIAC client connection.
        
        Args:
            host (str): The host address of the 4DIAC runtime (default: localhost)
            port (int): The port number (default: 61499 - standard 4DIAC port)
        """
        self.host = host
        self.port = port
        self.socket = None
        self.connected = False
        
        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def print_data_info(self, data, source=""):
        """Print detailed information about the data.
        
        Args:
            data: The data to analyze
            source (str): Description of where the data came from
        """
        print(f"\n{'='*50}")
        print(f"Data Analysis ({source}):")
        print(f"{'='*50}")
        
        print(f"Raw data: {data}")
        print(f"Type: {type(data)}")
        print(f"Length: {len(data)} bytes")
        
        # Hexadecimal representation
        print(f"\nHexadecimal: {binascii.hexlify(data).decode()}")
        
        # Try different decodings
        print("\nPossible text representations:")
        encodings = ['utf-8', 'ascii', 'iso-8859-1']
        for encoding in encodings:
            try:
                decoded = data.decode(encoding)
                print(f"{encoding}: {decoded}")
            except Exception as e:
                print(f"{encoding}: Unable to decode - {str(e)}")
        
        # Try to interpret as different number formats if the length matches
        print("\nPossible number interpretations:")
        if len(data) >= 4:
            try:
                # Try as 32-bit integer
                int_val = struct.unpack('!i', data[:4])[0]
                print(f"As 32-bit int: {int_val}")
            except:
                print("Not a valid 32-bit integer")
            
            try:
                # Try as float
                float_val = struct.unpack('!f', data[:4])[0]
                print(f"As float: {float_val}")
            except:
                print("Not a valid float")
        
        if len(data) >= 8:
            try:
                # Try as 64-bit double
                double_val = struct.unpack('!d', data[:8])[0]
                print(f"As double: {double_val}")
            except:
                print("Not a valid double")
        
        print(f"{'='*50}\n")

    def connect(self):
        """Establish connection to 4DIAC runtime."""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
            self.connected = True
            self.logger.info(f"Connected successfully to {self.host}:{self.port}")
            print(f"\n[+] Connected to 4DIAC at {self.host}:{self.port}")
            return True
        except socket.error as e:
            self.logger.error(f"Connection failed: {e}")
            print(f"\n[-] Connection failed: {e}")
            self.connected = False
            return False

    def disconnect(self):
        """Close the connection to 4DIAC runtime."""
        if self.socket and self.connected:
            self.socket.close()
            self.connected = False
            self.logger.info("Disconnected from 4DIAC runtime")
            print("\n[*] Disconnected from 4DIAC runtime")

    def send_data(self, data):
        """Send data to 4DIAC runtime.
        
        Args:
            data (bytes): Data to send
        """
        if not self.connected:
            self.logger.error("Not connected to 4DIAC runtime")
            print("\n[-] Error: Not connected to 4DIAC runtime")
            return False
        
        try:
            self.socket.sendall(data)
            self.logger.info(f"Sent data: {data}")
            print("\n[>] Sending data:")
            self.print_data_info(data, "Sent")
            return True
        except socket.error as e:
            self.logger.error(f"Error sending data: {e}")
            print(f"\n[-] Error sending data: {e}")
            return False

    def receive_data(self, buffer_size=1024):
        """Receive data from 4DIAC runtime.
        
        Args:
            buffer_size (int): Size of the receive buffer
            
        Returns:
            bytes: Received data
        """
        if not self.connected:
            self.logger.error("Not connected to 4DIAC runtime")
            print("\n[-] Error: Not connected to 4DIAC runtime")
            return None
        
        try:
            print("\n[*] Waiting for data...")
            data = self.socket.recv(buffer_size)
            if data:
                self.logger.info(f"Received data: {data}")
                print("\n[<] Received data:")
                self.print_data_info(data, "Received")
                return data
            print("\n[-] No data received")
            return None
        except socket.error as e:
            self.logger.error(f"Error receiving data: {e}")
            print(f"\n[-] Error receiving data: {e}")
            return None

def main():
    # Example usage
    client = FORDIAC_Client()
    
    if client.connect():
        try:
            # Example: Send a test message
            test_message = b"Hello 4DIAC!"
            client.send_data(test_message)
            
            # Wait for response
            response = client.receive_data()
            
            # Send another message with different data type
            numeric_data = struct.pack('!f', 123.456)  # Example with float
            client.send_data(numeric_data)
            
            # Wait for another response
            response = client.receive_data()
            
        finally:
            client.disconnect()

if __name__ == "__main__":
    main()
