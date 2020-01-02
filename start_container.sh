./start_celery.sh &
P1=$!
./start_django.sh &
P2=$!
wait $P1 $P2