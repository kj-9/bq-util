from pathlib import Path

import click
from dbt.cli.main import dbtRunner, dbtRunnerResult


@click.group()
@click.version_option()
def cli():
    """"""


@cli.command(name="compile")
@click.argument("example")
@click.option(
    "-o",
    "--option",
    help="An example option",
)
def first_command(example, option):
    project_dir = Path(__file__).parent / "dbt_bq_util"
    profiles_dir = project_dir / "profiles"

    # initialize
    dbt = dbtRunner()

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
        '{"BQ_UTIL_DATASET": "test_data", "BQ_UTIL_PROJECT": "test_project"}',
    ]

    # run the command
    res: dbtRunnerResult = dbt.invoke(cli_args)

    print(res)

    # inspect the results
    for r in res.result:
        print(f"{r.node.name}: {r.status}")
    import dbt
