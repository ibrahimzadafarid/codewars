// ! Sum without highest and lowest number https://www.codewars.com/kata/576b93db1129fcf2200001e6
// ! 8KYU
export function sumArray(array: number[] | null): number {
  if (!array || array.length <= 1) return 0;
  array.sort((a, b) => a - b);

  return array
    .filter((_, i) => i !== 0 && i !== array.length - 1)
    .reduce((acc, el) => acc + el, 0);
}

console.log(sumArray([6, 2, 1, 8, 10]));
console.log(sumArray([6, 0, 1, 10, 10]));
