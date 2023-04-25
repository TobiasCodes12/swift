import swiftFiles.parse as p

def main():
    parser = p.create_parser()
    p.add_arguments(parser)
    p.add_subparsers(parser)

    args = parser.parse_args()
    p.process_args(args)

if __name__ == "__main__":
    main()