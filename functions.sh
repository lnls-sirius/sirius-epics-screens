#!/usr/bin/env bash

set -ueo pipefail

dest_proj_name()
{
    local PROJECT_NAME=$1
    local TAG=$2

    DEST_PROJ_NAME=${PROJECT_NAME}

    echo ${DEST_PROJ_NAME}
}

get_repo()
{
    local GIT_URL=$1
    local GIT_ORG=$2
    local PROJECT_NAME=$3
    local TAG=$4
    local DEST_DIR=$5
    local TYPE=$6

    local DEST_PROJ_NAME=$(dest_proj_name ${PROJECT_NAME} ${TAG})
    local FULL_GIT_URL=${GIT_URL}/${GIT_ORG}/${PROJECT_NAME}
    local DEST=${DEST_DIR}/${DEST_PROJ_NAME}

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


get_shallow_repo()
{
    get_repo "${@:1:5}" "shallow"
}

get_full_repo()
{
    get_repo "${@:1:5}" "full"
}

copy_opis()
{
    local SRC_OPI_PROJ_DIR=$1
    local DEST_OPI_PROJ_DIR=$2

    mkdir -p ${DEST_OPI_PROJ_DIR}
    cp -r ${SRC_OPI_PROJ_DIR}/* \
        ${DEST_OPI_PROJ_DIR}
}

copy_repo_opis()
{
    local PROJ_NAME=$1
    local DEST_REPO_DIR=$2
    DEST_OPI_DIR=$3

    local _git_url="${PROJ_NAME}_GIT_URL"
    local _git_org="${PROJ_NAME}_ORG"
    local _git_proj="${PROJ_NAME}_PROJECT"
    local _git_tag="${PROJ_NAME}_TAG"
    local _opi_folder="${PROJ_NAME}_OPI_DIR"

    local git_url=${!_git_url}
    local git_org=${!_git_org}
    local git_proj=${!_git_proj}
    local git_tag=${!_git_tag}
    local opi_folder=${!_opi_folder}

    # Get repo
    get_shallow_repo ${git_url} ${git_org} ${git_proj} ${git_tag} ${DEST_REPO_DIR}

    # Copy only OPI to target folder
    copy_opis "${DEST_REPO_DIR}/${git_proj}/${opi_folder}" "${DEST_OPI_DIR}/${git_proj}"
}

copy_local_opis()
{
    local PROJ_NAME=$1
    local DEST_REPO_DIR=$2
    local DEST_OPI_DIR=$3
    SRC_OPI_DIR=$4

    _git_url="${PROJ_NAME}_GIT_URL"
    _git_org="${PROJ_NAME}_ORG"
    _git_proj="${PROJ_NAME}_PROJECT"
    _git_tag="${PROJ_NAME}_TAG"
    _opi_folder="${PROJ_NAME}_OPI_DIR"

    git_url=${!_git_url}
    git_org=${!_git_org}
    git_proj=${!_git_proj}
    git_tag=${!_git_tag}
    opi_folder=${!_opi_folder}

    # Copy only OPI to target folder
    copy_opis "${SRC_OPI_DIR}/${opi_folder}" "${DEST_OPI_DIR}"
}
