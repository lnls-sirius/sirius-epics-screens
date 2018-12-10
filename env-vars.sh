#!/usr/bin/env bash

set -ue

SCRIPTPATH="$( cd "$( dirname "${BASH_SOURCE[0]}"  )" && pwd  )"

# Build folder
BUILD_FOLDER="build"

# EPICS IOC screens folder
IOC_REPO_FOLDER=${BUILD_FOLDER}/"epics-iocs"

# EPICS target OPI folder
OPI_FOLDER=${BUILD_FOLDER}/"op/opi"
