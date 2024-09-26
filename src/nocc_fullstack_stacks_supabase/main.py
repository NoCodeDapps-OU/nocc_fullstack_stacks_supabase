import os
from dotenv import load_dotenv
from crewai import Agent, Task
from .crew import SmartContractCrews, FrontendCrews, BackendCrews
from .utils.backend_helpers import save_backend_code

load_dotenv()

def get_user_confirmation(message: str) -> bool:
    while True:
        user_input = input(f"{message} (yes/no): ").lower()
        if user_input in ['yes', 'y']:
            return True
        elif user_input in ['no', 'n']:
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def run():
    # Get user input
    project_name = input("Enter the name for your project: ")
    project_type = input("Enter the type of project (e.g., NFT marketplace, DeFi app): ")
    contract_requirements = input("Describe the requirements for your smart contract: ")
    frontend_requirements = input("Describe the requirements for your frontend: ")

    project_details = {
        "project_name": project_name,
        "project_type": project_type,
        "frontend_requirements": frontend_requirements
    }

    try:
        # Generate and display each component
        smart_contract_crews = SmartContractCrews()
        frontend_crews = FrontendCrews()
        backend_crews = BackendCrews()

        # Generate contract
        contract_result = smart_contract_crews.contract_design_crew(contract_requirements).kickoff()
        print("Contract Generation:", contract_result)

        # Generate tests
        test_result = smart_contract_crews.test_generation_crew(str(contract_result)).kickoff()
        print("Test Generation:", test_result)

        # Generate frontend
        frontend_result = frontend_crews.frontend_design_crew(frontend_requirements).kickoff()
        print("Frontend Design:", str(frontend_result))

        # Generate backend
        backend_result = backend_crews.supabase_integration_crew(project_details).kickoff()
        print("Supabase Backend Integration:", str(backend_result))

        print(f"\nProject components generated for '{project_name}'.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def train():
    print("Training functionality not implemented yet.")

def replay():
    print("Replay functionality not implemented yet.")

def test():
    print("Testing functionality not implemented yet.")

if __name__ == "__main__":
    run()