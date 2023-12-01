#!/bin/bash
# Sends a JSON POST request
curl -sX POST -d "$(cat "$2")" "$1"
