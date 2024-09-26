from langchain.tools import tool
from .utils.clarity_helpers import (
    setup_project_structure,
    generate_clarity_contract,
    generate_clarity_tests,
    validate_clarity_contract,
    save_contract,
    save_tests,
    validate_clarity_tests
)
from .utils.frontend_helpers import (
    generate_html_css,
    generate_javascript,
    integrate_stacksjs,
    integrate_contract,
    save_frontend
)
from .utils.backend_helpers import (
    setup_supabase,
    generate_backend_code,
    save_backend_code
)

class ClarityProjectSetup:
    @tool("Setup Clarity project structure")
    def setup_project(project_name: str) -> str:
        """Sets up a new project structure for Clarity smart contract development."""
        return setup_project_structure(project_name)

class ClarityContractGenerator:
    @tool("Generate Clarity smart contract")
    def generate_contract(requirements: str) -> str:
        """Generates a Clarity smart contract based on the given requirements."""
        return generate_clarity_contract(requirements)

class ClarityTestGenerator:
    @tool("Generate Clarity contract tests")
    def generate_tests(contract: str) -> str:
        """Generates a comprehensive test suite for a given Clarity smart contract."""
        return generate_clarity_tests(contract)

class ContractValidator:
    @tool("Validate Clarity smart contract")
    def validate_contract(contract: str) -> str:
        """Validates a given Clarity smart contract for correctness and security."""
        return validate_clarity_contract(contract)
    
class TestValidator:
    @tool("Validate Clarity contract tests")
    def validate_tests(tests: str) -> str:
        """Validates the given Clarity contract test suite for completeness and correctness."""
        return validate_clarity_tests(tests)

class ProjectFinalizer:
    @tool("Finalize Clarity project")
    def finalize_project(project_name: str, contract: str) -> str:
        """Finalizes the Clarity smart contract project, saving all components."""
        contract_result = save_contract(project_name, contract)
        tests = generate_clarity_tests(contract)
        tests_result = save_tests(project_name, tests)
        return f"Project finalized. {contract_result} {tests_result}"

class FrontendTools:
    @tool("Generate HTML and Tailwind CSS")
    def generate_html_css(requirements: str) -> str:
        """Generates HTML structure with Tailwind CSS classes based on the given requirements."""
        return generate_html_css(requirements)

    @tool("Generate JavaScript")
    def generate_javascript(html_structure: str) -> str:
        """Generates JavaScript code based on the given HTML structure."""
        return generate_javascript(html_structure)

class StacksTools:
    @tool("Integrate Stacks.js")
    def integrate_stacksjs(frontend_code: str) -> str:
        """Integrates Stacks.js
        """
        return integrate_stacksjs(frontend_code)
    
class StacksTools:
    @tool("Integrate Stacks.js")
    def integrate_stacksjs(frontend_code: str) -> str:
        """Integrates Stacks.js components into the given frontend code."""
        return integrate_stacksjs(frontend_code)

class ContractIntegrationTools:
    @tool("Integrate Smart Contract")
    def integrate_contract(frontend_code: str, contract: str) -> str:
        """Integrates the given Clarity smart contract with the frontend code."""
        return integrate_contract(frontend_code, contract)

    @tool("Save Frontend")
    def save_frontend(project_name: str, html_content: str, css_content: str, js_content: str, stacksjs_content: str) -> str:
        """Saves the frontend code to the project directory."""
        return save_frontend(project_name, html_content, css_content, js_content, stacksjs_content)
    
class BackendTools:
    @tool("Setup Supabase")
    def setup_supabase(project_details: dict) -> str:
        """Sets up a Supabase project and creates the necessary database structure."""
        return setup_supabase(project_details)

    @tool("Generate Backend Code")
    def generate_backend_code(project_details: dict, supabase_setup: str) -> str:
        """Generates backend code for Supabase integration based on the project details and setup."""
        return generate_backend_code(project_details, supabase_setup)

    @tool("Save Backend Code")
    def save_backend_code(project_name: str, backend_code: str) -> str:
        """Saves the generated backend code to the project directory."""
        return save_backend_code(project_name, backend_code)