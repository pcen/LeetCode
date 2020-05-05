current=$(find "." -iname "$1-*" | sort -n | tail -1)
echo "compiling" $current
g++ $current -std=c++17
