import os
import yaml

# Usage
# 1. pip3 install pyyaml
# 2. Save this file in the root monaco directory (when the monaco binary is)
# 3. python3 generate-delete.file.py
# 4. A delete.yaml file will be created for you

# This script must be executed from the base directory (the same directory containing your monaco binary)
# The script looks for values for the  "name" variable. If you DON'T use:
# - name: "foo"
# then change name_key below to reflect what you use.
# If you're following best practices and monaco public docs (99% of people) YOU DO NOT NEED TO CHANGE ANYTHING
# 
# Usage
# python3 generate-delete-file.py

projects_folder_name = "projects"
name_key = "name" # Change this if you need to, 99% of people DO NOT need to change this


def get_delete_values():
  delete_values = []

  # Get projects
  projects = os.scandir(projects_folder_name)
  
  # For each project, get configuration types
  for project in projects:
    if os.path.isdir(project):
      #print(f"Printing project: {project.name}")
      
      # For each project get the configuration types
      # eg. auto-tag
      config_types = os.scandir(project)
      
      for config_type in config_types:
        #print(f"Config type in {project.name} is now {config_type.name}")
        
        # Get files inside each config_type directory
        files = os.scandir(config_type)

        # Find and work with only the YAML files...
        for file in files:
        
          if file.name.endswith('.yaml'):
            # Open the file
            with open(file.path, "r") as stream:
              try:
                docs = yaml.safe_load_all(stream)
                for doc in docs: # "config" is one doc, each tag is another doc
                  for k, v in doc.items():
                    # Skip config document
                    if k == "config": continue
                     # Loop through values and if key of value is matches the name_key (by default "name"), save it
                    for value in v:
                      if name_key in value:
                        # Get the value of name
                        #print(f"Name Value is: {value['name']}")
                        #print(f"Final Stored Value is: {config_type.name}/{value['name']}")
                        # Will store "auto-tag/Resistance is Futile!" from a doc such as:
                        # foo:
                        #   - name: "Resistance Is Futile!"
                        delete_values.append(f"{config_type.name}/{value['name']}")
              except yaml.YAMLError as exc:
                print(exc)
      return delete_values

def build_delete_output(delete_values):
  delete_output = {
    "delete": []
  }

  for delete_value in delete_values:
    delete_output['delete'].append(f"{delete_value}")

  return delete_output


delete_values = get_delete_values()
delete_output = build_delete_output(delete_values)

with open(r'delete.yaml', 'w') as file:
    docs = yaml.safe_dump(delete_output,file)
