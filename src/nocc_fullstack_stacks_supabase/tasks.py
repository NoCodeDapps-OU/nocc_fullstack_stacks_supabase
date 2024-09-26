from crewai import Task

class SmartContractTasks:
    @staticmethod
    def setup_project(agent, project_name):
        return Task(
            description=f"Set up a new Clarity smart contract project structure named '{project_name}'",
            agent=agent,
            expected_output="A fully initialized project structure for a Clarity smart contract project."
        )

    @staticmethod
    def generate_contract(agent, requirements):
        return Task(
            description=f"Generate a Clarity smart contract based on the following requirements: {requirements}",
            agent=agent,
            expected_output="A complete Clarity smart contract code that fulfills the user's requirements."
        )

    @staticmethod
    def generate_tests(agent, contract):
        return Task(
            description=f"Generate a comprehensive test suite for the Clarity smart contract: {contract}",
            agent=agent,
            expected_output="A set of thorough test cases covering all functions and edge cases of the smart contract."
        )
    
    @staticmethod
    def validate_contract(agent, contract):
        return Task(
            description=f"Validate the Clarity smart contract: {contract}",
            agent=agent,
            expected_output="Validation result for the Clarity smart contract."
        )

    @staticmethod
    def validate_tests(agent, tests):
        return Task(
            description=f"Validate the test suite for the Clarity smart contract: {tests}",
            agent=agent,
            expected_output="Validation result for the test suite."
        )

    @staticmethod
    def finalize_project(agent, contract, tests):
        return Task(
            description=f"Validate and finalize the Clarity smart contract project. Contract: {contract}, Tests: {tests}",
            agent=agent,
            expected_output="A validated and finalized Clarity smart contract project, ready for deployment."
        )

class FrontendTasks:
    @staticmethod
    def design_frontend(agent, requirements):
        return Task(
            description=f"Design and implement the frontend structure using HTML and Tailwind CSS based on the following requirements: {requirements}",
            agent=agent,
            expected_output="Complete HTML structure with Tailwind CSS classes for the frontend."
        )

    @staticmethod
    def implement_javascript(agent, html_structure):
        return Task(
            description=f"Implement JavaScript functionality for the frontend based on the following HTML structure: {html_structure}",
            agent=agent,
            expected_output="JavaScript code to add interactivity and dynamic behavior to the frontend."
        )

    @staticmethod
    def integrate_stacksjs(agent, frontend_code):
        return Task(
            description=f"Integrate Stacks.js components into the frontend code: {frontend_code}",
            agent=agent,
            expected_output="Updated frontend code with Stacks.js components integrated for blockchain functionality."
        )

    @staticmethod
    def integrate_smart_contract(agent, frontend_code, contract):
        return Task(
            description=f"Integrate the Clarity smart contract with the frontend. Frontend code: {frontend_code}, Contract: {contract}",
            agent=agent,
            expected_output="Frontend code updated with smart contract integration, including function calls and event listeners."
        )

class BackendTasks:
    @staticmethod
    def setup_supabase(agent, project_details):
        return Task(
            description=f"Set up a Supabase project and create the necessary database structure for: {project_details}",
            agent=agent,
            expected_output="Detailed instructions for setting up Supabase project and database structure."
        )

    @staticmethod
    def generate_backend_code(agent, project_details, supabase_setup):
        return Task(
            description=f"Generate backend code for Supabase integration based on the project details: {project_details} and Supabase setup: {supabase_setup}",
            agent=agent,
            expected_output="Complete backend code for Supabase integration in JavaScript."
        )