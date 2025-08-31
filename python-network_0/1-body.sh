#!/bin/bash
# Sends a GET request to the URL and displays the body only if the status code is 200
curl -s -o /dev/stdout -w "%{http_code}" "$1" | {
    read -r body
    code="${body: -3}"
    content="${body::-3}"
    [ "$code" = "200" ] && echo -n "$content"
}
