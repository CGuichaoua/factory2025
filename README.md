# Setting up an environment
## Install and configure WSL

## Install VSCode 
- Download VSCode.
- Install the WSL extension
- Open a WSL window: F1 -> connect to WSL 

## Install uv
In a root shell of WSL (`wsl -u root`), type `snap install astral-uv`

## Setup a project
- Create a new folder and open it
- Run `uv init` and `uv python pin 3.13`

## Add the dependencies we'll use
- Run `uv add openai`
- Finish with `uv sync`