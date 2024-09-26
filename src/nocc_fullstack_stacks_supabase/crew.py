from crewai import Crew, Process
from .agents import SmartContractAgents, FrontendAgents, BackendAgents
from .tasks import SmartContractTasks, FrontendTasks, BackendTasks

class SmartContractCrews:
    def __init__(self):
        self.agents = SmartContractAgents()

    def project_setup_crew(self, project_name):
        setup_agent = self.agents.project_setup_agent()
        setup_task = SmartContractTasks.setup_project(setup_agent, project_name)
        return Crew(
            agents=[setup_agent],
            tasks=[setup_task],
            verbose=True,
            process=Process.sequential
        )

    def contract_design_crew(self, requirements):
        designer = self.agents.contract_designer()
        design_task = SmartContractTasks.generate_contract(designer, requirements)
        return Crew(
            agents=[designer],
            tasks=[design_task],
            verbose=True,
            process=Process.sequential
        )

    def test_generation_crew(self, contract):
        tester = self.agents.contract_tester()
        test_task = SmartContractTasks.generate_tests(tester, contract)
        return Crew(
            agents=[tester],
            tasks=[test_task],
            verbose=True,
            process=Process.sequential
        )

    def contract_validation_crew(self, contract):
        validator = self.agents.contract_validator()
        validate_task = SmartContractTasks.validate_contract(validator, contract)
        return Crew(
            agents=[validator],
            tasks=[validate_task],
            verbose=True,
            process=Process.sequential
        )

    def test_validation_crew(self, tests):
        validator = self.agents.test_validator()
        validate_task = SmartContractTasks.validate_tests(validator, tests)
        return Crew(
            agents=[validator],
            tasks=[validate_task],
            verbose=True,
            process=Process.sequential
        )

    def project_finalization_crew(self, project_name, contract):
        finalizer = self.agents.project_finalizer()
        finalize_task = SmartContractTasks.finalize_project(finalizer, project_name, contract)
        return Crew(
            agents=[finalizer],
            tasks=[finalize_task],
            verbose=True,
            process=Process.sequential
        )

class FrontendCrews:
    def __init__(self):
        self.agents = FrontendAgents()

    def frontend_design_crew(self, requirements):
        designer = self.agents.frontend_designer()
        design_task = FrontendTasks.design_frontend(designer, requirements)
        return Crew(
            agents=[designer],
            tasks=[design_task],
            verbose=True,
            process=Process.sequential
        )

    def javascript_implementation_crew(self, html_structure):
        developer = self.agents.javascript_developer()
        js_task = FrontendTasks.implement_javascript(developer, html_structure)
        return Crew(
            agents=[developer],
            tasks=[js_task],
            verbose=True,
            process=Process.sequential
        )

    def stacksjs_integration_crew(self, frontend_code):
        integrator = self.agents.stacksjs_integrator()
        integration_task = FrontendTasks.integrate_stacksjs(integrator, frontend_code)
        return Crew(
            agents=[integrator],
            tasks=[integration_task],
            verbose=True,
            process=Process.sequential
        )

    def contract_integration_crew(self, frontend_code, contract):
        integrator = self.agents.contract_integrator()
        integration_task = FrontendTasks.integrate_smart_contract(integrator, frontend_code, contract)
        return Crew(
            agents=[integrator],
            tasks=[integration_task],
            verbose=True,
            process=Process.sequential
        )

class BackendCrews:
    def __init__(self):
        self.agents = BackendAgents()

    def supabase_integration_crew(self, project_details):
        integrator = self.agents.supabase_integrator()
        setup_task = BackendTasks.setup_supabase(integrator, project_details)
        code_task = BackendTasks.generate_backend_code(integrator, project_details, "")
        return Crew(
            agents=[integrator],
            tasks=[setup_task, code_task],
            verbose=True,
            process=Process.sequential
        )