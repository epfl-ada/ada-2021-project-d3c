import callbacks
from app import app 

server = app.server  
if __name__ == '__main__':
    app.run_server(port=5000, host= '127.0.01',debug=True)