#这是临时的记录,用到时候再调整
mkdir data
cd data
python ../1.py > lst.txt
aria2c -i lst.txt
rm lst.txt
python ../2_continue.py *.txt > continue.txt
python ../3_all.py *.txt > all.txt
