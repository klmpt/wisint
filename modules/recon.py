import subprocess

class ReconEngine:
    def __init__(self, target):
        self.target = target

    def search(self):
        print(f"[*] Gathering links for: {self.target}")
        url = f"https://html.duckduckgo.com/html/?q={self.target}"
        ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        
        # Executes curl search and extracts URLs using grep
        cmd = f"curl -s -A '{ua}' -d 'q={self.target}' '{url}' | grep -oP 'http[s]?://[^\" >]+' | grep -v 'duckduckgo' | sort -u"
        
        try:
            raw_output = subprocess.check_output(cmd, shell=True, text=True)
            links = raw_output.splitlines()
            
            # Save results to a file for later analysis
            filename = f"{self.target}_links.txt"
            with open(filename, "w") as f:
                for link in links:
                    f.write(link + "\n")
            
            print(f"[*] Search complete. {len(links)} unique links saved to '{filename}'.")
            return links
            
        except subprocess.CalledProcessError:
            print(f"[-] Error: Recon search failed.")
            return []