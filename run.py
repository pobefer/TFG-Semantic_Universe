import argparse
import main as main

class A():
    """
    Semantic Universe Project
        Ussage:
            [+] Run the script in one of the following modes:
                [-] IA execution (-i) for automatic detection setting thje dead man option
                [-] Manual execution setting the deep of your search
    """
    pass


if __name__ == '__main__':
    my_parser = argparse.ArgumentParser(A().__doc__,
                            formatter_class=argparse.RawDescriptionHelpFormatter)
    my_parser.add_argument('-p', action='store', type=int, required=False, help='Deep search')
    my_parser.add_argument('-d', action='store', type=str, required=False, help='Database to use')
    my_parser.add_argument('-v',
                    '--verbose',
                    action='store_true',
                    help='enable the long listing format')

    args = my_parser.parse_args()

    main.main(args.p, args.d, args.verbose)
    