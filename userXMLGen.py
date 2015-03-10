import sys

def check_file(in_file):

    summary = '<?xml version="1.0" encoding="UTF-8"?>' + '\n'
    summary += '<person-mappings xmlns="http://tasktop.com/xml/ns/sync/person-mapping-model">' + '\n\n'
    summary += '    <repository url="https://pht.jamacloud.com" mapping-ignore-case="false" default-person-id="jamasync"/>' + '\n'
    summary += '    <repository url="https://phtcorp.atlassian.net" mapping-ignore-case="false" default-person-id="jirasync"/>' + '\n\n'
    with open(in_file, "r") as f:
        for line in f:
            user = line.replace('\n', '').split(',')
            summary += '    <person-mapping>' + '\n'
            summary += '        <person id="%s" />' % user[1] + '\n'
            summary += '        <person id="%s" />' % user[2] + '\n'
            summary += '    </person-mapping>' + '\n'

    summary += '\n' + '</person-mappings>'
    print summary
            
  
if __name__ == "__main__":

	in_file       = sys.argv[1]
	check_file(in_file)

    
