#!/usr/bin/env bash

shopt -s expand_aliases
set -ueo pipefail

SCRIPTPATH="$( cd "$( dirname "${BASH_SOURCE[0]}"  )" && pwd  )"
TOP="${SCRIPTPATH}"

# Environment variables
source ${SCRIPTPATH}/env-vars.sh
# Source common functions
source ${SCRIPTPATH}/functions.sh
# Get all repositories
source ${SCRIPTPATH}/repos.sh

# Common paths
IOC_REPOS=${TOP}/${IOC_REPO_DIR}
DEST_OPI_DIR=${TOP}/${OPI_DIR}

usage () {
    echo "Usage:" >&2
    echo "  $1 -f       [yes|no]" >&2
    echo >&2
    echo " Options:" >&2
    echo "  -f          Get full git repository [yes|no]" >&2
}

FULL_GIT_REPO="no"
while getopts ":f:" opt; do
  case $opt in
    f) FULL_GIT_REPO="$OPTARG" ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      usage $0
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      usage $0
      exit 1
      ;;
  esac
done

# if getopts did not process all input
if [ "$OPTIND" -le "$#" ]; then
    echo "Invalid argument at index '$OPTIND' does not have a corresponding option." >&2
    usage $0
    exit 1
fi

if [ "${FULL_GIT_REPO}" != "yes" ] && [ "${FULL_GIT_REPO}" != "no" ]; then
    echo "Invalid -f option. Available options are: \"yes\" or \"no\"" >&2
    exit 1
fi

alias get_repo='shallow_repo'
if [ "${FULL_GIT_REPO}" == "yes" ]; then
	alias get_repo='full_repo'
fi

# Create folders
mkdir -p ${IOC_REPOS}
mkdir -p ${DEST_OPI_DIR}

set +u

# Get repos
for proj in "${PROJECTS[@]}"; do
    _git_url="${proj}_GIT_URL"
    _git_org="${proj}_ORG"
    _git_proj="${proj}_PROJECT"
    _git_tag="${proj}_TAG"
    _opi_folder="${proj}_OPI_DIR"

    git_url=${!_git_url}
    git_org=${!_git_org}
    git_proj=${!_git_proj}
    git_tag=${!_git_tag}
    opi_folder=${!_opi_folder}

    dest_proj_name=$(dest_proj_name ${git_proj} ${git_tag})

    get_repo ${git_url} ${git_org} ${git_proj} ${git_tag} ${IOC_REPOS}

    # Copy only OPI to target folder
    mkdir -p ${DEST_OPI_DIR}/${git_proj}
    cp -r ${IOC_REPOS}/${dest_proj_name}/${opi_folder}/* \
        ${DEST_OPI_DIR}/${git_proj}
done

# Get repos
for proj in "${TOP_PROJECTS[@]}"; do
    _git_url="${proj}_GIT_URL"
    _git_org="${proj}_ORG"
    _git_proj="${proj}_PROJECT"
    _git_tag="${proj}_TAG"
    _opi_folder="${proj}_OPI_DIR"

    git_url=${!_git_url}
    git_org=${!_git_org}
    git_proj=${!_git_proj}
    git_tag=${!_git_tag}
    opi_folder=${!_opi_folder}

    DEST_PROJ_NAME=$(dest_proj_name ${git_proj} ${git_tag})

    # Copy only OPI to target folder
    mkdir -p ${DEST_OPI_DIR}/${git_proj}
    cp -r ${TOP}/${opi_folder}/* \
        ${DEST_OPI_DIR}
done

set -u
