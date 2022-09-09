# replicada
Replicada is a self-replicating file written in Python, running it will mess up your directory.

watch [this](https://youtu.be/8xqzGnn6GH4) video to see how it looks like to be executed.

## warnings

- this file may cause damage to your cwd (current working directory)

- this file may cause lags to your computer

- this file may lead to unexpected results

## processes

1. creates randomly named directories (will not stop until the script is being killed)

2. scans the currently working directory (cwd)

3. copies itself and pastes inside every directories that are inside cwd (and probably overwrites existed files)

4. copies itself into every directories that were created by itself

5. execute itself inside directories

6. create directories
