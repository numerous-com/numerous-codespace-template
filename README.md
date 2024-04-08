# Numerous Codespaces Template

Create a GitHub codespace with this template: https://github.com/codespaces/new/numerous-team/numerous-codespace-template

# Try out examples

Inside the codespaces, use the pre-installed numerous CLI, to upload an app to the numerous platform.

First login to your account, or sign up:

    numerous login

Then go to an example project, for example for a marimo app, or streamlit app:

    cd marimo_app
    numerous init --app-file app.py --app-library marimo --name "My App" --requirements-file requirements.txt
    numerous push

You can do the same for the streamlit app:

    cd streamlit_app
    numerous init --app-file app.py --app-library streamlit --name "My App" --requirements-file requirements.txt
    numerous push
