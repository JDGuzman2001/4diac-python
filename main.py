import socket
import json
import xml.etree.ElementTree as ET

HOST = '127.0.0.1'
PORT = 61499
# PORT = 5000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[Servidor TCP] Escuchando en {HOST}:{PORT}")
    while True:  # Aceptar múltiples conexiones
        conn, addr = s.accept()
        with conn:
            print(f"[Servidor TCP] Conectado con {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                msg = data.decode().strip().replace('\0', '')
                print(f"[Servidor TCP] Recibido: {msg}")
                try:
                    # Quitar cualquier prefijo antes del XML
                    if "<" in msg:
                        msg = msg[msg.index("<"):]
                    
                    # Parse XML
                    root = ET.fromstring(msg)
                    print(f"XML decodificado: {root.tag}")
                    
                    # Process the request based on the Action attribute
                    action = root.get('Action')
                    if action == "QUERY":
                        fb = root.find('.//FB')
                        if fb is not None and fb.get('Name') == "*" and fb.get('Type') == "*":
                            # Responder con recursos (puedes agregar más si quieres)
                            response = f'<Response ID="{root.get("ID")}" Action="QUERY"><Resource Name="EMB_RES" Type="EMB_RES"/></Response>'
                        else:
                            # Responder con FBs específicos si es necesario
                            fb_name = fb.get('Name')
                            fb_type = fb.get('Type')
                            response = f'<Response ID="{root.get("ID")}" Action="QUERY"><FB Name="{fb_name}" Type="{fb_type}"/></Response>'
                    elif action == "READ":
                        response = f'<Response ID="{root.get("ID")}" Action="READ"></Response>'
                    else:
                        response = f'<Response ID="{root.get("ID")}" Action="{action}" Status="error"><Error>Unsupported action</Error></Response>'
                    
                except Exception as e:
                    print(f"Error al procesar XML: {e}")
                    response = f'<Response Status="error"><Error>{str(e)}</Error></Response>'
                
                conn.sendall(response.encode())
