from brownie import LegendNFT, network, config
from scripts.utils import get_account


def deploy_contract():
    account = get_account()
    legend_contract = LegendNFT.deploy(
        {"from" : account}, 
        publish_source=config["networks"][network.show_active()].get("verify")
    )
    print("contract has been deployed successfully to :", legend_contract.address)

    return legend_contract



def main():
    deploy_contract()

