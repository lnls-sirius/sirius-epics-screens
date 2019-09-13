# Sirius Diagnostics EPICS Screens

Sirius EPICS IOC Screens

## Description

This repository acts like a reference point for all
CSS screens used for Sirius.

## Usage

```bash
./get-opis.sh -p [all|general|merge|top|<project_name>]
```

where the options are:

```bash
  -h          Display help message
  -f          Get full git repository [yes|no]
  -b          Specify build directory <directory name>
  -r          Specify IOCs target repository <directory name>.
                Defaults to <BUILD_DIR>/epics-iocs
  -o          Specify OPIs target directory <directory name>.
                Defaults to <BUILD_DIR>/op/opi
  -p          Project name to update OPIs ["all", "general", "top", "merge"
                  or specify a specific project name]
```

## Tip

It's possible to open CSS with the Main OPI being opened via the command-line with

```bash
<CSS executable> \
    -data <path_to_workspace> \
    -share_link <path_to_shared_directory>=/<directory_in_workspace> \
    --launcher.openFile "/<directory_in_workspace>/<OPI>.opi"
```

Example:

```bash
./cs-studio/css \
    -data /home/lerwys/workspace-share \
    -share_link /home/lerwys/Repos/sirius-screens/build/op/opi=/displays \
    --launcher.openFile "/displays/sirius_main_all.opi"
```

Example Sirius:

```bash
cs-studio \
    -consoleLog \
    -pluginCustomization /home/opis/sirius-screens/cfg/combined_settings.ini \
    -workspace_prompt ~/.ess-cs-studio/cs-studio-workspace \
    -share_link /home/opis/sirius-screens=/displays \
    -workbench_xmi /home/opis/sirius-screens/cfg/diagnostics_workbench.xmi \
    --launcher.appendVmargs \
        -Dorg.eclipse.swt.internal.gtk.cairoGraphics=false \
        -Dorg.eclipse.swt.internal.gtk.useCairo=false \
        -Dorg.eclipse.swt.browser.DefaultType=mozilla \
    --launcher.openFile "/displays/sirius_main_all.opi"
```
