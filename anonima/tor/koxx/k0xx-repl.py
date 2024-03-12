#!/usr/bin/env python3
# koxx-repl
#
import pycountry
import pprint

def run():
    pp = pprint.PrettyPrinter(indent=4)

    def concat_sets(countries):
        return ','.join(['{' + r.lower() + '}' for r in countries])

    # 対話的な入力で各セットを設定
    entry_countries = set(input("Enter entry countries (space-separated, e.g., 'SG'): ").lower().split())
    include_countries = set(input("Enter include countries (space-separated, e.g., 'SG TH HU AL IN MX BR'): ").lower().split())
    exit_countries = set(input("Enter exit countries (space-separated, e.g., 'SG TH HU AL IN MX BR'): ").lower().split())
    input_forbid_countries = (input("Enter forbidden countries (space-separated, press Enter for none): ").split())
    forbid_countries = set(input_forbid_countries) if input_forbid_countries else set([c.alpha_2.lower() for c in list(pycountry.countries)]) - entry_countries - include_countries - exit_countries
    all_countries = set([c.alpha_2.lower() for c in list(pycountry.countries)])

    # 禁止国が指定されない場合、すべての国からentry、include、exitを引いた集合を禁止国とする
    forbid_countries = set(input_forbid_countries) if input_forbid_countries else set([c.alpha_2.lower() for c in list(pycountry.countries)]) - entry_countries - include_countries - exit_countries
    all_countries = set([c.alpha_2.lower() for c in list(pycountry.countries)])

    all_countries = set([c.alpha_2 for c in list(pycountry.countries)])

    exclude_countries = forbid_countries

    exclude_nodes = concat_sets(exclude_countries)
    entry_nodes = concat_sets(entry_countries)
    exit_nodes = concat_sets(exit_countries)

    print("StrictNodes 1")
    print("ExcludeNodes " + exclude_nodes)
    if len(entry_nodes) > 0:
        print("EntryNodes " + entry_nodes)
    if len(exit_nodes) > 0:
        print("ExitNodes " + exit_nodes)

# プログラム実行
run()

