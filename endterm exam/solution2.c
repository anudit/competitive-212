#include<stdio.h>
#include<limits.h>

int max(int a, int b) {
  return (a > b) ? a : b;
}

int calcamt(int n, int amts[]) {
  int val[n + 1];
  val[0] = 0;
  int i, j;

  for (i = 1; i <= n; i++) {
    int max_val = INT_MIN;
    for (j = 0; j < i; j++)
      max_val = max(max_val, amts[j] + val[i - j - 1]);
    val[i] = max_val;
  }

  return val[n];
}

int main() {

  int n;
  scanf("%d", & n);

  int arr[n];

  for (int i = 0; i < n; ++i) {
    scanf("%d", & arr[i]);
  }

  printf("%d", calcamt(n, arr));
  return 0;
}
