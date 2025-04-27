#a function that recursively digs through a specified directory
#and stores all file and dir paths to a list which is returned at the end
import os
def path_finder(source_dir):
    obj_in_dir = os.listdir(source_dir)
    if len(obj_in_dir) == 0:
        return []
    list_of_paths = []
    for obj in obj_in_dir:
        obj_path = os.path.join(source_dir, obj)
        list_of_paths.append(obj_path)
        if os.path.isdir(obj_path):
            list_of_paths.extend(path_finder(obj_path))
    return list_of_paths
