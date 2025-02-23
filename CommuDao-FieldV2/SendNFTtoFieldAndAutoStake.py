import csv
import json
from web3 import Web3

# Set up your Web3 provider (e.g., using Infura or local provider)
w3 = Web3(Web3.HTTPProvider("https://rpc-l1.jibchain.net"))

# ERC721 and FieldV2 contract ABI and address
ERC721ABI = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"string","name":"tokenURI","type":"string"}],"name":"safeMint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"}]')  # Replace with actual ERC721 ABI JSON
ERC721Address = "0x20724DC1D37E67B7B69B52300fDbA85E558d8F9A"  # Replace with actual ERC721 contract address
FieldV2ABI = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"OwnableInvalidOwner","type":"error"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"OwnableUnauthorizedAccount","type":"error"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"staker","type":"address"},{"indexed":true,"internalType":"uint256","name":"peripheryIndex","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"nftIndex","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"nftId","type":"uint256"}],"name":"AllowStakedUseByPeriphery","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"staker","type":"address"},{"indexed":true,"internalType":"uint256","name":"nftIndex","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"nftId","type":"uint256"}],"name":"EmergencyWithdrawNft","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"peripheryIndex","type":"uint256"},{"indexed":true,"internalType":"address","name":"peripheryOwner","type":"address"},{"indexed":true,"internalType":"uint256","name":"rewardTokenIndex","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"migrateAmount","type":"uint256"}],"name":"EmergencyWithdrawRewardToken","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"peripheryIndex","type":"uint256"},{"indexed":true,"internalType":"address","name":"migrateTo","type":"address"},{"indexed":true,"internalType":"uint256","name":"rewardTokenIndex","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"migrateAmount","type":"uint256"}],"name":"MigratePeripheryRewardToAddr","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"peripheryIndexFrom","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"peripheryIndexTo","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"rewardTokenIndex","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"migrateAmount","type":"uint256"}],"name":"MigratePeripheryRewardToHook","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"staker","type":"address"},{"indexed":true,"internalType":"uint256","name":"nftIndex","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"nftId","type":"uint256"}],"name":"NftStaked","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"staker","type":"address"},{"indexed":true,"internalType":"uint256","name":"nftIndex","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"nftId","type":"uint256"}],"name":"NftUnstaked","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"staker","type":"address"},{"indexed":true,"internalType":"uint256","name":"peripheryIndex","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"nftIndex","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"nftId","type":"uint256"}],"name":"RevokeStakedUseByPeriphery","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"peripheryIndex","type":"uint256"},{"indexed":true,"internalType":"address","name":"claimedTo","type":"address"},{"indexed":true,"internalType":"uint256","name":"rewardTokenIndex","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"claimedAmount","type":"uint256"}],"name":"SendRewardFromPeriphery","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"peripheryIndex","type":"uint256"},{"indexed":true,"internalType":"address","name":"oldOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"SetPeripheryOwner","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"peripheryIndex","type":"uint256"},{"indexed":true,"internalType":"address","name":"peripheryOwner","type":"address"},{"indexed":true,"internalType":"uint256","name":"rewardTokenIndex","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"rewardTokenAmount","type":"uint256"}],"name":"SetPeripheryReward","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"peripheryIndex","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"nftIndex","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"nftId","type":"uint256"},{"indexed":true,"internalType":"address","name":"robber","type":"address"}],"name":"StealNftStakedFromPeriphery","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"peripheryIndex","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"nftIndex","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"nftId","type":"uint256"}],"name":"SyncNftStakedAtFromPeriphery","type":"event"},{"inputs":[{"internalType":"uint256","name":"_peripheryIndex","type":"uint256"},{"internalType":"uint256","name":"_nftIndex","type":"uint256"},{"internalType":"uint256","name":"_nftId","type":"uint256"}],"name":"allowStakedUseByPeriphery","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_nftIndex","type":"uint256"},{"internalType":"uint256","name":"_nftId","type":"uint256"}],"name":"emergencyWithdrawNft","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_peripheryIndex","type":"uint256"},{"internalType":"uint256","name":"_rewardTokenIndex","type":"uint256"},{"internalType":"uint256","name":"_migrateAmount","type":"uint256"}],"name":"emergencyWithdrawRewardToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"feeForCreatePeriphery","outputs":[{"internalType":"address","name":"feeCollector","type":"address"},{"internalType":"uint256","name":"feeAmount","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"hookUseByPeriphery","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"hooks","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"hooksCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"hooksIndexOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_peripheryIndex","type":"uint256"},{"internalType":"address","name":"_migrateTo","type":"address"},{"internalType":"uint256","name":"_rewardTokenIndex","type":"uint256"},{"internalType":"uint256","name":"_migrateAmount","type":"uint256"}],"name":"migratePeripheryRewardToAddr","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_peripheryIndexFrom","type":"uint256"},{"internalType":"uint256","name":"_peripheryIndexTo","type":"uint256"},{"internalType":"uint256","name":"_rewardTokenIndex","type":"uint256"},{"internalType":"uint256","name":"_migrateAmount","type":"uint256"}],"name":"migratePeripheryRewardToHook","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_nftIndex","type":"uint256"},{"internalType":"uint256","name":"_nftId","type":"uint256"}],"name":"nftStake","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_nftIndex","type":"uint256"},{"internalType":"uint256","name":"_nftId","type":"uint256"}],"name":"nftUnstake","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"nfts","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"nftsCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nftsIndexOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"periphery","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"peripheryCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"peripheryIndexOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"peripheryOwner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_peripheryIndex","type":"uint256"},{"internalType":"uint256","name":"_nftIndex","type":"uint256"},{"internalType":"uint256","name":"_nftId","type":"uint256"}],"name":"revokeStakedUseByPeriphery","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"rewardTokenIndex","type":"uint256"},{"internalType":"uint256","name":"peripheryIndex","type":"uint256"}],"name":"rewardTokenUseByPeriphery","outputs":[{"internalType":"uint256","name":"rewardTokenAmount","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"rewardTokens","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"rewardTokensCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"rewardTokensIndexOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_peripheryIndex","type":"uint256"},{"internalType":"address","name":"_claimedTo","type":"address"},{"internalType":"uint256","name":"_rewardTokenIndex","type":"uint256"},{"internalType":"uint256","name":"_claimedAmount","type":"uint256"}],"name":"sendRewardFromPeriphery","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_feeCollector","type":"address"},{"internalType":"uint256","name":"_feeAmount","type":"uint256"}],"name":"setFeeForCreatePeriphery","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_hookAddr","type":"address"}],"name":"setHook","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_nftAddr","type":"address"}],"name":"setNft","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_peripheryAddr","type":"address"},{"internalType":"address","name":"_peripheryOwner","type":"address"}],"name":"setPeriphery","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_peripheryIndex","type":"uint256"},{"internalType":"address","name":"_newOwner","type":"address"}],"name":"setPeripheryOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_peripheryIndex","type":"uint256"},{"internalType":"uint256","name":"_rewardTokenIndex","type":"uint256"},{"internalType":"uint256","name":"_rewardTokenAmount","type":"uint256"}],"name":"setPeripheryReward","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_rewardTokenAddr","type":"address"}],"name":"setRewardToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"nftIndex","type":"uint256"},{"internalType":"uint256","name":"nftId","type":"uint256"}],"name":"stakedData","outputs":[{"internalType":"address","name":"nftOwnerOf","type":"address"},{"internalType":"uint256","name":"nftStakedAt","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"peripheryIndex","type":"uint256"},{"internalType":"uint256","name":"nftIndex","type":"uint256"},{"internalType":"uint256","name":"nftId","type":"uint256"}],"name":"stakedUseByPeriphery","outputs":[{"internalType":"uint256","name":"timestamp","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_peripheryIndex","type":"uint256"},{"internalType":"uint256","name":"_nftIndex","type":"uint256"},{"internalType":"uint256","name":"_nftId","type":"uint256"},{"internalType":"address","name":"_robber","type":"address"}],"name":"stealNftStakedFromPeriphery","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_peripheryIndex","type":"uint256"},{"internalType":"uint256","name":"_nftIndex","type":"uint256"},{"internalType":"uint256","name":"_nftId","type":"uint256"}],"name":"syncNftStakedAtFromPeriphery","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"}]')  # Replace with actual FieldV2 ABI JSON
FieldV2Address = "0x4b958647b3D5240587843C16d4dfC13B19de2671"  # Replace with actual FieldV2 contract address

# Set up the account and private key for signing transactions
account = "Your Address"
private_key = "Your PrivateKey"

# Create contract instances
erc721_contract = w3.eth.contract(address=ERC721Address, abi=ERC721ABI)
fieldv2_contract = w3.eth.contract(address=FieldV2Address, abi=FieldV2ABI)

# Read the Token IDs from the CSV file
token_ids = []
with open("token_ids.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        token_ids.append(int(row[0]))  # Assuming the Token ID is the first column

# Function to approve all tokens to the FieldV2 contract
def approve_all_tokens():
    nonce = w3.eth.get_transaction_count(account)  # Get the current nonce
    approve_all_txn = erc721_contract.functions.setApprovalForAll(FieldV2Address, True).build_transaction({
        'chainId': 8899,  # Mainnet, change if using testnet
        'gas': 200000,
        'gasPrice': w3.to_wei('20', 'gwei'),
        'nonce': nonce,
    })
    signed_txn = w3.eth.account.sign_transaction(approve_all_txn, private_key)
    txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print(f"Approve all transaction sent: {txn_hash.hex()}")
    
    # Increment the nonce after the transaction is sent
    return txn_hash, nonce + 1

# Function to stake NFT tokens
def stake_nfts(nonce):
    for token_id in token_ids:
        nft_index = fieldv2_contract.functions.nftsIndexOf(FieldV2Address).call()
        nft_stake_txn = fieldv2_contract.functions.nftStake(2, token_id).build_transaction({
            'chainId': 8899,
            'gas': 200000,
            'gasPrice': w3.to_wei('1', 'gwei'),
            'nonce': nonce,
        })
        signed_txn = w3.eth.account.sign_transaction(nft_stake_txn, private_key)
        txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        print(f"NFT stake transaction sent for token {token_id}: {txn_hash.hex()}")
        
        # Increment the nonce after the transaction is sent
        nonce += 1

    return nonce

# Function to allow staked NFTs for use by periphery
def allow_staked_use(nonce):
    for token_id in token_ids:
        nft_index = fieldv2_contract.functions.nftsIndexOf(FieldV2Address).call()
        allow_staked_txn = fieldv2_contract.functions.allowStakedUseByPeriphery(2, nft_index, token_id).build_transaction({
            'chainId': 8899,
            'gas': 200000,
            'gasPrice': w3.to_wei('1', 'gwei'),
            'nonce': nonce,
        })
        signed_txn = w3.eth.account.sign_transaction(allow_staked_txn, private_key)
        txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        print(f"Allow staked transaction sent for token {token_id}: {txn_hash.hex()}")
        
        # Increment the nonce after the transaction is sent
        nonce += 1

    return nonce

# Run the functions
def main():
    # Approve all tokens to FieldV2 contract
    print("Approving all tokens...")
    txn_hash, nonce = approve_all_tokens()

    # Stake NFTs
    print("Staking NFTs...")
    nonce = stake_nfts(nonce)

    # Allow staked NFTs for periphery use
    print("Allowing staked NFTs for periphery use...")
    nonce = allow_staked_use(nonce)

if __name__ == "__main__":
    main()
