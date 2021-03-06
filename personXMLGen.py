import sys
import json
import subprocess
from pprint import pprint


def gen_xml_file(jira_user_data, jama_user_data):

    notinjira = ''
    summary = '<?xml version="1.0" encoding="UTF-8"?>' + '\n'
    summary += '<person-mappings xmlns="http://tasktop.com/xml/ns/sync/person-mapping-model">' + '\n\n'
    summary += '    <repository url="https://pht.jamacloud.com" mapping-ignore-case="false" default-person-id="jamasync"/>' + '\n'
    summary += '    <repository url="https://phtcorp.atlassian.net" mapping-ignore-case="false" default-person-id="jirasync"/>' + '\n\n'

    for j in jama_user_data:
        if j.get('userName') in jira_user_data:
            summary += '    <person-mapping>' + '\n'
            summary += '        <person id="%s" />' % j.get('id') + '\n'
            summary += '        <person id="%s" />' % j.get('userName') + '\n'
            summary += '    </person-mapping>' + '\n'
        else:
            notinjira += '%s' % j.get('userName') + '\n'

    summary += '\n' + '</person-mappings>'
    print summary
    syncfile=open('./personMapping.xml', 'w+')
    syncfile.write(summary)
    #print '\n\n\n'
    #print notinjira
    outfile=open('./notinjira.out', 'w+')
    outfile.write(notinjira)

            
  
if __name__ == "__main__":

    in_file_jama       = sys.argv[1]
    #in_file_jira       = sys.argv[2]
    
    # Prepare Jira data (input file method used before CLI)
    #jira_user_data = [line.strip() for line in open(in_file_jira, 'r')]
    #print jira_user_data

    jira_user_data = []
    jira_get_user_list = subprocess.Popen(["../../work/jira-cli-4.1.0/jira.sh", "--action", "getUserList", "--group", "jira-users"], stdout=subprocess.PIPE).communicate()[0]
    gen_list = jira_get_user_list.split("\n")
    for line in gen_list[+2:-2]:
        jira_user_data.append(line.split(",")[0].strip('"'))

    
    #Pepare Jama data from json file
    json_data=open(in_file_jama)
    jama_data = json.load(json_data)
    #print jama_data
    jama_user_data = jama_data["Body"]["getUsersResponse"]["return"]    
    #jama_user_data = jama_data["soap:Envelope"]["soap:Body"]["ns2:getUsersResponse"]["return"]    
    json_data.close()

    gen_xml_file(jira_user_data, jama_user_data)