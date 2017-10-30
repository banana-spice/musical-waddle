var _ = require('lodash');
//consle.log(Math.floor(Math.random()*10));
var theDate = new Date();
//console.log(theDate.getDay(), theDate.getMonth());

//var person = new Object;
//var Inventory = {};

var Dog = {
    name: "Odie",
    age: 6
};

//console.log(Dog.name);
//console.log(Dog["age"]);

/*for (var prop in Dog){
    console.log(prop);
}

_.forEach(Dog, value =>{
    console.log(value);
});

//create an object Owner that has a name and an age

var Owner = {
    name: "Jon",
    age: 32,
    cat: {
        name: "Garfield",
        color: "Orange"
    },
    dog: {
        name: "Odie",
        color: "Yellow"
    }
};

console.log(Owner.name);
console.log(Owner.cat.name);
console.log(Owner.dog.color);

Owner.lName = "Arbuckle";
console.log(Owner.lName);

var Dog = {
    name: "Jd",
    breed: "lab",
    makeNoise: (noise, elses) => {
        //console.log("I can " + noise + " and " + elses);
        console.log(`I can ${noise} and ${elses}`);
    },
    run(){
        console.log("I run fast ...");
    }
};

Dog.makeNoise("Woof!", "Bark!");
Dog.run();*/

function Animal(species, name){
    ///statements
    this.type = species;
    this.title = name;
    this.noiseMaker = sound=>{
        console.log(`I ${sound}!`)
    }
    this.run = running;
};

var dog = new Animal("dog", "Sgt");
var cat = new Animal("cat", "Chuck");
console.log(`My name is ${dog.title} and I am a ${dog.type}`);
console.log(cat.type);

//after the method is added
dog.noiseMaker("bark bark");
cat.noiseMaker("mew purrrrrr");
cat.run();

//another method for my constructor
function running(){
    console.log(`${this.title} is very fast!`);
};
