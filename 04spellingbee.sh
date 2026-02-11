ln -s ~/Code/MCB185/data/dictionary.gz ./dic.gz
gunzip -c dic.gz |grep -E "^.{4,}$"| grep -E "r"|grep -E ^[oznraic]+$
gunzip -c dic.gz |grep -E "^.{4,}$"| grep -E "r"|grep -E ^[oznraic]+$|wc -l
rm dic.gz
