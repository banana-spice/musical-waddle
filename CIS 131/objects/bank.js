var account = {
    name: "Alex",
    balance: 0,
    credit: 1,
    describe(){
        return `Owner: ${this.name}, balance ${this.balance}`;
    }
};

account.credit += 250;
account.credit -= 80;

console.log(account.describe());