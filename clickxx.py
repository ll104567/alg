import click


@click.command()
@click.option('-d', '--debug', is_flag=True, help='debug mode')
def main(debug):
	if debug:
		print('Debug')
	else:
		print('Info')

main()
