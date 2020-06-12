import json
import os
# from Colors import bcolors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    Black= '\033[30m'
    Red= '\033[31m'
    Green= '\033[32m'
    Yellow= '\033[33m'
    Blue= '\033[34m'
    Magenta= '\033[35m'
    Cyan= '\033[36m'
    White= '\033[37m'
    Reset= '\033[0m'

# Get All services  
def get_services():
  directory = os.getcwd()+'/services/services.json'
  with open(directory, 'r') as json_file:
    data=json_file.read()

  obj = json.loads(data)
  services = obj["services"]
  return services

# Order list of groups
def order_groups(services):
  groups=[]
  for service in services:
    if not service["resourceGroup"] in groups:
      groups.append(str(service["resourceGroup"]))
    pass
  groups = sorted(groups)
  return groups

# Get name of group
def get_one_group(groupNumber):
  services = get_services()
  groups=order_groups(services)

  if groupNumber < 0 or groupNumber > len(groups):
    return {"Valid": False, "Message": "The number group does not exist"}
  else:
    return {"Valid": True, "groupName": groups[groupNumber], "Message": "ok"}


def print_services(services_by_group, group):
  print(bcolors.Cyan+" ResourceGroup: "+bcolors.ENDC+bcolors.BOLD+group+bcolors.ENDC)
  for index in range(len(services_by_group)):
    print(bcolors.Magenta +f"  {index} "+ bcolors.ENDC + bcolors.Yellow + services_by_group[index] + bcolors.ENDC)

def list_services(group):
  services = get_services()

  services_by_group = []
  for service in services:
    if service["resourceGroup"] == group:
      services_by_group.append(service["app"])
    pass

  services_by_group = sorted(services_by_group)
  return services_by_group

# Get serrvice name
def get_one_service(groupName, serviceNumber):
  services = list_services(groupName)
  if serviceNumber < 0 or serviceNumber > len(services):
    return {"Valid": False, "Message": "Service not found"}
  else:
    return {"Valid": True, "serviceName":services[serviceNumber], "Message": "ok"}


def list_groups():
  services = get_services()
  groups = order_groups(services)

  for index in range(len(groups)):
    print(bcolors.Magenta +f"[{index}] "+ bcolors.ENDC + bcolors.Yellow + groups[index] + bcolors.ENDC)
    pass
