// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract AuraIntelVault {
    address public owner;
    mapping(address => uint256) public balances;

    constructor() {
        owner = msg.sender; // El 100% del control es tuyo
    }

    // Sugerencia 100%: Solo el dueño puede retirar
    modifier onlyOwner() {
        require(msg.sender == owner, "Aura Intel: Acceso denegado al 100%");
        _;
    }

    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw(uint256 _amount) public onlyOwner {
        require(address(this).balance >= _amount, "Saldo insuficiente");
        payable(owner).transfer(_amount);
    }
}
