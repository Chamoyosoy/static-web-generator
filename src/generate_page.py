import os
from markdown_block import markdown_to_html_node

def extract_title(markdown):
    try:
        with open(markdown) as f:
            title = f.readline().rstrip()
            if title.startswith("# "):
                print(title.replace("# ", ""))
                return title.replace("# ", "")
                
    except Exception as e:
        return f'Error: {e}'

def generate_page(from_path,template_path,dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    
    from_path = os.path.abspath(from_path)
    template_path = os.path.abspath(template_path)
    dest_path = os.path.abspath(dest_path)

    if not os.path.exists(dest_path):
        try: #if not exist try to create the path 
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            
        except Exception as e:
            return f'Error: creating directory {e}'

    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as f:
        template = f.read()
    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(from_path)
    # final = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    final = template.replace("{{ Content }}", content).replace("{{ Title }}", title)
    try:
        with open(dest_path, "w") as f:
            f.write(final)
        return f'succesfully wrote to {dest_path}'
    except Exception as e:
        return f'Error: writing to file {e}'
