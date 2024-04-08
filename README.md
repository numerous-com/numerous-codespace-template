# Numerous Codespaces Template

Create a GitHub codespace with this template: https://github.com/codespaces/new/numerous-team/numerous-codespace-template

## Use as a template for your own project

You can [fork this repository](https://github.com/numerous-team/numerous-codespace-template/fork)
and use it as a starting point for app development in your own repository,
or you can just try it out. See below how to do that!

## Try out numerous in the codespace

Inside the codespaces, use the pre-installed numerous CLI, to upload an app to the numerous platform.

First login to your account, or sign up:

    numerous login

Then go to an example project, for example for the marimo example app:

    cd marimo_app
    numerous init --app-file app.py --app-library marimo --name "My App" --requirements-file requirements.txt
    numerous push

You can do the same for the streamlit example app:

    cd streamlit_app
    numerous init --app-file app.py --app-library streamlit --name "My App" --requirements-file requirements.txt
    numerous push

## Initializing a new project

Before we used the `numerous init` command with arguments that specify the marimo and streamlit example projects specifically. But if we want to start a new project
from scratch, you can instead leave out those arguments, and follow a wizard in the terminal.

We create a folder, enter it, and run the init command (you can use a different folder name, if you prefer):

    mkdir my-app
    cd my-app
    numerous init

Now a numerous project is initialized!

## Developing in the codespace

You can of course edit the examples and try them out directly in the codespace!

For example, for the marimo example:

    cd marimo_app
    marimo edit

And for the streamlit example:

    cd streamlit_app
    streamlit run
