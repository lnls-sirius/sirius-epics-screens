#!/usr/bin/env bash

shopt -s expand_aliases
set -ueo pipefail

SCRIPTPATH="$( cd "$( dirname "${BASH_SOURCE[0]}"  )" && pwd  )"
TOP="${SCRIPTPATH}"

# Source common functions
source ${SCRIPTPATH}/functions.sh
# Get all repositories
source ${SCRIPTPATH}/repos.sh

contains_element () {
  local e match="$1"
  shift
  for e; do [[ "$e" == "$match" ]] && return 0; done
  return 1
}

usage () {
    echo "Usage:" >&2
    echo "  $1 -p       [\"all\", \"general\", \"top\", \"merge\""
    echo "                          or specify a specific project name]" >&2
    echo >&2
    echo " Options:" >&2
    echo "  -h          Display help message" >&2
    echo "  -f          Get full git repository [yes|no]" >&2
    echo "  -b          Specify build directory <directory name>" >&2
    echo "  -r          Specify IOCs target repository <directory name>." >&2
    echo "                Defaults to <BUILD_DIR>/epics-iocs" >&2
    echo "  -o          Specify OPIs target directory <directory name>." >&2
    echo "                Defaults to <BUILD_DIR>/op/opi" >&2
    echo "  -p          Project name to update OPIs [\"all\", \"general\", \"top\", \"merge\""
    echo "                  or specify a specific project name]" >&2
}

FULL_GIT_REPO="no"
BUILD_DIR="build"
IOC_REPO_DIR_REL="epics-iocs"
OPI_DIR_REL="op/opi"
IOC_REPO_DIR="${TOP}/${BUILD_DIR}/${IOC_REPO_DIR_REL}"
OPI_DIR="${TOP}/${BUILD_DIR}/${OPI_DIR_REL}"
BUILD_DIR_SET=0
IOC_REPO_DIR_SET=0
OPI_DIR_SET=0
while getopts ":f:b:r:o:p:h" opt; do
  case $opt in
    f) FULL_GIT_REPO="$OPTARG" ;;
    b)
        __BUILD_DIR="$OPTARG"
        BUILD_DIR_SET=1
      ;;
    r)
        __IOC_REPO_DIR="$OPTARG"
        IOC_REPO_DIR_SET=1
      ;;
    o)
        __OPI_DIR="$OPTARG"
        OPI_DIR_SET=1
      ;;
    p) SPEC_PROJECT="$OPTARG" ;;
    h)
      usage $0
      exit 1
      ;;
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

set +u
if [ -z "${SPEC_PROJECT}" ]; then
    echo "Invalid -p option. Cannot be empty. Choose: \"all\" or \"<project name>\"" >&2
    exit 1
fi
set -u

# Set new repo relative to BUILD_DIR
if [ "${BUILD_DIR_SET}" -eq 1 ]; then
    BUILD_DIR="${__BUILD_DIR}"
    IOC_REPO_DIR="${BUILD_DIR}/${IOC_REPO_DIR_REL}"
    OPI_DIR="${BUILD_DIR}/${OPI_DIR_REL}"
fi

if [ "${IOC_REPO_DIR_SET}" -eq 1 ]; then
    IOC_REPO_DIR="${__IOC_REPO_DIR}"
fi

if [ "${OPI_DIR_SET}" -eq 1 ]; then
    OPI_DIR="${__OPI_DIR}"
fi

alias get_repo='shallow_repo'
if [ "${FULL_GIT_REPO}" == "yes" ]; then
	alias get_repo='full_repo'
fi

# Common paths. Only if not set overriden by the above
DEST_REPO_DIR=${IOC_REPO_DIR}
DEST_OPI_DIR=${OPI_DIR}

# Create folders
mkdir -p ${DEST_REPO_DIR}
mkdir -p ${DEST_OPI_DIR}

set +u

UPDATE_PROJECTS="no"
UPDATE_TOP_PROJECTS="no"
UPDATE_MERGE_PROJECTS="no"
LOCAL_PROJECTS=()
LOCAL_TOP_PROJECTS=()
LOCAL_MERGE_PROJECTS=()
# Filter name repos according to command line
case "${SPEC_PROJECT}" in
    [Aa][Ll][Ll])
        echo "Updating all projects"
        UPDATE_PROJECTS="yes"
        LOCAL_PROJECTS=("${PROJECTS[@]}")
        UPDATE_TOP_PROJECTS="yes"
        LOCAL_TOP_PROJECTS=("${TOP_PROJECTS[@]}")
        UPDATE_MERGE_PROJECTS="yes"
        LOCAL_MERGE_PROJECTS=("${MERGE_PROJECTS[@]}")
        ;;
    [Gg][En][Nn][Ee][Rr][Aa][Ll])
        echo "Updating only General projects"
        UPDATE_PROJECTS="yes"
        LOCAL_PROJECTS=("${PROJECTS[@]}")
        UPDATE_TOP_PROJECTS="no"
        UPDATE_MERGE_PROJECTS="no"
        ;;
    [Tt][Oo][Pp])
        echo "Updating only TOP projects"
        UPDATE_PROJECTS="no"
        UPDATE_TOP_PROJECTS="yes"
        LOCAL_TOP_PROJECTS=("${TOP_PROJECTS[@]}")
        UPDATE_MERGE_PROJECTS="no"
        ;;
    [Mm][Ee][Rr][Gg][Ee])
        echo "Updating only MERGE projects"
        UPDATE_PROJECTS="no"
        UPDATE_TOP_PROJECTS="no"
        UPDATE_MERGE_PROJECTS="yes"
        LOCAL_MERGE_PROJECTS=("${MERGE_PROJECTS[@]}")
        ;;
    *)
        if $(contains_element "${SPEC_PROJECT}" "${PROJECTS[@]}") ; then
            echo "Updating General project ${SPEC_PROJECT}"
            UPDATE_PROJECTS="yes"
            LOCAL_PROJECTS=("${SPEC_PROJECT}")
        elif $(contains_element "${SPEC_PROJECT}" "${TOP_PROJECTS[@]}") ; then
            echo "Updating only TOP project ${SPEC_PROJECT}"
            UPDATE_TOP_PROJECTS="yes"
            LOCAL_TOP_PROJECTS=("${SPEC_PROJECT}")
        elif $(contains_element "${SPEC_PROJECT}" "${MERGE_PROJECTS[@]}") ; then
            echo "Updating only MERGE project ${SPEC_PROJECT}"
            UPDATE_MERGE_PROJECTS="yes"
            LOCAL_MERGE_PROJECTS=("${SPEC_PROJECT}")
        else
            echo "Not updating any project. No match for project ${SPEC_PROJECT}"
            exit 0
        fi
        ;;
esac

# Get repos
if [ "${UPDATE_PROJECTS}" == "yes" ]; then
    echo "Updating general projects"

    [[ ! -z "${LOCAL_PROJECTS}" ]] && echo "Building target OPI directory with remote repositories"
    for proj in "${LOCAL_PROJECTS[@]}"; do
        copy_repo_opis ${proj} ${DEST_REPO_DIR} ${DEST_OPI_DIR}
    done
fi

# Get local repos
if [ "${UPDATE_TOP_PROJECTS}" == "yes" ]; then
    echo "Updating TOP projects"

    [[ ! -z "${LOCAL_TOP_PROJECTS}" ]] && echo "Building target OPI directory with local files"
    for proj in "${LOCAL_TOP_PROJECTS[@]}"; do
        copy_local_opis ${proj} ${TOP} ${DEST_OPI_DIR}
    done
fi

# Merge OPI folders
if [ "${UPDATE_MERGE_PROJECTS}" == "yes" ]; then
    echo "Updating MERGE projects"

    [[ ! -z "${LOCAL_MERGE_PROJECTS}" ]] && echo "Merging tagged projects into target OPI directory"
    for merge in "${LOCAL_MERGE_PROJECTS[@]}"; do
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
            # Copy source OPI into destination project
            copy_repo_opis_2_top ${proj} ${DEST_REPO_DIR} ${DEST_OPI_DIR}/${merge_dest_proj}
        done
    done
fi

if [ "${UPDATE_TOP_PROJECTS}" == "yes" ]; then
    # Copy .project file as CSS on NFS apparently needs it, as it's read-only
    echo "Copying .project file to OPI directory"
    copy_project_file ${TOP_PROJECTS[0]} ${TOP} ${DEST_OPI_DIR}
fi

set -u
