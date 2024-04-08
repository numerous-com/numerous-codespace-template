# Numerous Codespaces Template

Create a GitHub codespace with this template: https://github.com/codespaces/new/numerous-team/numerous-codespace-template

## Use as a template for your own project

You can [fork this repository](https://github.com/numerous-team/numerous-codespace-template/fork)
and use it as a starting point for app development in your own repository,
or you can just try it out. See below to learn how!

## Try out Numerous in the codespace

Inside the codespaces, use the pre-installed Numerous command-line interface (CLI) to upload an app to the Numerous platform.

First login to your account or sign up:

    numerous login

Then go to an example project, such as the Marimo example app:

    cd marimo_app
    numerous init --app-file app.py --app-library marimo --name "My App" --requirements-file requirements.txt
    numerous push

You can do the same for the Streamlit example app:

    cd streamlit_app
    numerous init --app-file app.py --app-library streamlit --name "My App" --requirements-file requirements.txt
    numerous push

## Initializing a new project

Before, we used the `numerous init` command with arguments that specify the Marimo and Streamlit example projects specifically. But if we want to start a new project
from scratch, you can leave out those arguments and follow a wizard in the terminal instead.

We create a folder, enter it, and run the init command (you can use a different folder name, if you prefer):

    mkdir my-app
    cd my-app
    numerous init

Now a Numerous project is initialized!

## Developing in the codespace

You can edit the examples and try them out directly in the codespace!

For the Marimo example:

    cd marimo_app
    marimo edit

For the Streamlit example:

    cd streamlit_app
    streamlit run
