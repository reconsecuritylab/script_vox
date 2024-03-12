# K0XX - torrc generater
k0xx is a script that generates torrc that only goes through the specified country. Written in Python. The biggest appeal of the k0xx series is that if you specify the entry country, include country, and exit country, all countries other than those specified will be designated as prohibited countries at once. In addition to reducing the risk of mixing prohibited countries and permitted countries compared to manual work, since all countries other than the selected country are prohibited countries, the tedious process of circuit creation can be semi-automated.
## k0xx-repl vs k0xx-cli
k0xx-repl is interactive, whereas k0xx-cli operates with command line arguments. k0xx-repl was created assuming operation in an Android Termux environment, so it is optimized for smartphones. On the other hand, k0xx-cli is intended for use in a PC environment or as an assembly for external programs, so operations are performed using command line arguments.

## How To Use
```
## k0xx-cli
~ :% k0xx-cli.py
usage: k0xx-cli.py [-h] [--entry ENTRY] [--include INCLUDE] [--exit EXIT] [--forbid FORBID]

Configure koxx-repl settings.

options:
  -h, --help         show this help message and exit
  --entry ENTRY      Entry countries (space-separated, e.g., 'SG')
  --include INCLUDE  Include countries (space-separated, e.g., 'SG TH HU AL IN MX BR')
  --exit EXIT        Exit countries (space-separated, e.g., 'SG TH HU AL IN MX BR')
  --forbid FORBID    Forbidden countries (space-separated)
~ :% k0xx-cli.py --entry SG --include AT --exit JP
StrictNodes 1
ExcludeNodes {be},{ps},{aq},{gh},{tw},{br},{ru},{va},{lr},{bz},{gi},{py},{dj},{eg},{fm},{ni},{re},{dz},{la},{mq},{wf},{us},{bo},{kw},{mt},{tf},{gm},{nr},{ne},{ve},{es},{cu},{lc},{pe},{ke},{ax},{mg},{cv},{gb},{pm},{no},{mk},{ro},{bq},{ma},{qa},{gy},{se},{sk},{bv},{cg},{sj},{cz},{za},{bb},{fj},{ai},{tt},{cd},{pw},{pn},{dm},{mc},{ad},{cm},{do},{tl},{bf},{ph},{as},{gl},{io},{ki},{si},{ht},{ie},{me},{mz},{sm},{pt},{dk},{tg},{ck},{bt},{iq},{kz},{ng},{sx},{ec},{pg},{az},{jm},{bi},{ao},{co},{td},{mf},{vc},{vu},{je},{st},{sh},{sc},{bg},{pk},{rs},{sr},{vn},{hk},{lv},{mn},{zw},{pl},{ar},{sy},{mh},{pf},{gt},{ca},{id},{kr},{hn},{bs},{gp},{nl},{km},{nu},{np},{um},{in},{lb},{lu},{ms},{tk},{by},{kh},{cy},{af},{li},{gf},{ua},{cf},{ee},{jo},{sl},{ch},{to},{gr},{sd},{cw},{tn},{il},{au},{tz},{tj},{gu},{uz},{bl},{mr},{gs},{al},{sa},{tm},{nz},{my},{mw},{sb},{gq},{bd},{et},{gg},{ge},{is},{tv},{gw},{mv},{ss},{cc},{ir},{pr},{ag},{ye},{om},{lt},{fk},{gn},{im},{cn},{kn},{bw},{fo},{fr},{ae},{hr},{de},{kg},{bm},{ky},{bn},{sn},{bh},{pa},{mu},{tr},{ba},{mx},{nc},{sz},{na},{it},{tc},{vg},{aw},{hu},{cl},{ci},{uy},{cx},{am},{lk},{ws},{eh},{mo},{ml},{ug},{mm},{th},{ly},{yt},{zm},{mp},{sv},{so},{bj},{er},{ga},{nf},{fi},{kp},{cr},{hm},{vi},{rw},{gd},{ls},{md}
EntryNodes {sg}
ExitNodes {jp}

```
```
## k0xx-repl
~ :% k0xx-repl.py
Enter entry countries (space-separated, e.g., 'SG'): SG
Enter include countries (space-separated, e.g., 'SG TH HU AL IN MX BR'): AT
Enter exit countries (space-separated, e.g., 'SG TH HU AL IN MX BR'): JP
Enter forbidden countries (space-separated, press Enter for none):
StrictNodes 1
ExcludeNodes {ec},{fr},{be},{gi},{ki},{yt},{to},{lr},{gb},{as},{bg},{gn},{gp},{kr},{bo},{nu},{pa},{sr},{ua},{gf},{cd},{kw},{na},{no},{jo},{ms},{sc},{tk},{sy},{cw},{pk},{io},{bf},{au},{bt},{uy},{fk},{cn},{dj},{ky},{bv},{tw},{ye},{mo},{jm},{ws},{cr},{bz},{ai},{im},{me},{do},{sb},{by},{sa},{tn},{mg},{mt},{cc},{nc},{la},{my},{ir},{va},{lv},{mh},{kz},{sv},{km},{rw},{wf},{aq},{bd},{lb},{cm},{cl},{cg},{bl},{nf},{za},{pw},{mn},{ma},{bs},{vg},{mm},{tl},{kh},{md},{ba},{sl},{pg},{kn},{dz},{tf},{gw},{ni},{np},{sk},{gg},{id},{sx},{er},{ck},{ly},{mq},{pr},{st},{cf},{ga},{vi},{is},{ph},{cy},{sh},{gr},{py},{gu},{je},{lu},{cz},{ug},{lt},{gq},{sd},{ml},{in},{mz},{ae},{ke},{mx},{ch},{vn},{ag},{gt},{bn},{lc},{iq},{tc},{qa},{sz},{bh},{ao},{mf},{tt},{fj},{rs},{tj},{ar},{hk},{de},{uz},{ss},{pe},{pf},{gd},{vu},{af},{gl},{mr},{us},{re},{mu},{se},{az},{bi},{ps},{es},{ru},{li},{pn},{ht},{om},{mw},{co},{eg},{am},{gh},{nz},{ng},{ax},{tr},{dk},{mc},{gy},{fi},{tv},{ls},{it},{sm},{kg},{zw},{al},{cu},{mp},{kp},{si},{eh},{br},{pm},{sn},{ci},{zm},{mk},{ee},{ie},{pl},{lk},{ro},{bj},{hu},{ne},{nr},{gs},{so},{fo},{tm},{cv},{et},{il},{hn},{ad},{dm},{hr},{bq},{sj},{tg},{vc},{fm},{gm},{bm},{bb},{th},{ca},{mv},{td},{aw},{nl},{pt},{bw},{ge},{um},{ve},{cx},{hm},{tz}
EntryNodes {sg}
ExitNodes {jp}

```
