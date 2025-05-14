# 4DIAC Socket Communication Server

This Python server implements a socket-based communication interface for 4DIAC (Framework for Industrial Automation and Control). It provides a robust way to establish TCP/IP connections and handle XML-based communication with 4DIAC clients.

## Features

- TCP/IP socket server implementation
- XML message parsing and handling
- Support for QUERY and READ actions
- Detailed logging and error handling
- Connection management
- Multiple client support

## Requirements

- Python 3.x
- Network connectivity
- XML message format compliance

## Installation

1. Clone this repository or download the files
2. Ensure you have Python 3.x installed
3. No additional dependencies are required as the script uses only Python standard library

## Usage

### Running the Server

```python
# The server will start listening on localhost:61499 by default
python main.py
```

### Supported XML Actions

The server currently supports the following XML actions:

1. **QUERY**
   - Query for resources or specific FBs
   - Example request:
     ```xml
     <Request ID="1" Action="QUERY">
         <FB Name="*" Type="*"/>
     </Request>
     ```

2. **READ**
   - Read operation
   - Example request:
     ```xml
     <Request ID="1" Action="READ">
     </Request>
     ```

## Server Implementation Details

### Configuration

The server is configured with the following default settings:
- Host: 127.0.0.1
- Port: 61499

### Message Processing

The server processes incoming XML messages with the following features:

1. **XML Parsing**
   - Validates XML structure
   - Extracts action type and parameters
   - Handles malformed XML gracefully

2. **Response Generation**
   - Generates appropriate XML responses
   - Includes status and error information
   - Maintains request ID in responses

### Error Handling

The server includes comprehensive error handling for:
- Connection failures
- XML parsing errors
- Invalid message formats
- Socket errors

## Best Practices

1. Ensure proper XML formatting in client messages
2. Handle server responses appropriately
3. Implement proper error handling on the client side
4. Monitor server logs for debugging
5. Use appropriate message sizes

## Troubleshooting

1. **Connection Issues**
   - Verify server is running
   - Check host and port settings
   - Ensure network connectivity

2. **XML Format Issues**
   - Verify XML structure
   - Check action names
   - Ensure proper attribute formatting

3. **Performance Issues**
   - Monitor system resources
   - Check network latency
   - Verify client connection handling
