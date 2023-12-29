#!/bin/bash

rm -rf deployment_package.zip package
pip3 install --target ./package requests
cd package
zip -r ../deployment_package.zip .
cd ..
zip -g deployment_package.zip recovery_credentials.py