SUPABASE_SETUP_PROMPT = """
Given the following project details, provide step-by-step instructions to set up a Supabase project and create the necessary database structure:

Project Name: {project_name}
Project Type: {project_type}
Frontend Requirements: {frontend_requirements}

Please include:
1. Steps to create a new Supabase project
2. SQL commands to create tables and relationships
3. Instructions for setting up authentication (if required)
4. Any necessary Supabase configurations (e.g., row-level security policies)

Ensure the instructions are clear and can be followed by a developer with basic Supabase knowledge.
"""

BACKEND_CODE_GENERATION_PROMPT = """
Based on the following project details and Supabase setup, generate the necessary backend code in JavaScript:

Project Name: {project_name}
Project Type: {project_type}
Frontend Requirements: {frontend_requirements}
Supabase Setup: {supabase_setup}

Please provide:
1. JavaScript code for initializing the Supabase client
2. Functions for interacting with the Supabase database (CRUD operations)
3. Any necessary authentication logic
4. Error handling and data validation

Ensure the code follows best practices for Supabase integration and is well-commented for clarity.
"""