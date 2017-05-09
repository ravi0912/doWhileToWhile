
#include <stdio.h>


int main(void)
{
 int n=8;
 int a[8];
 int min;
 int i;
 int j;
 int temp;
 int j_star;
 int sT0_13;
 int sT1_13;
 int sT2_15;
 int sT3_15;
 int sT4_16;
 int sT5_16;
 int sT6_15;
 int sT7_16;
 int sT8_16;
 int sT9_15;
 int sT10_15;
 int sT11_15;
 int sT12_15;
 int sT13_14;
 int sT14_15;

  a[0] = 23;
  i = 0;
  a[1] = 11;
  a[2] = 27;
  a[3] = 19;
  a[4] = 12;
  a[5] = 10;
  a[6] = 31;
  a[7] = 7;
  min = a[0];
  do{
    sT0_13 = n - 2;
    sT12_15 = i + 1;
    sT13_14 = a[i];
    sT14_15 = n - 1;
    sT1_13 = i <= sT0_13;
    if (sT1_13){
      min = sT13_14;
      j_star = i;
      j = sT12_15;
      sT10_15 = sT14_15;
      sT2_15 = sT14_15;
      sT9_15 = sT14_15;
      temp = sT13_14;
      do{
        sT11_15 = n - 1;
        sT6_15 = j + 1;
        sT3_15 = j <= sT2_15;
        sT7_16 = a[j];
        sT8_16 = sT7_16 < min;
        if (sT3_15){
          if (sT8_16){
            sT4_16 = sT7_16;
            sT5_16 = sT8_16;
            min = sT7_16;
            j_star = j;
            j = sT6_15;
            sT2_15 = sT9_15;
            sT9_15 = sT11_15;
           }else{
            sT4_16 = sT7_16;
            sT5_16 = sT8_16;
            j = sT6_15;
            sT2_15 = sT9_15;
            sT9_15 = sT11_15;
           }
         }else
          break;
       }while (1);

      a[i] = sT13_14;
      i = sT12_15;
      a[j_star] = sT13_14;
     }
    else
      break;
   }while (1);
   printf("value of min: %d\n", a[0]);
   printf("value of min: %d\n", a[1]);
   printf("value of min: %d\n", a[2]);
   printf("value of min: %d\n", a[3]);
   printf("value of min: %d\n", a[4]);
   printf("value of min: %d\n", a[5]);
   printf("value of min: %d\n", a[6]);
  return 0;

}
