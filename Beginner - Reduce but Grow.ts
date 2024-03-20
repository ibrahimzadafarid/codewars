// ! Beginner - Reduce but Grow https://www.codewars.com/kata/57f780909f7e8e3183000078
// !8KYU

export function grow(arr: number[]): number {
   const num = arr.reduce((accumulator, currentValue) => accumulator * currentValue);
   return num;
  }