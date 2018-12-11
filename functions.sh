#!/usr/bin/env bash

set -ueo pipefail

dest_proj_name()
{
    PROJECT_NAME=$1
    TAG=$2

    DEST_PROJ_NAME=${PROJECT_NAME}

    echo ${DEST_PROJ_NAME}
}

get_repo()
{
    GIT_URL=$1
    GIT_ORG=$2
    PROJECT_NAME=$3
    TAG=$4
    DEST_DIR=$5
    TYPE=$6

    DEST_PROJ_NAME=$(dest_proj_name ${PROJECT_NAME} ${TAG})
    FULL_GIT_URL=${GIT_URL}/${GIT_ORG}/${PROJECT_NAME}
    DEST=${DEST_DIR}/${DEST_PROJ_NAME}

    # Do git submodule init/update if not available
    if [ -z "$(find ${DEST} -type d -name ".git" 2>/dev/null)" ]; then
        if [  "${TYPE}" == "shallow" ]; then
            echo "Grabbing ${PROJECT_NAME} \"shallow\" repository at tag: ${TAG}"
            git clone -q --branch ${TAG} --depth 1 ${FULL_GIT_URL} ${DEST}
        elif [  "${TYPE}" == "full" ]; then
            echo "Grabbing ${PROJECT_NAME} \"full\" repository at tag: ${TAG}"
            git clone -q ${FULL_GIT_URL} ${DEST}
            ( \
                cd ${DEST} && \
                git checkout -q ${TAG}
            )
        fi
    else
        echo "Repository ${PROJECT_NAME} already exists. Updating the current one to tag: ${TAG}"
        ( \
            cd ${DEST} && \
            git fetch -q --all && \
            git checkout -q ${TAG} && \
            git reset -q --hard origin/${TAG}
        )
    fi
}


shallow_repo()
{
    get_repo "${@:1:5}" "shallow"
}

full_repo()
{
    get_repo "${@:1:5}" "full"
}
