# Pipelines

The pipelines are orchestrated using [DVC](https://dvc.org).

## Current dependency graph

[![](https://mermaid.ink/img/pako:eNqVlE1TgzAQhv9KJ-dGpba15eDJo170pnjYJgtkmg8mBDtMp__dtIVRSPwoJ9jN805292X3hBmOJCW5NDtWgnWTx-dMT7pH-2TylpFKVCiFxvqaf7CrFpRMWYlsS3NjaQUF0qbi4LDOyPuQng1ohrpuvolws9PSAKfnREDf_kpX1jCs65_g-RCWIBRoF-P7VCCxiNeujRI17S8fUMs45awoCrS0Fg6p7xYE4N0AFDqX4ITRXxIFugBa_QV1ZQbgegBK2JjGUgV2iy4yodwaRU-FB0LJzUVK8mgUR5XRrpRtqJb8R62fXSe2aWnFjA7FZheJqYiBKb0_WXHkzC68HHkuHl504flo3l14NZpoXGTdhZNk3P4-MRt3Mi6U9DUtyZQotAoE9ytgfzyVEVeiwoyk_pVjDo30lsv0wR-FxpmXVjPirdzglJz_-QcBhQVF0hxk7aMV6Fdjvr6RC2fs03nNnLbN4ROhFXZq?type=png)](https://mermaid.live/edit#pako:eNqVlE1TgzAQhv9KJ-dGpba15eDJo170pnjYJgtkmg8mBDtMp__dtIVRSPwoJ9jN805292X3hBmOJCW5NDtWgnWTx-dMT7pH-2TylpFKVCiFxvqaf7CrFpRMWYlsS3NjaQUF0qbi4LDOyPuQng1ohrpuvolws9PSAKfnREDf_kpX1jCs65_g-RCWIBRoF-P7VCCxiNeujRI17S8fUMs45awoCrS0Fg6p7xYE4N0AFDqX4ITRXxIFugBa_QV1ZQbgegBK2JjGUgV2iy4yodwaRU-FB0LJzUVK8mgUR5XRrpRtqJb8R62fXSe2aWnFjA7FZheJqYiBKb0_WXHkzC68HHkuHl504flo3l14NZpoXGTdhZNk3P4-MRt3Mi6U9DUtyZQotAoE9ytgfzyVEVeiwoyk_pVjDo30lsv0wR-FxpmXVjPirdzglJz_-QcBhQVF0hxk7aMV6Fdjvr6RC2fs03nNnLbN4ROhFXZq)

> This has been generated by running `dvc dag --mermaid` and copying the result
> into https://mermaid.live/. _NB_ changing the flowchart direction from `TD` to
> `LR` seems to render a better chart.

## Pipeline automation

These are automated by the
[`pipeline` GitHub action](../.github/workflows/pipeline.yml).

It is currently scheduled to run every weekday at 06:20, 07:20, 08:20 and 09:20,
using the cron string [20 6-9 * * 1-5](https://crontab.guru/#20_6-9_*_*_1-5). It
can also be triggered manually on the
[`pipeline` page on GitHub](https://github.com/open-innovations/yff-data-pipelines/actions/workflows/pipeline.yml).

## Outbound triggers

The stage [pipelines/dvc.yaml:trigger-site-build](../pipelines/dvc.yaml) watches
for any changes in `data/processed` and `data/metadata` and uses a GitHub
Repository Dispatch trigger to cause the
[Update data action](https://github.com/open-innovations/yff-data/actions/workflows/update-data.yml)
to run on the YFF Data site repository. This means that as the data changes in
this repository, it will immediately start a build in the data pipeline, which
will in turn trigger a build in the site.

_NB_ There is a slight possiblity that the build of the pipeline will start
working before the update from the site has been committed to this repository.
This would mean the data is not available to the site build[^1]. This is being
monitoried for the next run to see how problematic it becomes.

[^1]: There are ways around this, using a conditional GitHub action step which
triggers only if the commit step triggers.