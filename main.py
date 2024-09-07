import os
from pathlib import Path
from lib_resume_builder_AIHawk import FacadeManager, StyleManager, ResumeGenerator, Resume

openai_api_key = "api-key"

style_manager = StyleManager()
resume_generator = ResumeGenerator()
with open('my_resume.yaml', 'r') as file:
    my_resume = file.read()
resume_object = Resume(my_resume)
resume_generator_manager = FacadeManager(openai_api_key, style_manager, resume_generator, resume_object, Path("data_folder/output"))
os.system('cls' if os.name == 'nt' else 'clear')
resume_generator_manager.choose_style()
os.system('cls' if os.name == 'nt' else 'clear')
        
# Generate resume
output_file = "output_resume.html"
resume_generator_manager.resume_generator.create_resume(resume_generator_manager.selected_style_path, output_file)

print(f"Resume generated: {output_file}")

# Steps to run the script
# 1. python3 -m venv virtual
# 2. source virtual/bin/activate  
# 3. pip install -e .
# 4. python main.py
