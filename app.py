import psutil
from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
    cpu_percent=psutil.cpu_percent()
    memory_percent=psutil.virtual_memory().percent
    Message=None
    if cpu_percent >80 or memory_percent >80:
        Message="High CPU or Memory Usage"
    return f"CPU Percentage:{cpu_percent} Memory Percentage:{memory_percent} Message:{Message}"
    

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8081)
