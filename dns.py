# Opalstack API settings
api_token = '123456789'  # Replace with your Opalstack API token
# Domain settings
domain_name = 'example.com'  # Replace with your domain name
import requests
import opalstack
# Initialize Opalstack API
opal = opalstack.Api(token=api_token)

def get_wan_ip():
    """
    Get the current WAN IP using a public API.
    """
    response = requests.get('https://api.ipify.org?format=json')
    return response.json()['ip']

def check_domain_in_list(domain_id, records_list):
    """
    Check if the given domain ID exists in the list of records.
    :param domain_id: The domain ID to search for.
    :param records_list: The list of records, each a dictionary.
    :return: True if the domain ID is found, False otherwise.
    """
    for record in records_list:
        if record['domain'] == domain_id:
            return record
    return False

def update_a_record(domain, ip_address):
    """
    Update the A record for the specified domain with the provided IP address.
    """
    domains = opal.domains.list_all()
    # Enhanced domain matching logic
    domain_id = None
    for d in domains:
        full_domain = d['name'].strip()
        if full_domain == domain.strip():
            domain_id = d['id']
            break

    if not domain_id:
        print(f"Domain '{domain}' not found.")
        return

    records = opal.dnsrecords.list_all()
    a_record = check_domain_in_list(domain_id, records)
    if not a_record:
        print(f"No A record found for '{domain}'. Creating one.")
        opal.dnsrecords.create(domain_id, 'A', ip_address, 600)
        print(f"A record created for IP {ip_address}")
    else:
        print(a_record['id'], ip_address)
        opal.dnsrecords.update_one({'id':a_record['id'], 'type':'A', 'content':ip_address, 'ttl':600})
        print(f"A record updated to IP {ip_address}")

# Main execution
current_ip = get_wan_ip()
update_a_record(domain_name, current_ip)
