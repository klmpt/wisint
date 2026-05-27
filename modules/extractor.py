import re
import subprocess
import html
import urllib.parse

class DataExtractor:
    def __init__(self):
        self.patterns = {
            "emails": r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
            "phones": r'\+?\d{1,4}[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{3}[-.\s]?\d{2}[-.\s]?\d{2}',
            "btc": r'[13][a-km-zA-HJ-NP-Z1-9]{25,34}',
            "eth": r'0x[a-fA-F0-9]{40}',
            "socials": r'(https?://(?:www\.)?(?:vk|t\.me|instagram|facebook|twitter|linkedin)\.com/[^\s"<>]+)',
            "telegram_id": r'@\w{5,32}',
            "meta_desc": r'<meta name="description" content="([^"]+)"',
            "author": r'author" content="([^"]+)"',
            "ip_addr": r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        }
        self.ua = "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0"

    def _execute(self, cmd):
        try:
            return subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.DEVNULL)
        except:
            return ""

    def get_server_info(self, url):
        raw_headers = self._execute(f"curl -I -s -L -m 5 '{url}'")
        server_match = re.search(r'Server: (.+)', raw_headers, re.IGNORECASE)
        return server_match.group(1).strip() if server_match else "Unknown"

    def get_robots_txt(self, url):
        parsed = urllib.parse.urlparse(url)
        base = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
        robots = self._execute(f"curl -s -L -m 5 '{base}'")
        disallowed = re.findall(r'Disallow: (.*)', robots)
        return [d.strip() for d in disallowed if d.strip()]

    def search_hidden_comments(self, raw_html):
        return list(set(re.findall(r'', raw_html, re.DOTALL)))

    def extract(self, url):
        raw_html = self._execute(f"curl -s -L -m 10 -A '{self.ua}' '{url}'")
        if not raw_html:
            return {"error": "Connection timeout or unreachable"}

        text_content = self._execute(f"echo '{html.escape(raw_html)}' | lynx -dump -stdin")
        
        report = {
            "server_type": self.get_server_info(url),
            "hidden_paths": self.get_robots_txt(url),
            "found": {}
        }
        
        for key, pattern in self.patterns.items():
            source = raw_html if key in ["meta_desc", "author"] else text_content
            found = re.findall(pattern, source)
            report["found"][key] = list(set(found))
            
        report["hidden_comments"] = self.search_hidden_comments(raw_html)
        return report

    def validate_data(self, data):
        for key in data.get("found", {}):
            if key == "phones":
                data["found"][key] = [re.sub(r'[\s\-\(\)]', '', p) for p in data["found"][key]]
        return data