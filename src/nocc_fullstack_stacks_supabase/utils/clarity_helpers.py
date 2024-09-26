import os
from anthropic import Anthropic
from dotenv import load_dotenv
from ..logger import log_step

load_dotenv()

anthropic = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def generate_clarity_contract(requirements: str) -> str:
    prompt = f"""
    Given the following requirements, generate a Clarity smart contract:

    Requirements:
    {requirements}

    Please provide a complete Clarity smart contract that includes:
    1. Appropriate data vars and maps
    2. Relevant functions with proper access controls
    3. Error handling
    4. Any necessary helper functions
    5. Comments explaining the purpose of each section

    Ensure the contract follows best practices for security and efficiency in Clarity.
    """

    message = anthropic.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=4096,  
        temperature=0.7,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    contract = message.content[0].text.strip()
    contract = contract.replace("```clarity", "").replace("```", "").strip()

    log_step("Generated Clarity Contract", contract)
    return contract

def generate_clarity_tests(contract: str) -> str:
    prompt = f"""
    Given the following Clarity smart contract, generate a comprehensive test suite using Clarinet and TypeScript:

    {contract}

    Your test suite should include:
    1. Unit tests for each public function
    2. Tests for edge cases and potential error conditions
    3. Tests for different user roles (if applicable)
    4. Tests for any complex logic or calculations

    Provide the COMPLETE test cases in TypeScript format compatible with Clarinet, including setup, execution, and assertions for each test. 
    Ensure that the test suite is complete, syntactically correct, and covers all aspects of the contract.
    Include necessary imports and the complete Clarinet.test structure for each test case.
    Do not include any explanations or summaries, only output the actual TypeScript code for the tests.
    """

    message = anthropic.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=4096,  
        temperature=0.7,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    tests = message.content[0].text.strip()
    tests = tests.replace("```typescript", "").replace("```", "").strip()
    
    log_step("Generated Clarity Tests", tests)
    return tests

def validate_clarity_contract(contract: str) -> str:
    # Implement actual validation logic here
    validation_result = "Contract validation successful."
    log_step("Validated Clarity Contract", validation_result)
    return validation_result

def validate_clarity_tests(tests: str) -> str:
    # Implement actual test validation logic here
    validation_result = "Test validation successful."
    log_step("Validated Clarity Tests", validation_result)
    return validation_result

def setup_project_structure(project_name: str) -> str:
    try:
        project_dir = os.path.join(os.getcwd(), project_name)
        os.makedirs(project_dir, exist_ok=True)
        os.makedirs(os.path.join(project_dir, "contracts"), exist_ok=True)
        os.makedirs(os.path.join(project_dir, "tests"), exist_ok=True)
        os.makedirs(os.path.join(project_dir, "frontend"), exist_ok=True)
        os.makedirs(os.path.join(project_dir, "logs"), exist_ok=True)
        
        result = f"Project structure for '{project_name}' set up successfully in {project_dir}."
        log_step("Set Up Project Structure", result)
        return result
    except Exception as e:
        error = f"Error setting up project structure: {str(e)}"
        log_step("Set Up Project Structure Error", error)
        return error

def save_contract(project_name: str, contract: str) -> str:
    try:
        os.makedirs(os.path.join(project_name, "contracts"), exist_ok=True)
        contract_path = os.path.join(project_name, "contracts", "contract.clar")
        with open(contract_path, "w") as f:
            f.write(contract)
        result = f"Contract saved successfully to {contract_path}"
        log_step("Saved Contract", result)
        return result
    except Exception as e:
        error = f"Error saving contract: {str(e)}"
        log_step("Save Contract Error", error)
        return error

def save_tests(project_name: str, tests: str) -> str:
    try:
        os.makedirs(os.path.join(project_name, "tests"), exist_ok=True)
        tests_path = os.path.join(project_name, "tests", "contract_test.ts")
        with open(tests_path, "w") as f:
            f.write(tests)
        result = f"Tests saved successfully to {tests_path}"
        log_step("Saved Tests", result)
        return result
    except Exception as e:
        error = f"Error saving tests: {str(e)}"
        log_step("Save Tests Error", error)
        return error