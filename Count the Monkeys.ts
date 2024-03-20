// ! Count the Monkeys! https://www.codewars.com/kata/56f69d9f9400f508fb000ba7
// ! 8KYU

export function monkeyCount(n: number): number[] {
  let arr: number[] = [];
  for (let i = 1; i <= n; i++) {
    arr.push(i);
  }
  return arr;
}
