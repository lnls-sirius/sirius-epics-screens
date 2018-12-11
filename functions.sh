#!/usr/bin/env bash

set -ueo pipefail

dest_proj_name()
{
    PROJECT_NAME=$1
    TAG=$2

    DEST_PROJ_NAME=${PROJECT_NAME}

    echo ${DEST_PROJ_NAME}
}

shallow_repo()
{
    GIT_URL=$1
    GIT_ORG=$2
    PROJECT_NAME=$3
    TAG=$4
    DEST_DIR=$5

    DEST_PROJ_NAME=$(dest_proj_name ${PROJECT_NAME} ${TAG})

    echo "Grabbing ${PROJECT_NAME} at tag: ${TAG}"

    git clone -q --branch ${TAG} --depth 1 ${GIT_URL}/${GIT_ORG}/${PROJECT_NAME} ${DEST_DIR}/${DEST_PROJ_NAME}
}

full_repo()
{
    GIT_URL=$1
    GIT_ORG=$2
    PROJECT_NAME=$3
    TAG=$4
    DEST_DIR=$5

    DEST_PROJ_NAME=$(dest_proj_name ${PROJECT_NAME} ${TAG})

    echo "Grabbing ${PROJECT_NAME} at tag: ${TAG}"

    git clone -q ${GIT_URL}/${GIT_ORG}/${PROJECT_NAME} ${DEST_DIR}/${DEST_PROJ_NAME}

    CURR=$(pwd)

    cd ${DEST_PROJ_NAME}
    git checkout -q ${TAG}
    cd "${CURR}"
}
