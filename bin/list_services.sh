#!/bin/bash
PWD="$(pwd)"
function getServicesList(){
  color='\033[94m'
  ENDC='\033[0m'
  echo "$color Resouces Group: $ENDC"
  VAR="$(az webapp list --query "[].{host: defaultHostName, state: state, app: repositorySiteName, resourceGroup: resourceGroup}")"
  echo "{\"services\":$VAR}" > $PWD/services/services.json
}
DIR="$PWD/services/"
if [ -d "$DIR" ]; then
  getServicesList
else 
  # echo "Error: ${DIR} not found. Can not continue."
  mkdir $PWD/services
  getServicesList
  exit 0
fi


# VAR="$(az webapp list --query "[].{host: defaultHostName, state: state, app: repositorySiteName, resourceGroup: resourceGroup}")"
# echo "{\"services\":$VAR}" > /Users/josueandres/Desktop/MyProjects/CLI_/cli/services/services.json
# echo "{\"services\":$VAR}" > /usr/local/Cellar/