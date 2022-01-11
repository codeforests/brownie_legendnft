from typing import Container
from brownie import network, config
import pytest

@pytest.fixture
def legendNFT(LegendNFT, accounts):
    contract = LegendNFT.deploy(
        {"from" : accounts[0]}, 
        publish_source=config["networks"][network.show_active()].get("verify")
    )
    return contract

def test_total_init_supply(legendNFT):    
    init_supply = 1000000
    assert legendNFT.totalSupply() == init_supply

def test_make_nft(legendNFT):
    tx = legendNFT.makeLegendNFT()
    tx.wait(1)
    assert legendNFT.getTotalNFTsMintedSoFar() == 1


