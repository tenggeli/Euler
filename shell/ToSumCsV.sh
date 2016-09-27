#!/bin/bash
#
i=0
for file in `ls *.csv`
do
     echo $file
     $(awk -F ',' -v OFS=',' '{print $27,$32,$33,$34,$35,$36}' "$file" >"$i"x.csv)
     $(ls "$i"x.csv | xargs -I {} sh -c "iconv -f gbk -t utf-8 {} > utf8_{}")
     amount=$(awk -F "," ' $1 != "是" {  sum += $2} END { printf "%.2f\n", sum }' utf8_"$i"x.csv);
     echo '         amount:' $amount
     capital=$(awk -F "," ' $1 != "是" {  sum += $3} END { printf "%.2f\n", sum }' utf8_"$i"x.csv);
     echo '         capital:' $capital
     inters=$(awk -F "," ' $1 != "是" {  sum += $4} END { printf "%.2f\n", sum }' utf8_"$i"x.csv);
     echo '         inters:'  $inters
     over_due=$(awk -F "," ' $1 != "是" {  sum += $5} END { printf "%.2f\n", sum }' utf8_"$i"x.csv);
     echo '         over_due:' $over_due
     overflow=$(awk -F "," ' $1 != "是" {  sum += $6} END { printf "%.2f\n", sum }' utf8_"$i"x.csv);
     echo '         overflow:' $overflow
done
