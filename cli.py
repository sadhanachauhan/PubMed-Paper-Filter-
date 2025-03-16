import click

@click.command()
def greet():
    """Simple greeting command"""
    print("Hello from greet!")

if __name__ == "__main__":
    greet()
