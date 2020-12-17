import boto3
import os
import sys
ec2 = boto3.client('ec2', region_name='us-east-1')
response = ec2.describe_security_groups()
ec2 = boto3.resource('ec2')
instances = ec2.instances.filter()
for instance in instances:
    for tag in instance.tags:
        if tag['Key'] == 'Name':
            intancetag = (tag['Value'])
    print('EC2 Nome: ', intancetag)
    print('EC2 ID: ', instance.id, '\n')
    for sg in range(len(instance.security_groups)):
        for i in response['SecurityGroups']:
            if i['GroupId'] == instance.security_groups[sg]['GroupId']:
                print("Security Group Name: "+i['GroupName'])
                print("Security Group ID: "+i['GroupId'])
                print("Regras de Entrada: ")
                for j in i['IpPermissions']:
                    try:
                        print("\nProtocolo IP: "+j['IpProtocol'] + ". Liberado da porta: " + str(
                            j['FromPort']) + ' até a porta ' + str(j['ToPort']))
                        for k in j['IpRanges']:
                            CidrIp = "{0:19}".format(k['CidrIp'])
                            print("     IP Ranges: "+CidrIp +
                                  ' |  Descrição: ', end='')
                            try:
                                print(k['Description'])
                            except Exception:
                                print(" ")
                                continue
                        try:
                            for k in j['Ipv6Ranges']:
                                CidrIpv6 = "{0:25}".format(k['CidrIpv6'])
                                print('     IPV6: ' + CidrIpv6 +
                                      '|  Descrição: ', end='')
                                try:
                                    print(k['Description'])
                                except Exception:
                                    print(" ")
                                continue
                        except Exception:
                            continue
                    except Exception:
                        print("\nProtocolo IP: " + j['IpProtocol'])
                        for k in j['IpRanges']:
                            CidrIp = "{0:19}".format(k['CidrIp'])
                            print("     IP Ranges: "+CidrIp +
                                  ' |  Descrição: ', end='')
                            try:
                                print(k['Description'])
                            except Exception:
                                print(" ")
                                continue
                        try:
                            for k in j['Ipv6Ranges']:
                                CidrIpv6 = "{0:25}".format(k['CidrIpv6'])
                                print('     IPV6: ' + CidrIpv6 +
                                      '|  Descrição: ', end='')
                                try:
                                    print(k['Description'])
                                except Exception:
                                    print(" ")
                                continue
                        except Exception:
                            continue
                        try:
                            for k in j['UserIdGroupPairs']:
                                print('\n     SG vinculado:')
                                print("     GroupID: " + k['GroupId'])
                                print("     UserID: " + k['UserId'])
                                try:
                                    print("     Descrição: " +
                                          k['Description'])
                                except Exception:
                                    print("     Descrição: ")
                        except Exception:
                            continue
                        continue
                print("------------------------------------------------------------")
    print("\n============================================================\n")
