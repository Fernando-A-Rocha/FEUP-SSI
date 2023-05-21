# Task 3

For this task, the objective is to run the reentrancy attack and steal the money of the victim contract (25 eth). For this purpouse, the script _launch\_attack.py_ was modified to contain the attackers address and executed to launch the attack. 

Output of get_balance.py before the attack is launched:
```bash

----------------------------------------------------------
*** This client program connects to 10.151.0.71:8545
*** The following are the accounts on this Ethereum node
0xD4CC43e3f2830f9082495Dba904B57fc2Ca95CBd: 52000151739000000000
0x5551Ee6a5E1c07A91B8a8F0Ec795d664b6F5F984: 5499999999999999999997998268568373598733
----------------------------------------------------------
  Victim: 0x744c284812517b382FA6B79A555A55d3cDC19C18: 25000000000000000000
Attacker: 0xCD292478210B48b5cE415677d51a9B4d4009c321: 0

```

Output of get_balance.py after the attack is launched:
```bash

----------------------------------------------------------
*** This client program connects to 10.151.0.71:8545
*** The following are the accounts on this Ethereum node
0xD4CC43e3f2830f9082495Dba904B57fc2Ca95CBd: 52000151739000000000
0x5551Ee6a5E1c07A91B8a8F0Ec795d664b6F5F984: 5499999999999999999996998116829372536560
----------------------------------------------------------
  Victim: 0x744c284812517b382FA6B79A555A55d3cDC19C18: 0
Attacker: 0xCD292478210B48b5cE415677d51a9B4d4009c321: 26000000000000000000


```

As observable in the output of the get_balance.py script before and after the attack is executed, we can conclude that it succeeds, given that the victim's money (25 eth) is completely drained into the attackers smart contract.
Consequently, the cashout.py script is run and the attackers money is transferred into another account (the first one).

Output of get_balance.py after executing cashout.py into the first account:
```bash

----------------------------------------------------------
*** This client program connects to 10.151.0.71:8545
*** The following are the accounts on this Ethereum node
0xD4CC43e3f2830f9082495Dba904B57fc2Ca95CBd: 78000151739000000000
0x5551Ee6a5E1c07A91B8a8F0Ec795d664b6F5F984: 5499999999999999999996998083567372303726
----------------------------------------------------------
  Victim: 0x744c284812517b382FA6B79A555A55d3cDC19C18: 0
Attacker: 0xCD292478210B48b5cE415677d51a9B4d4009c321: 0

```