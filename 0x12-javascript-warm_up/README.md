# 0x12-javascript-warm_up

#### process.argv in javascript is an array which stores the command line arguments as an array of strings.
#### The String.repeat((Number)) method takes a number as a parameter and repeat specific string according to this number.


### This code contains some methods to study!   

const arr = process.argv.slice(2).map(Number);
const second = arr.sort(function (a, b) {
return b - a;})[1]

#### The array.slice(start, end) : This methods take start index and return the array from this index to the end if i didn't specify end Index.

#### The .map: This method converts the elements of an array to another datatype

#### The array.sort : This method is used to sort the array in the above context, The method will sort the array in descending manner.

## Module
### We use export.(function) = function{}; to make specific function accessible #### by other files, for example if we have a file called file.js, So dealing with this in this file will be like:
// file.js
add = require('./add.js').add;
//add.js
export.add = function(a, b) {return a + b;};
