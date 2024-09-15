# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"

# my solution:
import re
def domain_name(url):
    domain = re.search(r'(https?://)?(www\d?\.)?([^/]+)', url)
    domain_parts = domain.group(3).split('.')
    return domain_parts[0]