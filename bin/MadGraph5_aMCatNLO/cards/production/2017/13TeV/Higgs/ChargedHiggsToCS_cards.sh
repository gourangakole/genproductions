#!/bin/bash

masses=(80 90 120 130 140 150 160)

sample=ChargedHiggsToCS
postfix=(_run_card.dat _customizecards.dat _proc_card.dat)

#echo ${masses[*]}

# get length of an array
tLen=${#postfix[@]}

for mass in ${masses[*]}; do
    echo generating cards for M = $mass GeV

    for (( i=0; i<${tLen}; i++ )) do
        if [ ! -d ${sample}_M${mass} ]; then
            mkdir ${sample}_M${mass}
        fi
        sed "s/<MASS>/${mass}/g" ${sample}/${sample}${postfix[$i]} > ${sample}_M$mass/${sample}_M$mass${postfix[$i]}
    done  
done
