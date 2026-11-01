import re
from urllib.parse import urlparse


info = (
    "No URL entered",
  "Could not identify",
 "No listed warning",
  "This text is not a valid URL"
)

def inspurl(rawurl):
    url = rawurl.strip()
    result = []

    if url == "":
     return ["No URL entered."]
    if "://" not in url:
        url = "http://" + url
    try:
        parsed = urlparse(url)
    except ValueError:
        return ["This text is not a valid URL format."]
    host = (parsed.hostname or "").lower()
    if not host:
        return ["Could not identify a hostname."]
    if "@" in url:
        result.append("Contains an @ symbol; inspect carefully.")
    if len(rawurl.strip()) > 100:
        result.append("Unusually long URL (over 100 characters).")

    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        result.append("Uses an IP address instead of a familiar domain.")

    parts = host.split(".")
    if len(parts) >= 5:
        result.append("Contains many hostname segments/subdomains.")
    if "xn--" in host:
        result.append("Contains a punycode-style hostname.")

    if parsed.scheme == "http":
        result.append("Uses HTTP. HTTPS alone does not prove trust.")

    if len(result) == 0:
        result.append("No listed warning signs found. This does NOT prove safety.")
    return result



def haswarnings(result):
    return not result[0].startswith(info)


def main():
    print("EWB Phishing URL Awareness Checker")
    
    while True:
        url = input("\nEnter a sample URL (or type q to quit): ")

        if url.lower().strip() in ("q", "quit", "exit"):
            print("Goodbye! Stay alert online.")
            break

        result = inspurl(url)

        print("\nResult:")
        for x in result:
            print("-", x)

        if haswarnings(result):
            print("\nREVIEW CAREFULLY:", len(result), "warning sign(s) found.")
        print("Never enter passwords from unexpected links.")


if __name__ == "__main__":
    main()