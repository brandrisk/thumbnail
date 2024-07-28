import os
import click
from PIL import Image
from PIL.Image import Resampling
import colorama
import pathlib

@click.group()
def cli():
    pass

@click.command()
@click.option('--fp', prompt='Path to file', help='Path to input file')
@click.option('--sizes', prompt='Output sizes', help='Comma-separated width values. For example 100,200,300.')
def make(fp, sizes):
    sizes = [s.strip() for s in sizes.split(',')]
    split_path = pathlib.Path(fp)

    for size in sizes:
        size = int(size)

        with Image.open(fp) as img:
            filename = f'{split_path.stem}-{size}{split_path.suffix}'
            path = os.path.join(os.path.dirname(fp), filename)

            if os.path.exists(path):
                red(f'{path} already exists')
                continue

            w, h = img.size

            if size > w:
                red(f'Output size ({size}) cannot be bigger than input size ({w})')
                continue

            ratio = h / w
            
            img.thumbnail((size, size * ratio), Resampling.LANCZOS)
            
            img.save(path)
            green(f'{path} saved')

@click.command()
@click.option('--fp', prompt='Path to file', help='Path to input file')
def getsize(fp):
    with Image.open(fp) as img:
        w, h = img.size
        info(f'{w} x {h}')

def info(content):
    click.echo(content)

def green(content):
    click.echo(f'{colorama.Fore.GREEN}{content}{colorama.Style.RESET_ALL}')

def red(content):
    click.echo(f'{colorama.Fore.RED}{content}{colorama.Style.RESET_ALL}')

cli.add_command(make)
cli.add_command(getsize)

if __name__ == '__main__':
    cli()
