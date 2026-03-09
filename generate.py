#!/usr/bin/env python3
"""
CV Generator - Generates HTML CV from YAML data
"""

import yaml
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import os
import sys


def load_cv_data(yaml_file):
    """Load CV data from YAML file."""
    try:
        with open(yaml_file, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Error: YAML file '{yaml_file}' not found.")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        sys.exit(1)


def generate_html(data, template_file, output_file):
    """Generate HTML from template and data."""
    try:
        # Set up Jinja2 environment
        template_dir = os.path.dirname(template_file)
        env = Environment(loader=FileSystemLoader(template_dir))
        template = env.get_template(os.path.basename(template_file))

        # Add current date to data
        data['current_date'] = datetime.now().strftime('%B %Y')

        # Render template
        html_output = template.render(data)

        # Write output
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_output)

        print(f"✓ Successfully generated CV: {output_file}")

    except Exception as e:
        print(f"Error generating HTML: {e}")
        sys.exit(1)


def main():
    """Main function."""
    # File paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    yaml_file = os.path.join(script_dir, 'input', 'cv.yaml')
    template_file = os.path.join(script_dir, 'input', 'template.html')
    output_file = os.path.join(script_dir, 'index.html')

    # Check if required packages are installed
    try:
        import yaml
        import jinja2
    except ImportError as e:
        print(f"Error: Missing required package. Please install dependencies:")
        print("  pip install pyyaml jinja2")
        sys.exit(1)

    # Generate CV
    print("Generating CV...")
    data = load_cv_data(yaml_file)
    generate_html(data, template_file, output_file)
    print(f"\nYour CV is ready! Open {output_file} in your browser.")


if __name__ == '__main__':
    main()
