
tr -s '[:space:]' '\n' < words.txt | sort | uniq -c | sort -rn | awk '{print $2, $1}'
