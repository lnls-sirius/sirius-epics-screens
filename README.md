# Sirius Diagnostics EPICS Screens

Sirius EPICS IOC Screens for Diagnostics

## Description

This repository acts like a reference point for all
diagnostics screens used for Sirius.

## Usage

```bash
./get-opis.sh -f [yes|no]
```

where the options are:

- `-f   [yes|no]`:        Get full git repository or not (optional)

## Tip

It's possible to open CSS with the Main OPI being opened via the command-line with

```bash
<CSS executable> -data <path_to_workspace> -share_link <path_to_shared_directory>=/<directory_in_workspace> --launcher.openFile "/<directory_in_workspace>/<OPI>.opi"
```

Example:

```bash
./cs-studio/css -data /home/lerwys/workspace-share -share_link /home/lerwys/workspace/diagnostics=/displays --launcher.openFile "/displays/sirius_main_all.opi
```
