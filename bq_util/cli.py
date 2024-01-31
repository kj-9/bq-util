import json
from pathlib import Path

import click
from dbt.cli.main import dbtRunner


@click.group()
@click.version_option()
def cli():
    """"""


def get_cli_args(project, dataset, location="US"):
    project_dir = Path(__file__).parent / "dbt_bq_util"
    dbt_packages_dir = project_dir / "dbt_packages"
    profiles_dir = project_dir / "profiles"

    # initialize
    dbtRunner()

    dbt_vars = {
        "PROJECT": project,
        "DATASET": dataset,
        "LOCATION": location,
        "DBT_PACKAGES_DIR": str(dbt_packages_dir),
    }

    # create CLI args as a list of strings
    cli_args = [
        "--project-dir",
        str(project_dir),
        "--profiles-dir",
        str(profiles_dir),
        "--vars",
        json.dumps(dbt_vars),
    ]

    return cli_args


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
def compile(project, dataset, location="US"):
    # initialize
    dbt = dbtRunner()

    cli_args = get_cli_args(project, dataset, location)

    cli_args = [
        "compile",
        "--select",
        "list_tables",
    ] + cli_args

    click.echo(f"Running: dbt {cli_args}")

    # run the command
    dbt.invoke(cli_args)


@cli.command(name="ls")
@click.argument("table_prefix", type=str)
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
def ls(table_prefix, project, dataset, location="US"):
    # initialize
    dbt = dbtRunner()

    cli_args = get_cli_args(project, dataset, location)

    cli_args = [
        "run-operation",
        "list_tables",
        "--args",
        json.dumps({"table_prefix": table_prefix}),
    ] + cli_args

    click.echo(f"Running: dbt {cli_args}")

    # run the command
    dbt.invoke(cli_args)


@cli.command(name="deps")
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
def deps(project, dataset, location="US"):
    # initialize
    dbt = dbtRunner()

    cli_args = get_cli_args(project, dataset, location)

    cli_args = [
        "deps",
    ] + cli_args

    click.echo(f"Running: dbt {cli_args}")

    # run the command
    dbt.invoke(cli_args)
