// const name_order = function(arr, name){
//   for(let i = 0; i < arr.length; i++){
//     if(name === arr[i]) return i;
//   }
  
//   return -1;
// }

// const collection = function(records){
//   let names = new Set();
  
//   for(let i = 0; i < records.length; i++){
//     names.add(records[i][0]);
//   }
  
//   return names;
// }


/*

We are working on a security system for a badged-access room in our company's building.

Given an ordered list of employees who used their badge to enter or exit the room, write a function that returns two collections:

1. All employees who didn't use their badge while exiting the room - they recorded an enter without a matching exit. (All employees are required to leave the room before the log ends.)

2. All employees who didn't use their badge while entering the room - they recorded an exit without a matching enter. (The room is empty when the log begins.)

Each collection should contain no duplicates, regardless of how many times a given employee matches the criteria for belonging to it.

records1 = [
  ["Paul",     "enter"],
  ["Pauline",  "exit"],
  ["Paul",     "enter"],
  ["Paul",     "exit"],
  ["Martha",   "exit"],
  ["Joe",      "enter"],
  ["Martha",   "enter"],
  ["Steve",    "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "enter"],
  ["Joe",      "enter"],
  ["Curtis",   "exit"],
  ["Curtis",   "enter"],
  ["Joe",      "exit"],
  ["Martha",   "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "exit"],
  ["Joe",      "enter"],
  ["Joe",      "enter"],
  ["Martha",   "exit"],
  ["Joe",      "exit"],
  ["Joe",      "exit"] 
]

Expected output: ["Steve", "Curtis", "Paul", "Joe"], ["Martha", "Pauline", "Curtis", "Joe"]

Other test cases:

records2 = [
  ["Paul", "enter"],
  ["Paul", "exit"],
]

Expected output: [], []

records3 = [
  ["Paul", "enter"],
  ["Paul", "enter"],
  ["Paul", "exit"],
  ["Paul", "exit"],
]

Expected output: ["Paul"], ["Paul"]

records4 = [
  ["Raj", "enter"],
  ["Paul", "enter"],
  ["Paul", "exit"],
  ["Paul", "exit"],
  ["Paul", "enter"],
  ["Raj", "enter"],
]

Expected output: ["Raj", "Paul"], ["Paul"]

All Test Cases:
mismatches(records1) => ["Steve", "Curtis", "Paul", "Joe"], ["Martha", "Pauline", "Curtis", "Joe"]
mismatches(records2) => [], []
mismatches(records3) => ["Paul"], ["Paul"]
mismatches(records4) => ["Raj", "Paul"], ["Paul"]

n: length of the badge records array
*/
"use strict";

const records1 = [
  ["Paul", "enter"],
  ["Pauline", "exit"],
  ["Paul", "enter"],
  ["Paul", "exit"],
  ["Martha", "exit"],
  ["Joe", "enter"],
  ["Martha", "enter"],
  ["Steve", "enter"],
  ["Martha", "exit"],
  ["Jennifer", "enter"],
  ["Joe", "enter"],
  ["Curtis", "exit"],
  ["Curtis", "enter"],
  ["Joe", "exit"],
  ["Martha", "enter"],
  ["Martha", "exit"],
  ["Jennifer", "exit"],
  ["Joe", "enter"],
  ["Joe", "enter"],
  ["Martha", "exit"],
  ["Joe", "exit"],
  ["Joe", "exit"]
];

const records2 = [
  ["Paul", "enter"],
  ["Paul", "exit"]
];

const records3 = [
  ["Paul", "enter"],
  ["Paul", "enter"],
  ["Paul", "exit"],
  ["Paul", "exit"]
];

const records4 = [
  ["Raj", "enter"],
  ["Paul", "enter"],
  ["Paul", "exit"],
  ["Paul", "exit"],
  ["Paul", "enter"],
  ["Raj", "enter"]
];



// const remaining = function(records){
//   let remains = new Set();
//   for(let i = 0; i < records.length; i++){
//     if(records[i][1] === 'enter' ){
//       remains.add(records[i][0])
//     } else {
//       remains.delete(records[i][0]);
//     }
//   }
//   return remains;
// }


const collections = function(records){
  let hash = {}
  let values = {
    'enter': 1,
    'exit': -1
  }
  
  let col1 = [];
  let col2 = [];
  
  for(let i = 0; i < records.length; i++){
    if(hash[records[i][0]] === undefined) hash[records[i][0]] = values[records[i][1]]
    else{
      hash[records[i][0]] += values[records[i][1]]
    }
  }
  
//   let vals = Object.values(hash)
//   for(let i = 0; i < hash.entries )
}








