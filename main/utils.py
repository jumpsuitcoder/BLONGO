import uuid
import os
import datetime

image_dir = datetime.datetime.now().strftime('img/%Y/%m/%d/')
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join(image_dir, filename)