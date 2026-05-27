import subprocess
import json

class ImageAnalyzer:
    def get_exif(self, file_path):
        print(f"[*] catching metadata: {file_path}")
        cmd = f"exiftool -j '{file_path}'"
        result = subprocess.check_output(cmd, shell=True, text=True)
        return json.loads(result)[0]