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
        
    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as f:
        template = f.read()
    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(from_path)
    final = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    try:
        with open(dest_path, "w") as f:
            f.write(final)
        return f'succesfully wrote to {dest_path}'
    except Exception as e:
        return f'Error: writing to file {e}'

def generate_pages(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename).replace(".md", ".html")
  
        try:
            if os.path.isfile(src_path):
                generate_page(src_path, template_path, dest_path)
            elif os.path.isdir(src_path):
                os.mkdir(dest_path)
                generate_pages(src_path, template_path, dest_path)
        except Exception as e:
            return f'Error: {e}'
