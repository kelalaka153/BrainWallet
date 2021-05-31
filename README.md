# BrainWallet with Python

During answering a question on [Cryptography.SE](https://crypto.stackexchange.com/a/90214/18298) I've seen that the brainwallet of [walletgenerator.net](https://walletgenerator.net/) behaves strange. To investigate I've build my own python code. And finally the behaviour is [understood](https://github.com/walletgeneratornet/WalletGenerator.net/issues/266);

> Anyways be CAREFUL. It is possible to send BTC to a wallet address which is not belong to you and probably is someones else's wallet (probably coder's wallet!!!)

> This is called SCAM or THIEF or STEALING BTC which WalletGenerator.net is doing...

There are two files;

 - **brainwallet_dev.py :** prints lots of infomation
 - **brainwallet.py :** for end-users that can use Python secrets to hide the input from the terminal and prints only the necessary information.
