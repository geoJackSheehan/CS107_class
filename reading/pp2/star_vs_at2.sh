echo "-- \"\$*\" "
for i in "$*"; do
 echo $i
done

echo "-- \"\$@\" "
for i in "$@"; do
 echo $i
done

echo "-- \$* æ"
for i in $*; do
 echo $i
done

echo "-- \$@"
for i in $@; do
 echo $i
done
