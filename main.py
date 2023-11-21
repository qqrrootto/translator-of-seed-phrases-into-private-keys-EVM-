from eth_account import Account

input_file = "input.txt"  
output_file = "output.txt"  

Account.enable_unaudited_hdwallet_features()  


with open(input_file, "r") as file:
    mnemos = file.readlines()


private_keys = [Account.from_mnemonic(mnemo.strip())._private_key.hex() + '\n' for mnemo in mnemos]


with open(output_file, "w") as file:
    file.writelines(private_keys)

print("Private keys are written to", output_file)
