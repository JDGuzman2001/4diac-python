# 4DIAC Socket Communication Client

This Python client implements a socket-based communication interface for 4DIAC (Framework for Industrial Automation and Control). It provides a robust way to establish TCP/IP connections with 4DIAC runtime environment (FORTE) and handle data exchange.

## Features

- TCP/IP socket communication with 4DIAC runtime
- Comprehensive data analysis and visualization
- Multiple data format support
- Detailed logging and error handling
- Connection management
- Support for both text and binary data

## Requirements

- Python 3.x
- Running instance of 4DIAC-RTE (FORTE)
- Network connectivity to the 4DIAC runtime

## Installation

1. Clone this repository or download the files
2. Ensure you have Python 3.x installed
3. No additional dependencies are required as the script uses only Python standard library

## Usage

### Basic Usage

```python
from main import FORDIAC_Client

# Create a client instance
client = FORDIAC_Client(host='localhost', port=61499)

# Connect to 4DIAC
if client.connect():
    try:
        # Send text data
        client.send_data(b"Hello 4DIAC!")
        
        # Receive response
        response = client.receive_data()
        
    finally:
        client.disconnect()
```

### Advanced Usage

```python
import struct
from main import FORDIAC_Client

client = FORDIAC_Client(host='192.168.1.100', port=61499)

if client.connect():
    try:
        # Send float data
        float_value = 123.456
        float_bytes = struct.pack('!f', float_value)
        client.send_data(float_bytes)
        
        # Receive and analyze response
        response = client.receive_data()
        
    finally:
        client.disconnect()
```

## Class Description

### FORDIAC_Client

The main class that handles all communication with 4DIAC.

#### Constructor Parameters

- `host` (str): The host address of the 4DIAC runtime (default: 'localhost')
- `port` (int): The port number (default: 61499)

#### Main Methods

1. `connect()`
   - Establishes connection to 4DIAC runtime
   - Returns: bool (True if successful)

2. `disconnect()`
   - Safely closes the connection
   - No return value

3. `send_data(data)`
   - Sends data to 4DIAC runtime
   - Parameters:
     - `data` (bytes): Data to send
   - Returns: bool (True if successful)

4. `receive_data(buffer_size=1024)`
   - Receives data from 4DIAC runtime
   - Parameters:
     - `buffer_size` (int): Size of receive buffer
   - Returns: bytes or None

5. `print_data_info(data, source="")`
   - Analyzes and displays detailed information about data
   - Parameters:
     - `data` (bytes): Data to analyze
     - `source` (str): Description of data source

## Data Analysis Features

The client provides comprehensive data analysis through the `print_data_info` method, which shows:

1. **Basic Information**
   - Raw data representation
   - Data type
   - Length in bytes

2. **Hexadecimal Representation**
   - Data in hexadecimal format

3. **Text Representations**
   - UTF-8 encoding
   - ASCII encoding
   - ISO-8859-1 encoding

4. **Numeric Interpretations**
   - 32-bit integer
   - Float (32-bit)
   - Double (64-bit)

## Logging

The client implements two levels of logging:

1. **File Logging**
   - Uses Python's logging module
   - Logs to console with timestamp
   - Includes INFO and ERROR level messages

2. **Console Output**
   - Uses formatted print statements
   - Includes visual indicators:
     - `[+]` Success messages
     - `[-]` Error messages
     - `[>]` Sent data
     - `[<]` Received data
     - `[*]` General information

## Error Handling

The client includes comprehensive error handling for:
- Connection failures
- Send/receive operations
- Data encoding/decoding
- Socket errors

## Common Use Cases

1. **Simple Text Communication**
```python
client.send_data(b"Hello 4DIAC!")
```

2. **Sending Numeric Data**
```python
float_data = struct.pack('!f', 123.456)
client.send_data(float_data)
```

3. **Continuous Monitoring**
```python
while client.connected:
    response = client.receive_data()
    time.sleep(1)
```

## Best Practices

1. Always use the client in a try-finally block to ensure proper disconnection
2. Check the connection status before sending/receiving data
3. Handle the received data appropriately based on the expected format
4. Monitor the detailed data analysis output for debugging
5. Use appropriate buffer sizes based on your data requirements

## Troubleshooting

1. **Connection Issues**
   - Verify 4DIAC-RTE is running
   - Check host and port settings
   - Ensure network connectivity

2. **Data Format Issues**
   - Use the data analysis output to verify data format
   - Ensure proper data packing/unpacking
   - Check encoding compatibility

3. **Performance Issues**
   - Adjust buffer size for large data
   - Monitor system resources
   - Check network latency

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 