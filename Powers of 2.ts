// !Powers of 2 https://www.codewars.com/kata/57a083a57cb1f31db7000028
// !8KYU

export function powersOfTwo(n: number): number[] {
  return Array.from({ length: n + 1 }, (_, i) => 2 ** i);
}
