import psutil
from flask import Flask, render_template
import time
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    # cpu_metric = psutil.cpu_percent()
    # mem_metric = psutil.virtual_memory().percent
    Message = None

        # Get CPU usage
    cpu_usage = psutil.cpu_percent()
    
    # Get memory usage
    memory = psutil.virtual_memory()
    memory_total = memory.total
    memory_used = memory.total - memory.available
    memory_percent = memory.percent
    
    # Get disk usage
    disk_usage = psutil.disk_usage('/')
    
    if cpu_usage > 80 or memory_percent > 80:
        Message = "High CPU or Memory Detected, scale up!!!"
    # Print the monitored data
    print(f"Date & Time: { datetime.datetime.now() }")
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Total: {memory_total / (1024 ** 3)} GB")
    print(f"Memory Used: {memory_used / (1024 ** 3)} GB")
    print(f"Memory Percent: {memory_percent}%")
    print(f"Disk Total: {disk_usage.total / (1024 ** 3)} GB")
    print(f"Disk Used: {disk_usage.used / (1024 ** 3)} GB")
    print(f"Disk Percent: {disk_usage.percent}%")
    print("--------------------------------------------")
        
    return render_template("index.html", cpu_metric=cpu_usage, mem_metric=memory_percent, disk_metric=disk_usage.percent, message=Message)

if __name__=='__main__':
    app.run(debug=True, host = '0.0.0.0')
