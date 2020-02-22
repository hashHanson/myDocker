#!/usr/bin/env python

import click
import readContent


if __name__ == '__main__':
    val = readContent.articleReader("articles")
    click.echo(val)