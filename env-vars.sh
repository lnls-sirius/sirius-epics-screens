#!/usr/bin/env bash

set -ue

SCRIPTPATH="$( cd "$( dirname "${BASH_SOURCE[0]}"  )" && pwd  )"

# Build folder
BUILD_DIR="build"

# EPICS IOC screens folder
IOC_REPO_DIR=${BUILD_DIR}/"epics-iocs"

# EPICS target OPI folder
OPI_DIR=${BUILD_DIR}/"op/opi"
