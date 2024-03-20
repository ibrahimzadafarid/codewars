// ! All Star Code Challenge #18  https://www.codewars.com/kata/5865918c6b569962950002a1
// ! 8KYU

export function strCount(str: string, letter: string): number {
  let count = 0;
  for (const currentLetter of str) {
    if (currentLetter === letter) {
      count++;
    }
  }
  return count;
}
