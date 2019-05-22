set timeout -1
spawn docker-compose logs -f
expect "INFO success: postfix entered RUNNING state, process has stayed up for > than 1 seconds (startsecs)"
close $spawn_id
