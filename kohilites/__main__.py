import click

from kohilites.kohilites import MetaData

@click.command()
@click.option('--path', help='Path to document metadata')
def get_highlights(path):
    metadata = MetaData(path)
    metadata.highlights()

if __name__ == "__main__":
    get_highlights()
