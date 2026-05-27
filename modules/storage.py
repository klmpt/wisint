import json

class Storage:
    def save(self, target, data):
        filename = f"{target}_report.json"
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"[!] data saved on {filename}")