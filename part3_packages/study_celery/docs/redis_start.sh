#!/usr/bin/env bash
#!/bin/sh
#
# Simple Redis init.d script conceived to work on Linux systems
# as it does use of the /proc filesystem.
source /etc/init.d/functions
REDISPORT=6379
EXEC=/usr/local/bin/redis-server
CLIEXEC=/usr/local/bin/redis-cli

PIDFILE=/var/run/redis_${REDISPORT}.pid
CONF="/usr/local/redis/etc/redis.conf"
AUTH="123456"
BIND_IP='0.0.0.0'

start(){

    if [[ -f $PIDFILE ]]
    then
        echo "$PIDFILE exists, process is already running or crashed"
    else
        echo "Starting Redis server..."
        $EXEC $CONF
    fi
    if [[ "$?"="0" ]]
    then
        echo "Redis is running..."
    fi


}

stop(){

    if [[ ! -f $PIDFILE ]]
    then
        echo "$PIDFILE does not exist, process is not running"
    else
        PID=$(cat $PIDFILE)
        echo "Stopping ..."
        $CLIEXEC -h $BIND_IP -a $AUTH -p $REDISPORT  SHUTDOWN
        sleep 1
        while [[ -x /proc/${PID} ]]
        do
            echo "Waiting for Redis to shutdown ..."
            sleep 1
        done
            echo "Redis stopped"
    fi
}

restart(){
    stop
    start

}
status(){

    ps -ef|grep redis-server|grep -v grep >/dev/null 2>&1

    if [ $? -eq 0 ];then

        echo "redis server is running"

    else
        echo "redis server is stopped"

    fi


}


case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;

    restart)
        restart
        ;;

    status)
        status
        ;;
    *)

     echo "Usage: /etc/init.d/redis {start|stop|status|start}" >&2
     exit 1
esac
