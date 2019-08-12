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
    local DEST_PROJECT_NAME=$6
    local TYPE=$7

    local DEST_PROJ_NAME=$(dest_proj_name ${DEST_PROJECT_NAME} ${TAG})
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
        echo "Repository ${DEST_PROJECT_NAME} already exists. Updating the current one to tag: ${TAG}"
        ( \
            cd ${DEST} && \
            git remote set-branches origin "${TAG}"
            git fetch -q --all && \
            git checkout -q ${TAG} && \
            git reset -q --hard origin/${TAG}
        )
    fi
}


get_shallow_repo()
{
    get_repo "${@:1:6}" "shallow"
}

get_full_repo()
{
    get_repo "${@:1:6}" "full"
}

copy_and_create_dest()
{
    local SRC_OPI_PROJ_DIR=$1
    local DEST_OPI_PROJ_DIR=$2

    mkdir -p ${DEST_OPI_PROJ_DIR}
    cp -r ${SRC_OPI_PROJ_DIR}/* \
        ${DEST_OPI_PROJ_DIR}
}

simple_copy()
{
    local SRC_OPI_PROJ_DIR=$1
    local DEST_OPI_PROJ_DIR=$2
    local SRC_FILE=$3

    cp ${SRC_OPI_PROJ_DIR}/${SRC_FILE} \
        ${DEST_OPI_PROJ_DIR}
}

copy_opis()
{
    local PROJ_NAME=$1
    local BASE_DIR=$2
    local DEST_OPI_DIR=$3
    local COPY_TYPE=$4

    local _git_url="${PROJ_NAME}_GIT_URL"
    local _git_org="${PROJ_NAME}_ORG"
    local _git_proj="${PROJ_NAME}_PROJECT"
    local _git_tag="${PROJ_NAME}_TAG"
    local _opi_folder="${PROJ_NAME}_OPI_DIR"
    local _dest_project_name="${PROJ_NAME}_DEST_PROJECT_NAME"

    local git_url=${!_git_url}
    local git_org=${!_git_org}
    local git_proj=${!_git_proj}
    local git_tag=${!_git_tag}
    local opi_folder=${!_opi_folder}
    local dest_project_name=""

    # This can be empty
    if [ -v "${_dest_project_name}" ]; then
        dest_project_name=${!_dest_project_name}
    fi

    if [ -z ${dest_project_name} ]; then
        dest_project_name=${git_proj}
    fi

    if [ "${COPY_TYPE}" == "raw" ]; then
        copy_and_create_dest "${BASE_DIR}" "${DEST_OPI_DIR}"
    elif [ "${COPY_TYPE}" == "remote_project" ]; then
        copy_and_create_dest "${BASE_DIR}/${dest_project_name}/${opi_folder}" "${DEST_OPI_DIR}/${dest_project_name}"
    elif [ "${COPY_TYPE}" == "remote_project_raw" ]; then
        copy_and_create_dest "${BASE_DIR}/${dest_project_name}/${opi_folder}" "${DEST_OPI_DIR}"
    elif [ "${COPY_TYPE}" == "local_project" ]; then
        copy_and_create_dest "${BASE_DIR}/${opi_folder}" "${DEST_OPI_DIR}"
    else
        copy_and_create_dest "${BASE_DIR}" "${DEST_OPI_DIR}"
    fi
}

copy_project()
{
    local PROJ_NAME=$1
    local BASE_DIR=$2
    local DEST_OPI_DIR=$3

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

    simple_copy "${BASE_DIR}/${opi_folder}" "${DEST_OPI_DIR}" ".project"
}

copy_repo()
{
    local PROJ_NAME=$1
    local DEST_REPO_DIR=$2

    local _git_url="${PROJ_NAME}_GIT_URL"
    local _git_org="${PROJ_NAME}_ORG"
    local _git_proj="${PROJ_NAME}_PROJECT"
    local _git_tag="${PROJ_NAME}_TAG"
    local _opi_folder="${PROJ_NAME}_OPI_DIR"
    local _dest_project_name="${PROJ_NAME}_DEST_PROJECT_NAME"

    local git_url=${!_git_url}
    local git_org=${!_git_org}
    local git_proj=${!_git_proj}
    local git_tag=${!_git_tag}
    local opi_folder=${!_opi_folder}
    local dest_project_name=""

    # This can be empty
    if [ -v "${_dest_project_name}" ]; then
        dest_project_name=${!_dest_project_name}
    fi

    if [ -z ${dest_project_name} ]; then
        dest_project_name=${git_proj}
    fi

    # Get repo
    get_shallow_repo ${git_url} ${git_org} ${git_proj} ${git_tag} ${DEST_REPO_DIR} ${dest_project_name}
}

copy_repo_opis()
{
    local PROJ_NAME=$1
    local DEST_REPO_DIR=$2
    local DEST_OPI_DIR=$3

    # Get repo
    copy_repo ${PROJ_NAME} ${DEST_REPO_DIR}

    # Copy only OPI to target folder
    copy_opis ${PROJ_NAME} ${DEST_REPO_DIR} ${DEST_OPI_DIR} "remote_project"
}

copy_repo_opis_2_top()
{
    local PROJ_NAME=$1
    local DEST_REPO_DIR=$2
    local DEST_OPI_DIR=$3

    # Get repo
    copy_repo ${PROJ_NAME} ${DEST_REPO_DIR}

    # Copy only OPI to target folder
    copy_opis ${PROJ_NAME} ${DEST_REPO_DIR} ${DEST_OPI_DIR} "remote_project_raw"
}

copy_local_opis()
{
    local PROJ_NAME=$1
    local DEST_REPO_DIR=$2
    local DEST_OPI_DIR=$3

    # Copy only OPI to target folder
    copy_opis ${PROJ_NAME} ${DEST_REPO_DIR} ${DEST_OPI_DIR} "local_project"
}

copy_project_file()
{
    local PROJ_NAME=$1
    local DEST_REPO_DIR=$2
    local DEST_OPI_DIR=$3

    # Copy only OPI to target folder
    copy_project ${PROJ_NAME} ${DEST_REPO_DIR} ${DEST_OPI_DIR}
}
