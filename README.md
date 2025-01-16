# yff-data-pipeline

Data pipelines for the
[YFF data dashboard](https://data.youthfuturesfoundation.org/)

## Preparation

### Environment file

Create a `.env` file with the following content

```
export GITHUB_TOKEN=<YOUR_GITHUB_TOKEN>
export PYTHONPATH=${PWD}
```

The GitHub token is used for cross-repo triggering of jobs (to run a site build)
(contained in [`trigger.py`](pipelines/trigger.py)). If you do not wish to do
this, you won't need to set it. It can be generated On the
[Personal access tokens (classic) page of yout GitHub Developer Settings](https://github.com/settings/tokens),
and requires _Full control of private repositories_ (`repo`).

TODO

- It is probably possible and may be desirable to update this to use
  _Fine-grained tokens_, but this may require updating the script.
- The script will currently also only trigger the hard-coded Open Innovations
  version of the site, which might be worth injecting via configuration.

### Python environment

The Python dependencies are managed with `pipenv`. You will need
[to install `pipenv`](https://pipenv.pypa.io/en/latest/installation.html). To
install the dependencies and prepare the `pipenv` environment run

```
pipenv install
```

## Pipelines

Pipeline scripts are stored in the [`pipelines`](./pipelines/) directory.

The pipelines are managed using [DVC](https://dvc.org/). DVC Stages are defined
in individual `dvc.yaml` files located close to the code they control. These
define the scripts to run, as well as the dependencies and outputs. This enables
DVC to determine the correct ordering of stages. It also means that any and
whether the stages should run (i.e. if any of the dependencies have changed).

Pipelines can be run using the command

```
pipenv run dvc repro -R pipelines
```

This will recursively find all stage definitions and run them as a job.

Individual pipelines can be run by specifying the path to a `dvc.yaml` file

```
pipenv run dvc repro pipelines/education/dvc.yaml
```

Individual stages within a pipeline can be run by specifying the path to a `dvc.yaml` file followed by the stage name:

```
pipenv run dvc repro pipelines/education/dvc.yaml:transform
```

By default this will check the dependencies.
Pipelines can be run in isolation by providing the `-s` flag.

```
pipenv run dvc repro -s pipelines/education/dvc.yaml:transform
```

To force a pipeline to run, use the `-f` flag.

```
pipenv run dvc repro -f pipelines/education/dvc.yaml:transform
```

## Data directory

Raw data is stored in `data/raw`
