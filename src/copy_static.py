import os
import shutil

def copy_static(working_dir, target_dir):
    
    
    for filename in os.listdir(working_dir):
        src_path = os.path.join(working_dir, filename)
        dst_path = os.path.join(target_dir, filename)
        try:
            if os.path.isdir(src_path):
                os.mkdir(dst_path)
                copy_static(src_path, dst_path)
            else:
                shutil.copy(src_path, dst_path)

        except Exception as e:
            return f'Error: {e}'