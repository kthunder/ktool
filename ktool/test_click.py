import click


@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    pass
    # click.echo('Debug mode is %s' % ('on' if debug else 'off'))


@cli.command()
def hello1():
    click.secho(f"Hello1", fg = 'green')


@cli.command()
def hello():
    click.secho(f"Hello", fg='red')


@cli.command()
@click.argument("hex_str")
def toArray(hex_str):
    click.secho(f"{hex_str}", fg='red')


if __name__ == "__main__":
    cli()
