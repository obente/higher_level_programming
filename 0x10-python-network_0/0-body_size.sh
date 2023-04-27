#!/bin/bash
# display size of body of response

curl -si $1 | grep Content-Length | cut -d " " -f 2
