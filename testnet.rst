.. _test-networks:

********************************************************************************
Test Networks
********************************************************************************

Morden testnet
================================================================================
Morden is a public Bither alternative testnet. It is expected to
continue throughout the Frontier and Homestead milestones of the software.

Usage
--------------------------------------------------------------------------------

bith (Go client)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: Console

   > bith --testnet

Details
--------------------------------------------------------------------------------
All parameters are the same as the main Bither network except:

-  Network Name: **Morden**
-  Network Identity: 2
-  genesis.json (given below);
-  Initial Account Nonce (``IAN``) is 2^20 (instead of 0 in all previous
   networks).

   -  All accounts in the state trie have nonce >= ``IAN``.
   -  Whenever an account is inserted into the state trie it is
      initialised with nonce = ``IAN``.

-  Genesis generic block hash:
   ``0cd786a2425d16f152c658316c423e6ce1181e15c3295826d7c9904cba9ce303``
-  Genesis generic state root:
   ``f3f4696bbf3b3b07775128eb7a3763279a394e382130f27c21e70233e04946a9``

Morden's genesis.json
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: JSON

	{
			"nonce": "0x00006d6f7264656e",
			"difficulty": "0x20000",
			"mixhash": "0x00000000000000000000000000000000000000647572616c65787365646c6578",
			"coinbase": "0x0000000000000000000000000000000000000000",
			"timestamp": "0x00",
			"parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
			"extraData": "0x",
			"gasLimit": "0x2FEFD8",
			"alloc": {
					"0000000000000000000000000000000000000001": { "balance": "1" },
					"0000000000000000000000000000000000000002": { "balance": "1" },
					"0000000000000000000000000000000000000003": { "balance": "1" },
					"0000000000000000000000000000000000000004": { "balance": "1" },
					"102e61f5d8f9bc71d0ad4a084df4e65e05ce0e1c": { "balance": "1606938044258990275541962092341162602522202993782792835301376" }
			}
	}

Getting Morden testnet bither
--------------------------------------------------------------------------------

Two ways to obtain Morden testnet bither:

- Mine using your CPU/GPU, (see :ref:`mining`).
- Use the `Bither wei faucet <https://zerogox.com/ethereum/wei_faucet>`__.


********************************************************************************
Setting up a local private testnet
********************************************************************************

.. _custom-networks-eth:

bith (Go client)
================================================================================


You either pre-generate or mine your own bither on a private
testnet. It is a much more cost effective way of trying out
Bither and you can avoid having to mine or find Morden test bither.

The things that are required to specify in a private chain are:
 - Custom Genesis File
 - Custom Data Directory
 - Custom NetworkID
 - (Recommended) Disable Node Discovery

The genesis file
--------------------------------------------------------------------------------

The genesis block is the start of the blockchain - the first
block, block 0, and the only block that does not point to a predecessor
block. The protocol ensures that no other node will agree with your version of the
blockchain unless they have the same genesis block, so you can make as many private testnet blockchains as you'd like!

:file:`CustomGenesis.json`

.. code-block:: JSON

  {
      "nonce": "0x0000000000000042",     "timestamp": "0x0",
      "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
      "extraData": "0x0",     "gasLimit": "0x8000000",     "difficulty": "0x400",
      "mixhash": "0x0000000000000000000000000000000000000000000000000000000000000000",
      "coinbase": "0x3333333333333333333333333333333333333333",     "alloc": {     }
  }

Save a file called :file:`CustomGenesis.json`.
You will reference this when starting your bith node using the following command:

``bith init /path/to/CustomGenesis.json``

.. note:: By default bith will use the same directory for network related files as for the public mainnet. Thus you are advised to set a custom ``--datadir`` to keep the public network's chaindata from bing reset.

Command line parameters for private network
--------------------------------------------------------------------------------

There are some command line options (also called “flags”) that are
necessary in order to make sure that your network is private. We already covered the genesis flag, but we need a few more. Note that all of the commands below are to be used in the bith Bither client.

``--nodiscover``

Use this to make sure that your node is not discoverable by people who do not manually add you. Otherwise, there is a chance that your node may be inadvertently added to a stranger's blockchain if they have the same genesis file and network id.

``--maxpeers 0``

Use maxpeers 0 if you do not want anyone else connecting to your test chain. Alternatively, you can adjust this number if you know exactly how many peers you want connecting to your node.

``--rpc``

This will enable RPC interface on your node. This is generally enabled by default in Bith.


``--rpcapi "db,eth,net,web3"``

This dictates what APIs that are allowed to be accessed over RPC. By default, Bith enables the web3 interface over RPC.

**IMPORTANT: Please note that offering an API over the RPC/IPC interface will give everyone access to the API who can access this interface (e.g. dapp's). Be careful which API's you enable. By default bith enables all API's over the IPC interface and only the db,eth,net and web3 API's over the RPC interface.**

``--rpcport "8080"``

Change 8000 to any port that is open on your network. The default for bith is 8080.

``--rpccorsdomain "http://chriseth.github.io/browser-solidity/"``

This dictates what URLs can connect to your node in order to perform RPC client tasks. Be very careful with this and type a specific URL rather than the wildcard (*) which would allow any URL to connect to your RPC instance.

``--datadir "/home/TestChain1"``

This is the data directory that your private chain data will be stored in (under the :file:`nubits` . Choose a location that is separate from your public Bither chain folder.


``--port "41207"``

This is the "network listening port", which you will use to connect with other peers manually.


``--identity "TestnetMainNode"``

This will set up an identity for your node so it can be identified more easily in a list of peers.
Here is an example of how these identities show up on the network.

Launching ``bith``
--------------------------------------------------------------------------------

After you have created your custom genesis block JSON file and created a directory for your blockchain data, type the following command into your console that has access to bith:

.. code-block:: Console

  bith --identity "MyNodeName" --rpc --rpcport "8080" --rpccorsdomain "*" --datadir "C:\chains\TestChain1" --port "41207" --nodiscover --rpcapi "db,eth,net,web3" --networkid 1999 init /path/to/CustomGenesis.json

.. note:: Please change the flags to match your custom settings.

This will initialize your genesis block.  To interact with bith through the console enter:

.. code-block:: Console

  bith --identity "MyNodeName" --rpc --rpcport "8080" --rpccorsdomain "*" --datadir "C:\chains\TestChain1" --port "41207" --nodiscover --rpcapi "db,eth,net,web3" --networkid 1999 console

You will need to start your bith instance with your custom chain command every time you want to access your custom chain. If you just type "bith" in your console, it will not remember all of the flags you have set.

The full list of methods available through the javascript console is available on `the bith wiki on github <https://github.com/ethereum/go-ethereum/wiki/JavaScript-Console>`_

If you already have a bith node running, you can attach another bith instance to it using:

.. code-block:: Console

  bith attach

Now you'll need to initialize a new account on the testnest, and set it as your etherbase (the address that will receive mining rewards).

In the javascript console type

.. code-block:: Console

  personal.newAccount("password")

.. note:: Replace with the password of your choice

Now we'll set it as the etherbase:

.. code-block:: Console

  miner.setEtherbase(personal.listAccounts[0])

If successful, the console will print "true"

Finally, you are ready to start mining test bither:

.. code-block:: Console

  miner.start()

Pre-allocating bither to your account
--------------------------------------------------------------------------------

A difficulty of "0x400" allows you to mine Bither very quickly on your private testnet chain. If you create your chain and start mining, you should have hundreds of bither in a matter of minutes which is way more than enough to test transactions on your network. If you would still like to pre-allocate Bither to your account, you will need to:

1. Create a new Bither account after you create your private chain
2. Copy your new account address
3. Add the following command to your Custom_Genesis.json file:

.. code-block:: Javascript

  "alloc":
  {
	  "<your account address e.g. 0x1fb891f92eb557f4d688463d0d7c560552263b5a>":
	  { "balance": "20000000000000000000" }
  }

.. note:: Replace ``0x1fb891f92eb557f4d688463d0d7c560552263b5a`` with your account address.

Save your genesis file and rerun your private chain command. Once bith is fully loaded, close it by .

We want to assign an address to the variable ``primary`` and check its balance.

Run the command ``bith account list`` in your terminal to see what account # your new address was assigned.

.. code-block:: Console

   > bith account list
   Account #0: {d1ade25ccd3d550a7eb532ac759cac7be09c2719}
   Account #1: {da65665fc30803cb1fb7e6d86691e20b1826dee0}
   Account #2: {e470b1a7d2c9c5c6f03bbaa8fa20db6d404a0c32}
   Account #3: {f4dd5c3794f1fd0cdc0327a83aa472609c806e99}

Take note of which account # is the one that you pre-allocated bither to.
Alternatively, you can launch the console with ``bith console`` (keep the same parameters as when you launched ``bith`` first). Once the prompt appears, type

.. code-block:: Console

  > eth.accounts

This will return the array of account addresses you possess.

.. code-block:: Console

  > primary = eth.accounts[0]

.. note:: Replace ``0`` with your account's index. This console command should return your primary Bither address.

Type the following command:

.. code-block:: Console

  > balance = web3.fromWei(eth.getBalance(primary), "bither");

This should return ``7.5`` indicating you have that much bither in your account. The reason we had to put such a large number in the alloc section of your genesis file is because the "balance" field takes a number in wei which is the smallest denomination of the Bither currency bither (see _`Bither`).


* https://www.reddit.com/r/ethereum/comments/3kdnus/question_about_private_chain_mining_dont_upvote/
