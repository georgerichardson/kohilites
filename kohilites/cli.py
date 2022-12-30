import click
import os

from .kohilites import MetaData

@click.command()
@click.option('--input', help='Path to document metadata.')
@click.option('--output', help='Path to save parsed document metadata.', default=None)
def get_highlights(input, output):
    """Extracts highlights from one or several KoReader metadata files.

    Args:
        input (str): Directory containing metadata files or path to a single
            metadata file.
        output (str): Directory to save parsed outputs. If empty then outputs
            are saved to same directory as inputs.
    """
    if os.path.isdir(input):
        for dir, _, files in os.walk(input):
            for fin in files:
                if fin.startswith("metadata.") and fin.endswith(".lua"):
                    fname = dir.split("/")[-1][:-4]
                    click.echo(f"Parsing {fname}")
                    metadata = MetaData(os.path.join(dir, fin), output)
                    metadata.highlights()
    else:
        metadata = MetaData(input, output)
        metadata.highlights()
        

if __name__ == "__main__":
    get_highlights()
