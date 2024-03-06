// ! Find out whether the shape is a cube https://www.codewars.com/kata/58d248c7012397a81800005c
// ! 8KYU
export function cubeChecker(volume: number, side: number): boolean {
  if (volume <= 0 || side <= 0) return false;
  return volume === side ** 3;
}

console.log(cubeChecker(27, 3));
