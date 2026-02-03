import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from core.colors import Colors
import time

def detect_parameters(url):
    """
    Parses the URL and returns a dictionary of query parameters.
    Returns None if no parameters are found.
    """
    parsed = urlparse(url)
    params = parse_qs(parsed.query)
    if not params:
        return None
    return params

def inject_payload(url, param_name, payload):
    """
    Injects a payload into a specific parameter of the URL.
    Returns the new URL.
    """
    parsed = urlparse(url)
    params = parse_qs(parsed.query)
    
    # parse_qs 'value' is a list, we replace it with our payload
    # We want to replace the FIRST value or ALL? Usually XSS affects one.
    # scan_url updates specific param.
    
    params[param_name] = [payload] 
    
    # Rebuild query string
    # doseq=True handles lists correctly, but we want ?param=payload not ?param=['payload']
    # parse_qs returns e.g. {'q': ['search']}
    # We set params['q'] = [payload]
    # urlencode check:
    encoded_query = urlencode(params, doseq=True)
    
    new_parts = list(parsed)
    new_parts[4] = encoded_query
    return urlunparse(new_parts)

def scan_target(urls, payloads):
    """
    Main scanning function.
    Iterates through URLs and Payloads.
    """
    vulnerabilities = []
    total_payloads_tested = 0
    start_time = time.time()
    
    print()
    Colors.print_info(f"Starting scan on {len(urls)} URLs with {len(payloads)} payloads...")
    print("-" * 50)

    for url in urls:
        params = detect_parameters(url)
        if not params:
            Colors.print_warning(f"No parameters found in: {url}")
            continue
            
        Colors.print_info(f"Scanning parameters in: {url}")
        
        for param in params.keys():
            for payload in payloads:
                total_payloads_tested += 1
                target_url = inject_payload(url, param, payload)
                
                # Show progress (overwrite line to keep clean)
                print(f"\r{Colors.BLUE}[~] Testing: {param} with payload: {payload}...{Colors.RESET}", end="", flush=True)
                
                try:
                    response = requests.get(target_url, timeout=5)
                    
                    # Detection Logic: Exact payload in response unencoded
                    if payload in response.text:
                        print() # Clear the progress line
                        Colors.print_success(f"[VULNERABLE] {target_url}")
                        vulnerabilities.append({
                            'url': target_url,
                            'payload': payload,
                            'param': param
                        })
                        
                except requests.exceptions.Timeout:
                     # print()
                     # Colors.print_error(f"Timeout scanning {url}")
                     pass
                except requests.exceptions.RequestException as e:
                     # print()
                     # Colors.print_error(f"Error scanning {url}: {e}")
                     pass
        print() # Newline after finishing parameters for a URL

    print("-" * 50)
    Colors.print_info("Scan completed!")
    print(f"Total payloads tested : {total_payloads_tested}")
    print(f"Total URLs scanned    : {len(urls)}")
    print(f"XSS vulnerabilities   : {len(vulnerabilities)}")
    
    if vulnerabilities:
        print()
        Colors.print_warning("Vulnerabilities Found:")
        for v in vulnerabilities:
             print(f"{Colors.RED}[VULNERABLE] {v['url']}{Colors.RESET}")
    else:
        Colors.print_success("No vulnerabilities found.")

