import os
import ipaddress

# get script directory
DIR = os.path.dirname(os.path.abspath(__file__)) if '__file__' in vars() else os.path.join(os.getcwd(), '')

# open ip ranges file
rangefile = open(os.path.join(DIR, 'range.txt'), 'r')

# open output file
networkfile = open(os.path.join(DIR, 'network.txt'), 'w')


lines = rangefile.readlines()
output = []

try:
    for idx, line in enumerate(lines):
        # print(line)
        line = line.strip()

        if line == '':
            continue
        elif '-' not in line:
            # print(line)
            output.append(line)
        else:
            parts = line.split('-')

            if len(parts) == 2:
                try:
                    start = ipaddress.ip_address(parts[0])
                    end = ipaddress.ip_address(parts[1])

                    summary = [ipaddr for ipaddr in
                               ipaddress.summarize_address_range(start, end)]
                    for network in summary:
                        # print(item)
                        output.append(network.__str__())

                except TypeError as err:
                    raise Exception('{0} Line: {1}'.format(idx, err))

                except ValueError as err:
                    raise Exception('{0} Line: {1}'.format(idx, err))
            else:
                raise Exception('{0} Line: is invalid format, it must include two ip address joined with - '.format(idx, line))

    networkfile.writelines('\n'.join(output))
    print(*output, sep='\n')

except Exception as err:
    print('Found Error, Please check your ip range format:')
    print('{0}'.format(err))
finally:
    rangefile.close()
    networkfile.close()


