// ! Counting sheep https://www.codewars.com/kata/54edbc7200b811e956000556
// ! 8KYU
export function countSheeps(arrayOfSheep: (boolean | undefined | null)[]) {
    return arrayOfSheep.filter(Boolean).length;
    
  }