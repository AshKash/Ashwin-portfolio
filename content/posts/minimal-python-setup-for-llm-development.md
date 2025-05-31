+++
date = '2024-03-18T09:00:00-07:00'
draft = false
title = 'Minimal Python Setup for LLM Development on MacBook'
description = 'A concise guide to setting up an efficient Python development environment for LLM development on macOS, following current best practices.'
tags = ['Python', 'Development', 'LLM', 'macOS', 'Environment Setup']
categories = ['Tutorials']
+++

A minimal Python setup for LLM development on a MacBook is crucial for a clean and efficient workflow. Here's a concise guide to current best practices.

## To Conda or Not to Conda?

For a minimal setup focused on LLM transformer development, **Conda is likely overkill**. While Conda is a powerful environment and package manager, it can be heavy and introduce unnecessary complexity. A more lightweight and modern approach is to use a combination of `pyenv` to manage Python versions and `venv` to manage project-specific dependencies. This combination provides the flexibility of Conda without the added bulk.

**`pyenv`** lets you easily switch between multiple Python versions on a single machine, which is invaluable when different projects have different version requirements.

**`venv`** is a built-in Python module that creates isolated environments, ensuring that the packages for one project don't interfere with others.

## The Minimalist's Setup Guide 🚀

Here's a streamlined process for setting up your environment:

1. **Install Homebrew:** If you don't already have it, install the quintessential macOS package manager.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. **Install `pyenv`:** Use Homebrew to install `pyenv`.

```bash
brew install pyenv
```

3. **Configure `pyenv`:** Add the following lines to your shell's configuration file (e.g., `.zshrc` for Zsh or `.bash_profile` for Bash) to ensure `pyenv` is loaded automatically.

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
```

Remember to restart your shell or run `source ~/.zshrc` for the changes to take effect.

4. **Install a Python Version:** With `pyenv` installed, you can now install your desired Python version. For LLM development, a recent version like 3.11 or later is recommended.

```bash
pyenv install 3.11.4
pyenv global 3.11.4
```

## Managing Your Virtual Environments

Once `pyenv` has set your global Python version, you can create a virtual environment for your project using `venv`.

1. **Navigate to your project directory:**

```bash
cd your-llm-project
```

2. **Create the virtual environment:**

```bash
python -m venv venv
```

This creates a `venv` directory within your project folder.

3. **Activate the environment:**

```bash
source venv/bin/activate
```

Your shell prompt will now indicate that you are in the virtual environment.

4. **Install your dependencies:** You can now install your required packages, such as PyTorch, Transformers, and Datasets.

```bash
pip install torch transformers datasets
```

5. **Create a `requirements.txt` file:** To ensure reproducibility, save your project's dependencies to a `requirements.txt` file.

```bash
pip freeze > requirements.txt
```

## Should You Check `venv` into Git?

**No, you should not check your `venv` directory into your Git repository.** This is a critical best practice for several reasons:

- **Bloat:** The `venv` folder can be quite large, containing numerous packages and their dependencies, which will unnecessarily inflate your repository size.
- **Platform Dependency:** Virtual environments are often platform-specific. A `venv` created on a MacBook may not work correctly on a Linux or Windows machine.
- **Redundancy:** The `requirements.txt` file is the canonical source for your project's dependencies. Anyone can recreate the virtual environment using this file with a simple `pip install -r requirements.txt`.

In a larger project that includes Go and Hugo, it's even more important to keep your repository clean and focused on the source code. Your `.gitignore` file should always include an entry for the virtual environment directory:

```gitignore
# Python
venv/
```

By following these guidelines, you can maintain a lean, efficient, and reproducible Python environment for your LLM development endeavors, even within a multi-language project structure.
