#Load Testing Script 


from urllib.request import urlopen
from collections import Counter
import argparse


def get_args():
	parser = argparse.ArgumentParser(description='Script runs requests against given server n number of times')

	# argument options
    parser.add_argument('-u', '--url', type=str, help="URL to connect to" required = True)
    parser.add_argument('-r','--requests', type=int, required = True, help="Number of requests to make")

    # array for all arguments passed to script
	args = parser.parse_args() 

    #assigning arguments to variables
	requests = args.requests
	url = args.url

    # return variable values
	return requests, url

# assigning the return values from get_args() to their respective variables
requests, url = get_args()
output = []	                     # Empty list

print
for i in range(requests):
        response = urlopen (url)     # Make the requests
        host = response.read()       # Read the response
        host = host.rstrip('\n')     # Remove new lines
        output.append(host)          # Append each response to list

counted_output = Counter(output)          # Count the number of hosts and occurrences of each host
print
print "Making sure loadbalancing is working. Should get an even number of hits on each node"
print
for host in sorted(counted_output):       # Loop through the sorted list
	print "%s: %s" % (host, counted_output[host])  # Pretty printing of the list
