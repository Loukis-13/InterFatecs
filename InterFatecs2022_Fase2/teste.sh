cd $1

for i in $(seq 1 $(ls -1 input | wc -l)); do
    python $1.py < input/$i.txt > result/$i.txt

    echo $i
    diff output/$i.txt result/$i.txt
done