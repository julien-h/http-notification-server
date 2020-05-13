#!/usr/bin/env bash

curl \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{"title":"Hello!","description":"Notification sent with cURL."}' \
  http://127.0.0.1:8000/json \
  && echo "" # echo prints a new line in the terminal