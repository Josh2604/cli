bold='\033[1m'
color='\033[37m'
reset='\033[0m'
echo "$bold$color Running logs... $ENDC"
# echo "Command: az webapp log tail --name $1 --resource-group $2"
az webapp log tail --name $1 --resource-group $2