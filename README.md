# PyFlink Dev

This project provides a template for developing Flink applications using the Python API.

## Features

- Run and debug Flink jobs locally
- Unit testing using [Pytest](https://pytest.org/)
- Dependency management using [Poetry](https://python-poetry.org/)
- A development environment using the [devcontainers](https://containers.dev/) standard

## Installation

To start using this development environment, follow the getting started guide for your preferred editor:

- [VS Code](https://code.visualstudio.com/docs/devcontainers/containers)
- [IntelliJ IDEA](https://www.jetbrains.com/help/idea/connect-to-devcontainer.html)
- [PyCharm](https://www.jetbrains.com/help/pycharm/connect-to-devcontainer.html)

> **Prerequisite**: Please ensure [Docker](https://www.docker.com/) is installed and running on your machine.

## Workflow

This development environment optimizes Apache Flink's Python API development using Docker Compose for a minimal local Flink Cluster, featuring a Job Manager and a Task Manager. Using the [devcontainers](https://containers.dev/) standard, it simplifies the deployment of code changes and enables convenient debugging.

```mermaid
graph LR

    subgraph LocalEnvironment["Local Environiment"]
        direction LR
        Editor["Editor"]

        subgraph Docker["Docker Compose"]
            direction TB
            JobManager["Job Manager"]

            subgraph Devcontainer["Development Container"]
                direction LR
                RemoteServer["Remote Development Server"]
                Repository["Code Repository"]
                TaskManager["Task Manager"]
            end
        end
    end

    Editor -->|"Accesses"| RemoteServer
    RemoteServer -->|"Accesses"| Repository
    Editor -->|"Starts Job"| JobManager
    JobManager -->|"Starts Task"| TaskManager
    TaskManager -->|"Uses"| Repository
```

Interact with the code via your preferred editor, connected to the Remote Development Server inside the Task Manager container. The code repository is directly cloned into this container, making any updates immediately ready for deployment. Running a new Flink job involves the Job Manager coordinating with the Task Manager container to execute tasks using the latest code.

The setup allows local code execution in the development environment, enabling debugger use through your editor. This repository provides utilities for connecting the debugger to a running Flink Job, allowing for in-depth inspection of tasks and setting breakpoints directly in the execution flow.

## Usage

Follow these instructions to execute common development tasks efficiently.

### Running a Flink Job

To run a flink job locally, simply run it with python:

```bash
python examples/word_count.py
```

> **Note**: To debug a locally running job, simply run it in debug mode.

### Deploying a Flink Job

To submit a job to the job manager, use the following command. For instance, to run the `word_count` job:

```bash
flink-run examples/word_count.py
```

### Debugging a Flink Task

To debug a running Flink job running on the job manager, use the following command:

```bash
flink-debug <optional_task_id>
```

> **Note**: Without arguments, `flink-debug` targets `1-1`. Specify a different task ID if needed.

After running the command, note the process ID (e.g., `1234`) from the output. Next, attach your debugger to the running process. This allows you to set breakpoints and inspect the task's execution in real-time.

#### For VS Code Users

1. Open the debugger tab within VS Code.
2. Click the green play button to launch the debugger. Ensure you select the debugger profile included with this environment.
3. VS Code will display a list of running processes. Choose the one that matches your noted process ID.

### Unit Testing

The development environment leverages its local execution capabilities to enable unit testing for Flink jobs. An example unit test for the word count functionality is provided in `examples/test__word_count.py`. To run the unit tests, simply use the `pytest` command.
