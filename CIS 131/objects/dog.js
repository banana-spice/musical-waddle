// TODO: create the dog object here

var dog = {
    name: "Fang",
    species: "boarhoud",
    size: 75,
    bark(){
        return "Grr! Grr!"
    }
};

console.log(`${dog.name} is a ${dog.species} dog measuring ${dog.size}`);
console.log(`Look, a cat! ${dog.name} barks: ${dog.bark()}`);
