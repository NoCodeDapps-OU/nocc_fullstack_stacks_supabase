from datetime import datetime

def log_step(step_name: str, content: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {step_name}:\n{content}\n\n"
    print(log_entry)