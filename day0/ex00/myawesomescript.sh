#!/bin/bash

curl -s $1 | grep -w href | cut -d '"' -f2