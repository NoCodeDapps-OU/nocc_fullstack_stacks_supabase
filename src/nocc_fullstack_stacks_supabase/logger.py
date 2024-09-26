import os
from datetime import datetime

def log_step(step_name: str, content: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {step_name}:\n{content}\n\n"
    
    project_name = os.environ.get("PROJECT_NAME", "unnamed_project")
    log_dir = os.path.join(project_name, "logs")
    os.makedirs(log_dir, exist_ok=True)
    
    log_file = os.path.join(log_dir, "generation_log.txt")
    
    with open(log_file, "a") as f:
        f.write(log_entry)

    print(f"Logged {step_name}")