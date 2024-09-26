import os
from anthropic import Anthropic
from dotenv import load_dotenv
from ..logger import log_step

load_dotenv()

anthropic = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def generate_html_css(requirements: str) -> tuple:
    prompt = f"""
    Given the following requirements, generate an HTML structure with Tailwind CSS classes:

    Requirements:
    {requirements}

    Please provide a complete HTML file that includes:
    1. Proper HTML5 structure
    2. Tailwind CSS classes for styling
    3. Responsive design considerations
    4. Semantic HTML elements
    5. Comments explaining the purpose of each section
    6. Link to the styles.css file
    7. Script tags for app.js and stacks-integration.js files

    Ensure the HTML is valid and follows best practices for modern web development.
    Include a script tag for loading Tailwind CSS from a CDN.
    """

    message = anthropic.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=4000,
        temperature=0.7,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    html_content = message.content[0].text.strip()
    html_content = html_content.replace("```html", "").replace("```", "").strip()
    css_content = "/* Tailwind CSS will be loaded from CDN */"

    log_step("Generated HTML and CSS", html_content)
    return html_content, css_content

def generate_javascript(html_structure: str) -> str:
    prompt = f"""
    Given the following HTML structure, generate JavaScript code to add interactivity and dynamic behavior:

    {html_structure}

    Please provide JavaScript code that includes:
    1. Event listeners for user interactions
    2. DOM manipulation to update the UI dynamically
    3. Any necessary AJAX calls (you can use fetch API)
    4. Error handling and input validation
    5. Comments explaining the purpose of each function or section of code

    Ensure the JavaScript is modern (ES6+) and follows best practices for web development.
    """

    message = anthropic.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=4000,
        temperature=0.7,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    js_content = message.content[0].text.strip()
    js_content = js_content.replace("```javascript", "").replace("```", "").strip()

    log_step("Generated JavaScript", js_content)
    return js_content

def integrate_stacksjs(frontend_code: str) -> str:
    prompt = f"""
    Given the following frontend code, integrate Stacks.js components and functionality:

    {frontend_code}

    Please provide ONLY the complete JavaScript code that includes:
    1. Necessary Stacks.js imports (use unpkg.com CDN for @stacks/connect, @stacks/network, and @stacks/transactions)
    2. Stacks authentication flow using @stacks/connect
    3. Functions to interact with Stacks blockchain (e.g., read from and write to smart contracts)
    4. UI elements to display Stacks wallet information and transaction status
    5. Error handling for Stacks-related operations
    6. Comments explaining the Stacks.js integration

    Ensure the integration follows best practices for Stacks.js usage and maintains the existing functionality of the frontend.
    Include the FULL code for connecting to the Hiro Wallet (formerly Stacks Wallet).
    Use the StacksMocknet for the network configuration.
    Do not include any HTML or explanations, only output the actual JavaScript code.
    """

    message = anthropic.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=4000,
        temperature=0.7,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    js_code = message.content[0].text.strip()
    js_code = js_code.replace("```javascript", "").replace("```", "").strip()
    
    log_step("Integrated Stacks.js", js_code)
    return js_code

def integrate_contract(frontend_code: str, contract: str) -> str:
    prompt = f"""
    Given the following frontend code and Clarity smart contract, integrate the contract functionality into the frontend:

    Frontend Code:
    {frontend_code}

    Clarity Smart Contract:
    {contract}

    Please update the frontend code to include:
    1. Functions to call the smart contract methods
    2. UI elements to interact with the smart contract (e.g., forms, buttons)
    3. Display of smart contract data and transaction results
    4. Error handling for contract interactions
    5. Comments explaining the integration of each smart contract function

    Ensure the integration follows best practices for interacting with Clarity smart contracts from a web frontend.
    """

    message = anthropic.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=4000,
        temperature=0.7,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    js_content = message.content[0].text.strip()
    js_content = js_content.replace("```javascript", "").replace("```", "").strip()

    log_step("Integrated Contract", js_content)
    return js_content

def save_frontend(project_name: str, html_content: str, css_content: str, js_content: str, stacksjs_content: str) -> str:
    try:
        os.makedirs(os.path.join(project_name, "frontend"), exist_ok=True)
        
        html_path = os.path.join(project_name, "frontend", "index.html")
        with open(html_path, "w") as f:
            f.write(html_content)
        css_path = os.path.join(project_name, "frontend", "styles.css")
        with open(css_path, "w") as f:
            f.write(css_content)
        
        js_path = os.path.join(project_name, "frontend", "app.js")
        with open(js_path, "w") as f:
            f.write(js_content)
        
        stacksjs_path = os.path.join(project_name, "frontend", "stacks-integration.js")
        with open(stacksjs_path, "w") as f:
            f.write(stacksjs_content)
        
        result = f"Frontend code saved successfully to {project_name}/frontend/"
        log_step("Saved Frontend", result)
        return result
    except Exception as e:
        error = f"Error saving frontend code: {str(e)}"
        log_step("Save Frontend Error", error)
        return error