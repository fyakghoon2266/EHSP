#!/bin/bash

# Set virtual environment name
venv_name=".venv"

# Function to build virtual environment
build_venv() {
    python3 -m venv $venv_name
    source $venv_name/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    echo "The Python environment has been set up. Virtual environment name: $venv_name"
}

# Function to clean virtual environment
clean_venv() {
    deactivate
    rm -rf $venv_name
    echo "The virtual environment has been cleaned up."
}

# Function to display help
display_help() {
    echo "Usage: source build_tool.sh [-b | -c | --help]"
    echo "-b: Build virtual environment"
    echo "-c: Clean virtual environment"
    echo "--help: Display this help message"
}

# Check for options using getopts
while getopts ":bc-:" opt; do
    case $opt in
        b)
            build_venv
            ;;
        c)
            clean_venv
            ;;
        -)
            case "${OPTARG}" in
                help)
                    display_help
                    ;;
                *)
                    echo "Invalid option: --${OPTARG}"
                    display_help
                    ;;
            esac
            ;;
        \?)
            echo "Invalid option: -$OPTARG"
            display_help
            ;;
    esac
done

# Resetting the option index
OPTIND=1