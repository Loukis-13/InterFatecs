DESAFIO=$1

if [[ -z "$DESAFIO" ]]; then
    echo 'É necessário informar o desafio'
    exit 1
fi

cd $DESAFIO

echo TESTANDO

time (
    for i in $(seq 1 $(ls -1 input | wc -l)); do
        python $DESAFIO.py < input/$i.txt > result/$i.txt
    done
)

echo VALIDANDO

for i in $(seq 1 $(ls -1 input | wc -l)); do
    echo $i
    diff output/$i.txt result/$i.txt
done
