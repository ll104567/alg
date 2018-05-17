
import click

@click.command()
@click.option('-c','--color',type=click.Choice(['red','green','default']))
def print_color(color):
	print(color)

print_color()
