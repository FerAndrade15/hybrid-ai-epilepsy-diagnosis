#!/bin/bash
set -e

echo "Verifying uv ..."
if ! command -v uv &> /dev/null; then
    echo "uv not found. Downloading..."
    if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
        powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
        export PATH="$HOME/.local/bin:$PATH"
    else
        curl -LsSf https://astral.sh/uv/install.sh | sh
        source "$HOME/.cargo/env" 2>/dev/null || export PATH="$HOME/.local/bin:$PATH"
    fi

    if ! command -v uv &> /dev/null; then
        echo "uv installed, but session not detected"
        echo "Close terminal and run ./setup.sh again"
        exit 1
    fi
    echo "uv installed successfully"
fi

echo "Creating venv with Python $(cat .python-version 2>/dev/null || echo '3.11')..."
uv venv --python "$(cat .python-version 2>/dev/null || echo '3.11')"

echo "Installing dependencies..."
uv pip install -r requirements.txt

echo ""
echo "Completed, activate the environment with:"
echo "  source .venv/Scripts/activate   (Windows/Git Bash)"
echo "  source .venv/bin/activate       (Mac/Linux)"
