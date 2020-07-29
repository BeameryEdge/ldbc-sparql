. ../env_vars.sh
echo $RDF_DATA_DIR
sed "s|SRC|"${RDF_DATA_DIR}"|g" load.tmp.sql > load.tmp.2
sed "s|SFACTOR|"${SFACTOR}"|g" load.tmp.2 > load.sql
rm load.tmp.2

echo "\nPreparing for bulk loading...\n"
"${VIRTUOSO_HOME}"/bin/isql 1111 dba dba exec="LOAD load.sql"

STARTTIME=$(date +%s)
echo "\nBulk loading started...\n"

for (( i=1; i<=$VIRTUOSO_LOADERS; i++ ))
do
	"${VIRTUOSO_HOME}"/bin/isql 1111 dba dba exec="rdf_loader_run();" & 
done

wait 
"${VIRTUOSO_HOME}"/bin/isql 1111 dba dba exec="checkpoint;" 

ENDTIME=$(date +%s)
LOADTIME=$((ENDTIME - STARTTIME))
echo "Loading time: ${LOADTIME} s"
