#!/bin/sh
while true; do
    if curl -f http://weather:8000 > /dev/null 2>&1; then
        echo "$(date): OK — приложение доступно"
    else
        echo "$(date): DOWN! — приложение не отвечает"
    fi
    sleep 60
done
