import os
import shutil

def copy_static(target_dir, working_dir):
    
    try:
        for filename in os.listdir(working_dir):
            src_path = os.path.join(working_dir, filename)
            dst_path = os.path.join(target_dir, filename)

            if os.path.isdir(src_path):
                os.mkdir(dst_path)
                for obj in os.listdir(src_path):
                    src_path2 = os.path.join(src_path, obj)
                    dst_path2 = os.path.join(dst_path, obj)
                    shutil.copy(src_path2, dst_path2)
            else:
                shutil.copy(src_path, dst_path)

    except Exception as e:
        return f'Error: {e}'