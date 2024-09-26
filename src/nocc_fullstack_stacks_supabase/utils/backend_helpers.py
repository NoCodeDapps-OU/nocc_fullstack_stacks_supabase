import os
from anthropic import Anthropic
from dotenv import load_dotenv
from ..logger import log_step
from ..prompts.backend_prompts import SUPABASE_SETUP_PROMPT, BACKEND_CODE_GENERATION_PROMPT

load_dotenv()

anthropic = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def setup_supabase(project_details: dict) -> str:
    prompt = SUPABASE_SETUP_PROMPT.format(**project_details)

    message = anthropic.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=2000,
        temperature=0.7,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    setup_instructions = message.content[0].text.strip()
    log_step("Supabase Setup Instructions", setup_instructions)
    return setup_instructions

def generate_backend_code(project_details: dict, supabase_setup: str) -> str:
    prompt = BACKEND_CODE_GENERATION_PROMPT.format(**project_details, supabase_setup=supabase_setup)

    message = anthropic.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=3000,
        temperature=0.7,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    backend_code = message.content[0].text.strip()
    log_step("Generated Backend Code", backend_code)
    return backend_code

def save_backend_code(project_name: str, backend_code: str) -> str:
    result = f"Backend code generated for {project_name}:\n\n{backend_code}"
    log_step("Generated Backend Code", result)
    return result