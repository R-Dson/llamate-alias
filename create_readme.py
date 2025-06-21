import yaml
import os

INPUT_YAML_FILE = "model_aliases.yml"
OUTPUT_README_FILE = "README.md"

def create_readme_from_aliases():
    """
    Reads model aliases from a YAML file and generates a README.md
    with commands (in bash code blocks) and arguments formatted as a list.
    """
    try:
        with open(INPUT_YAML_FILE, 'r', encoding='utf-8') as f:
            aliases_data = yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Error: The file '{INPUT_YAML_FILE}' was not found in the current directory.")
        print("Please create it with the specified format.")
        return
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file '{INPUT_YAML_FILE}': {e}")
        return
    except Exception as e:
        print(f"An unexpected error occurred while reading '{INPUT_YAML_FILE}': {e}")
        return

    if not aliases_data:
        print(f"Warning: '{INPUT_YAML_FILE}' is empty or does not contain valid YAML data.")
        with open(OUTPUT_README_FILE, 'w', encoding='utf-8') as f_out:
            f_out.write("# Model Aliases for llamate\n\n")
            f_out.write(f"No model aliases found in `{INPUT_YAML_FILE}`.\n")
        print(f"'{OUTPUT_README_FILE}' created with a note.")
        return

    readme_content = []
    readme_content.append("# Model Aliases for llamate\n")
    readme_content.append("This file lists available model aliases and their default arguments.\n")
    readme_content.append("You can add these models to your `llamate` setup using the commands shown.\n")

    for model_name, details in aliases_data.items():
        readme_content.append("```bash")  # Start the code block with bash
        readme_content.append(f"llamate add \"{model_name}\"") # Command on a new line
        readme_content.append("```")      # End the code block

        args_dict = details.get('args', {})
        if args_dict:
            for key, value in args_dict.items():
                readme_content.append(f'- {key}: "{value}"')
        # If no args_dict or it's empty, no argument lines will be added.

        readme_content.append("")  # Add a blank line for separation after each entry

    try:
        with open(OUTPUT_README_FILE, 'w', encoding='utf-8') as f_out:
            f_out.write("\n".join(readme_content))
        print(f"Successfully created '{OUTPUT_README_FILE}'.")
    except IOError as e:
        print(f"Error writing to '{OUTPUT_README_FILE}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred while writing '{OUTPUT_README_FILE}': {e}")


if __name__ == "__main__":
    create_readme_from_aliases()
