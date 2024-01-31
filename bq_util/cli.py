import json
from pathlib import Path

import click
from dbt.cli.main import dbtRunner, dbtRunnerResult


@click.group()
@click.version_option()
def cli():
    """"""


@cli.command(name="compile")
@click.option(
    "--project",
    required=True,
    help="The GCP project to use for the BigQuery dataset.",
)
@click.option(
    "--dataset",
    required=True,
    help="The BigQuery dataset to use for the DBT project.",
)
def compile(project, dataset, location="asia-northeast1"):
    project_dir = Path(__file__).parent / "dbt_bq_util"
    dbt_packages_dir = project_dir / "dbt_packages"
    profiles_dir = project_dir / "profiles"

    # initialize
    dbt = dbtRunner()

    dbt_vars = {
        "PROJECT": project,
        "DATASET": dataset,
        "LOCATION": location,
        "DBT_PACKAGES_DIR": str(dbt_packages_dir),
    }

    # create CLI args as a list of strings
    cli_args = [
        "compile",
        "--select",
        "tag:my_tag",
        "--project-dir",
        str(project_dir),
        "--profiles-dir",
        str(profiles_dir),
        "--vars",
        json.dumps(dbt_vars),
    ]

    click.echo(f"Running: dbt {cli_args}")

    # run the command
    res: dbtRunnerResult = dbt.invoke(cli_args)

    # inspect the results
    for r in res.result:
        click.echo(f"{r.node.name}: {r.status}")
