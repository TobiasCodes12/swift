# parser_module.py
import argparse

def create_parser():
    parser = argparse.ArgumentParser(description="Swift Files Tool")
    return parser

def add_arguments(parser):
    parser.add_argument("--file", type=str, help="Path to the input file")
    parser.add_argument("--output", type=str, help="Path to the output file")
    parser.add_argument("--flag", action="store_true", help="Enable or disable the flag")

def add_subparsers(parser):
    subparsers = parser.add_subparsers(dest="subparser_name", help="Subcommands help")

    # Create a subparser for the 'csv' subcommand
    csv_parser = subparsers.add_parser("csv", help="Csv files")
    csv_parser.add_argument("-d", "--duplicate-check", action="store_true", help="Duplicate check")

    # Create a subparser for the 'docx' subcommand
    doc_parser = subparsers.add_parser("doc", help="Doc files")
    doc_parser.add_argument("-d", "--duplicate-check", action="store_true", help="Duplicate check")

def process_args(args):
    input_file = args.input
    output_file = args.output
    flag = args.flag
    subparser_name = args.subparser_name

    print(f"Input file: {input_file}")
    print(f"Output file: {output_file}")
    print(f"Flag: {flag}")

    # if subparser_name == "csv":
    #     print(f"csv argument: {args.arg1}")
    # elif subparser_name == "doc":
    #     print(f"doc argument: {args.arg2}")
