#!/bin/bash
# Displays the status code
curl -sw "%{response_code}" -o /dev/null "$1"
