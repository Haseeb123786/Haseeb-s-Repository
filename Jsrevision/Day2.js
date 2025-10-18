let a =45
console.log(typeof a);
console.log(a);
//Primitve data 

//there are 7 types of primitive data
//1. Number
//2. String
//3. Boolean
//4. null
//5. undefined
//6. Symbol
//7. BigInt

//Reference (Non primitive) data types
//1. Object
//2. Array
//3. Function

const score = false //Boolean data type
const scoreValue = 34.5 //Number data type

let username; //undefined data type
const id =Symbol("1234") //Symbol data type
const anotherid =Symbol("1234") //Symbol data type
console.log(id==anotherid); //false

const bigNumber = BigInt(1234567890123456789012345678901234567890) //BigInt data type

const heros = ["shaktiman","nagraj","doga"] //Array data type
const myObj = {
    name:"Raju",
    age:24,
    hobbies:["coding","reading","gaming"]
} //Object data type

const myFunction = function(){
    console.log("Hello World");
} //Function data type 

