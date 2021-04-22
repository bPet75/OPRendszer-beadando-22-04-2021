#!/bin/bash

echo ""
echo "---PS5 megfigyelő program (by.: Benedek Péter)---"
echo "		A konzolvilag.hu adatai alapján		"
echo ""
echo "Leírás:"
echo "Kapcsolók nélkül is futtatható, ilyenkor minden adatot kiír"
echo "-t --> Kizárólag az idő kiírása"
echo "-d --> Csak a statisztika kiíratása"
echo "-f (formátum) --> Az idő formátumának megváltoztatása (SZÓKÖZ és PONTOSVESSZŐ nem megengedett!)"
echo "pl.: %b.%d.%Y,%H:%M:%S"
echo ""
wget konzolvilag.hu/playstation5/playstation-5-825gb -O weblap -q

#for param in $@
#do
#	if [[ $param == "-all" ]]
#	then
#		echo "a"
#	fi
#done

TIME="x"

while getopts 'tdf:' c
do
  case $c in
    t) ACTION="TIME" ;;
    d) ACTION="DIAG" ;;
    f) TIME=$OPTARG ;;
  esac
done


./Python.py $( cat weblap | grep 'Köszönjük mindenkinek, aki ellátogatott hozzánk és megrendelte a PS5-öt.' ) $ACTION $TIME
#./Python.py $( cat weblap | grep 'Köszönjük mindenkinek, aki ellátogatott hozzánk és megrendelte a PS5-öt.' )
rm weblap

