import click

@click.command()
@click.option('-c','--count',default=1,help='Number')
@click.argument('name')
def hello(count,name):
	if count and name:
		for i in range(count):
			click.echo('hello {}'.format(name))

if __name__ =='__main__':
	hello()
