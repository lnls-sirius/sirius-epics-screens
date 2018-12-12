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
DEST_REPO_DIR=${TOP}/${IOC_REPO_DIR}
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
mkdir -p ${DEST_REPO_DIR}
mkdir -p ${DEST_OPI_DIR}

set +u

# Get repos
for proj in "${PROJECTS[@]}"; do
    copy_repo_opis ${proj} ${DEST_REPO_DIR} ${DEST_OPI_DIR}
done

# Get local repos
for proj in "${TOP_PROJECTS[@]}"; do
    copy_local_opis ${proj} ${TOP} ${DEST_OPI_DIR}
done

# Merge OPI folders
for merge in "${MERGE_PROJECTS[@]}"; do
    _merge_repos_prefix="${merge}_REPOS_PREFIX[@]"
    _merge_dest_prefix="${merge}_DEST_PREFIX"

    merge_repos_prefix=(${!_merge_repos_prefix})
    merge_dest_prefix=${!_merge_dest_prefix}

    _merge_dest_opi_dir="${merge_dest_prefix}_OPI_DIR"
    _merge_dest_proj="${merge_dest_prefix}_PROJECT"
    merge_dest_opi_dir="${!_merge_dest_opi_dir}"
    merge_dest_proj="${!_merge_dest_proj}"

    # Get repos
    for proj in "${merge_repos_prefix[@]}"; do
        # Get repo
        copy_repo ${proj} ${DEST_REPO_DIR}

        # Copy source OPI into destination project
        copy_repo_opis_2_top ${proj} ${DEST_REPO_DIR} ${DEST_OPI_DIR}/${merge_dest_proj}
    done
done

set -u
