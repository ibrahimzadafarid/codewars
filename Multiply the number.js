// ! Multiply the number https://www.codewars.com/kata/5708f682c69b48047b000e07
// ! 8KYU
function multiply(number) {
  const power = Math.abs(number).toString().length;
  return number * 5 ** power;
}

console.log(multiply(3));
console.log(multiply(10));
console.log(multiply(200));
console.log(multiply(0));
console.log(multiply(-3));
