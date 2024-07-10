import os
import click
from PIL import Image
from PIL.Image import Resampling
import colorama

@click.group()
def cli():
    pass

@click.command()
@click.option('--file', prompt='Filename')
@click.option('--sizes', prompt='Output sizes')
def make(file, sizes):
    sizes = sizes.split(',')
    format = file.rsplit('.')[-1]
    imagename = file.rsplit('.')[-2]

    for size in sizes:
        with Image.open(os.path.join(os.getcwd(), file)) as img:
            w, h = img.size
            ratio = h / w

            if int(size) > w:
                red(f'Output ({size}) bigger than input ({w})')
                return
            
            img.thumbnail((int(size), int(size) * ratio), Resampling.LANCZOS)
            img.save(os.path.join(os.getcwd(), f'{imagename}-{size}.{format}'))
            green(f'{imagename}-{size}.{format} saved')

@click.command()
@click.option('--file', prompt='Filename')
def getsize(file):
    with Image.open(os.path.join(os.getcwd(), file)) as img:
        w, h = img.size
        green(f'{w} x {h}')

def green(content):
    click.echo(f'{colorama.Fore.GREEN}{content}{colorama.Style.RESET_ALL}')

def red(content):
    click.echo(f'{colorama.Fore.RED}{content}{colorama.Style.RESET_ALL}')


cli.add_command(make)
cli.add_command(getsize)


if __name__ == '__main__':
    cli()