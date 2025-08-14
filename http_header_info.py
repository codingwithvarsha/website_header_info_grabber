import requests

def get_headers(url):
    """Fetch HTTP response headers from the given URL."""
    try:
        # If scheme (http/https) is missing, add https by default
        if not url.startswith("http"):
            url = "https://" + url

        # Try HEAD request first for speed, fallback to GET if blocked
        try:
            response = requests.head(url, allow_redirects=True, timeout=5)
            if response.status_code >= 400 or not response.headers:
                response = requests.get(url, allow_redirects=True, timeout=5)
        except requests.RequestException:
            # If HEAD fails completely, try GET
            response = requests.get(url, allow_redirects=True, timeout=5)

        return response.headers
    except requests.exceptions.RequestException as e:
        print(f"[!] Error fetching headers: {e}")
        return None


def check_security_headers(headers):
    """Check for common security-related HTTP headers."""
    important_headers = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Content-Type-Options",
        "X-Frame-Options",
        "X-XSS-Protection",
        "Referrer-Policy",
        "Permissions-Policy",
        "Cross-Origin-Resource-Policy",
        "Cross-Origin-Embedder-Policy"
    ]

    print("\n[+] Security Headers Check:")
    for header in important_headers:
        if header in headers:
            print(f"  [OK] {header}: {headers[header]}")
        else:
            print(f"  [MISSING] {header}")


def main():
    url = input("Enter the website URL: ").strip()
    headers = get_headers(url)

    if headers:
        print("\n[+] HTTP Response Headers:")
        for key, value in headers.items():
            print(f"{key}: {value}")

        check_security_headers(headers)
    else:
        print("[!] Failed to retrieve headers.")


if __name__ == "__main__":
    main()
