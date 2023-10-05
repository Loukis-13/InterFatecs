cd $1

mkdir result

for i in $(seq 1 $(ls -1 input | wc -l)); do
    echo "### $i ###"
    python $1.py < input/$i.txt > result/$i.txt
    diff output/$i.txt result/$i.txt
done
