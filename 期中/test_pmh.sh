# ./test_pmh.sh
python test_pmh.py --dim 2 > output/output_dim2_test.txt 2>&1
python test_pmh.py --dim 10 > output/output_dim10_test.txt 2>&1
python test_pmh.py --dim 30 > output/output_dim30_test.txt 2>&1