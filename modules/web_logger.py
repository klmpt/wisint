import os

class WebLogger:
    """
    Module for generating web traps (honeypots) to capture 
    visitor technical data via PHP.
    """
    def create_trap(self, filename="trap.php", redirect_url="https://google.com"):
        php_code = f"""<?php
$log_file = "visitor_log.txt";
$ip = $_SERVER['REMOTE_ADDR'];
$ua = $_SERVER['HTTP_USER_AGENT'];
$time = date('Y-m-d H:i:s');
$details = "[$time] IP: $ip | UA: $ua" . PHP_EOL;

// Log visitor details
file_put_contents($log_file, $details, FILE_APPEND);

// Redirect the visitor
header("Location: {redirect_url}");
exit();
?>"""
        try:
            with open(filename, "w") as f:
                f.write(php_code)
            return f"File '{filename}' created successfully. Redirect set to: {redirect_url}"
        except Exception as e:
            return f"Error creating trap: {str(e)}"