import click

from .hex_to_array import hex_to_array


@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    pass


@cli.command()
@click.argument("hex_str")
def to_array(hex_str):
    click.secho(hex_to_array(hex_str), fg='green')


if __name__ == "__main__":
    cli()
