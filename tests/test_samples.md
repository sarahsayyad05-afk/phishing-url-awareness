# Test Results

Python version used: 3.13 | Operating system: Windows | Date: 30-10-2026

| # | Input | Expected result | Actual result | Pass/Fail |
|---|-------|-----------------|---------------|-----------|
| 1 | `https://www.example.com/login` | No listed warning signs | No listed warning signs found. This does NOT prove safety. | PASS |
| 2 | `http://192.0.2.10/account` | IP address + HTTP | Uses an IP address instead of a familiar domain. + Uses HTTP. HTTPS alone does not prove trust. (REVIEW CAREFULLY: 2 warning sign(s)) | PASS |
| 3 | `http://example.com@sample.invalid/login` | @ symbol + HTTP | Contains an @ symbol; inspect carefully. + Uses HTTP. HTTPS alone does not prove trust. (REVIEW CAREFULLY: 2 warning sign(s)) | PASS |
| 4 | `https://a.b.c.d.e.example.invalid/path` | Many hostname segments | Contains many hostname segments/subdomains. (REVIEW CAREFULLY: 1 warning sign(s)) | PASS |
| 5 | `https://xn--example.invalid/` | Punycode-style hostname | Contains a punycode-style hostname. (REVIEW CAREFULLY: 1 warning sign(s)) | PASS |

## Bonus checks

| Input | Result |
|-------|--------|
| (just pressed Enter) | No URL entered. |
| www.example.com | Uses HTTP. HTTPS alone does not prove trust. |
| https://secure-login.example.invalid | No listed warning signs found. This does NOT prove safety. |
| http://[bad | This text is not a valid URL format. (no crash after improvement C) |

## Notes

I learned that the tool only reads the text and never opens the link. What surprised me was that secure-login.example.invalid got no warnings even though the name looks fishy, so no warning really doesnt mean safe. Also www.example.com with no https:// showed the HTTP warning because the code adds http:// by itself.
