from pywallet import wallet
print("Welcome to BM Hd wallet generator!!")
print("this is a program that simply generates 7 different cryptocurrency address")
print("------------------------------------")
print("Bitcoin:BTC \n 2-BitcoinCash:BCH \n 3-BitcoinGold:BTG \n 4-Ethereum:ETH \n 5-LiteCoin:LTC \n 6-Dash:DSH \n 7-DogeCoin:DOGE")
print(" ")
coin = input("Enter the symbol of cryptocurrency to generate a wallet. like BTC(they must be in uppercase): ")
seed = wallet.generate_mnemonic()
w = wallet.create_wallet(network=coin, seed=seed, children=1)

print(w)

save = input("save this wallet information into a txt file?[y/n]")
if save == "y" :
    input("make sure you move the last wallet files to another directory. Press enter ")
    files = open ("walletinfo.txt","w")
    ww = str(w)
    files.write(ww)
    files.close()
    input("information has been saved in [walletinfo.txt] press enter to exit")
    exit()
else :
    exit()
