// ! Find Multiples of a Number https://www.codewars.com/kata/58ca658cc0d6401f2700045f
// !8KYU

export function findMultiples(integer: number, limit: number): number[] {
  const arr: number[] = [integer];
  let newEl = integer * 2;
  while (newEl <= limit) {
    arr.push(newEl);
    newEl += integer;
  }

  return arr;
}
