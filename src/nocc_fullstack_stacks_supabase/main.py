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
    smart_contract_crews = SmartContractCrews()
    frontend_crews = FrontendCrews()
    backend_crews = BackendCrews()

    # Get user input
    project_name = input("Enter the name for your project: ")
    os.environ["PROJECT_NAME"] = project_name
    project_type = input("Enter the type of project (e.g., NFT marketplace, DeFi app): ")
    contract_requirements = input("Describe the requirements for your smart contract: ")
    frontend_requirements = input("Describe the requirements for your frontend: ")

    project_details = {
        "project_name": project_name,
        "project_type": project_type,
        "frontend_requirements": frontend_requirements
    }

    try:
        # Step 1: Set up the project structure
        setup_result = smart_contract_crews.project_setup_crew(project_name).kickoff()
        print("Project Setup:", setup_result)
        if not get_user_confirmation("Do you want to proceed with contract generation?"):
            return

        # Step 2: Generate the contract
        contract_result = smart_contract_crews.contract_design_crew(contract_requirements).kickoff()
        print("Contract Generation:", contract_result)
        if not get_user_confirmation("Do you want to proceed with test generation?"):
            return

        # Step 3: Generate tests
        test_result = smart_contract_crews.test_generation_crew(str(contract_result)).kickoff()
        print("Test Generation:", test_result)
        if not get_user_confirmation("Do you want to proceed with contract validation?"):
            return

        # Step 4: Validate the contract and tests
        validation_result = smart_contract_crews.contract_validation_crew(str(contract_result)).kickoff()
        print("Contract Validation:", validation_result)

        test_validation_result = smart_contract_crews.test_validation_crew(str(test_result)).kickoff()
        print("Test Validation:", test_validation_result)
        if not get_user_confirmation("Do you want to proceed with frontend design?"):
            return

        # Step 5: Design Frontend
        frontend_result = frontend_crews.frontend_design_crew(frontend_requirements).kickoff()
        print("Frontend Design:", str(frontend_result))
        if not get_user_confirmation("Do you want to proceed with JavaScript implementation?"):
            return

        # Step 6: Implement JavaScript
        js_result = frontend_crews.javascript_implementation_crew(str(frontend_result)).kickoff()
        print("JavaScript Implementation:", js_result)
        if not get_user_confirmation("Do you want to proceed with Stacks.js integration?"):
            return

        # Step 7: Integrate Stacks.js
        stacksjs_result = frontend_crews.stacksjs_integration_crew(str(js_result)).kickoff()
        print("Stacks.js Integration:", stacksjs_result)
        if not get_user_confirmation("Do you want to proceed with smart contract integration?"):
            return

        # Step 8: Integrate Smart Contract with Frontend
        contract_integration_result = frontend_crews.contract_integration_crew(str(stacksjs_result), str(contract_result)).kickoff()
        print("Contract Integration:", contract_integration_result)
        if not get_user_confirmation("Do you want to proceed with Supabase backend integration?"):
            return

        # Step 9: Supabase Backend Integration
        backend_result = backend_crews.supabase_integration_crew(project_details).kickoff()
        print("Supabase Backend Integration:", str(backend_result))

        # Save backend code
        backend_code = str(backend_result)
        save_result = save_backend_code(project_name, backend_code)
        print("Save Backend Code:", save_result)

        print(f"\nProject completed! All components have been generated and saved in the '{project_name}' directory.")

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