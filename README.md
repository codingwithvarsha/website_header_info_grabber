# 🔐 HTTP Security Header Checker

A lightweight Python script to fetch and analyze HTTP response headers from any website, with a focus on identifying missing or misconfigured **security headers**.

---

## 🚀 Features

-  Automatically adds `https://` if missing from user input
-  Uses `HEAD` requests for speed, falls back to `GET` if needed
-  Checks for common security headers like:
  - `Content-Security-Policy`
  - `Strict-Transport-Security`
  - `X-Frame-Options`
  - `Permissions-Policy`
  - ...and more
-  Helps assess basic security posture of web servers
-  Clear CLI output with `[OK]` and `[MISSING]` tags

---

## 📦 Requirements

- Python 3.x
- `requests` library

Install dependencies using:

```bash
pip install requests
