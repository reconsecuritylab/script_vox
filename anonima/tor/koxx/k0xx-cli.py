#!/usr/bin/env python3
import argparse
import pycountry
import pprint

def concat_sets(countries):
    return ','.join(['{' + r.lower() + '}' for r in countries])
# run関数定義、main関数
def run(entry_countries, include_countries, exit_countries, forbid_countries):
    pp = pprint.PrettyPrinter(indent=4)

    # 各セットをコマンドラインで設定
    entry_countries = set(entry_countries.lower().split())
    include_countries = set(include_countries.lower().split())
    exit_countries = set(exit_countries.lower().split())

# (全ての国 - 入口 - 経由国 - 出口) = 禁止国
    if not forbid_countries:
        forbid_countries = set([c.alpha_2.lower() for c in list(pycountry.countries)]) - entry_countries - include_countries - exit_countries
    else:
        forbid_countries = set(forbid_countries.split())

    #all_countries = set([c.alpha_2.lower() for c in list(pycountry.countries)])
    # 各ノード初期化
    exclude_countries = forbid_countries
    exclude_nodes = concat_sets(exclude_countries)
    entry_nodes = concat_sets(entry_countries)
    exit_nodes = concat_sets(exit_countries)

  # 標準出力
    print("StrictNodes 1")
    print("ExcludeNodes " + exclude_nodes)
    if len(entry_nodes) > 0:
        print("EntryNodes " + entry_nodes)
    if len(exit_nodes) > 0:
        print("ExitNodes " + exit_nodes)

  # arg handling
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Configure koxx-repl settings.")
    parser.add_argument("--entry", help="Entry countries (space-separated, e.g., 'SG')")
    parser.add_argument("--include", help="Include countries (space-separated, e.g., 'SG TH HU AL IN MX BR')")
    parser.add_argument("--exit", help="Exit countries (space-separated, e.g., 'SG TH HU AL IN MX BR')")
    parser.add_argument("--forbid", help="Forbidden countries (space-separated)")

    args = parser.parse_args()
    if not any(vars(args).values()):
        parser.print_help()
    else:
        run(args.entry, args.include, args.exit, args.forbid)
