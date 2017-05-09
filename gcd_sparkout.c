#include <stdio.h>
#include <stdbool.h>

int main(void)
{
 int y1;
 int y2;
 int res;
 int yout;
 int i;
 bool sT0_6;
 int sT1_8;
 bool sT2_8;
 int sT3_9;
 int sT4_9;
 int sT5_17;
 int sT6_17;
 int sT7_19;
 int sT8_20;
 int sT9_22;
 bool sT10_19;
 int sT11_8;
 int sT12_17;
 bool sT13_17;
 int sT14_11;
 int sT15_11;
 int sT16_24;
 y1 = 10;
 y2 = 545;
 res = 1;
 i = 0;
  do{
    sT8_20 = (y1 - y2);
    sT9_22 = (y2 - y1);
    sT0_6 = (y1 != y2);
    sT10_19 = (y1 > y2);
    sT11_8 = (y1 % 2);
    sT12_17 = (y2 % 2);
    if(sT0_6){
      i = (i + 1);
      sT2_8 = (sT11_8 == 0);
      sT13_17 = (sT12_17 == 0);
      sT14_11 = (res * 2);
      sT15_11 = (y1 / 2);
      sT1_8 = sT11_8;
      if(sT2_8){
        if(sT13_17){
          y2 = (y2 / 2);
          sT3_9 = sT12_17;
          sT4_9 = sT13_17;
          res = sT14_11;
          y1 = sT15_11;
         }else{
          sT3_9 = sT12_17;
          sT4_9 = sT13_17;
          y1 = sT15_11;
         }
       }else{
        if(sT13_17){
          y2 = (y2 / 2);
          sT5_17 = sT12_17;
          sT6_17 = sT13_17;
         }else{
          if(sT10_19){
            sT5_17 = sT12_17;
            sT6_17 = sT13_17;
            sT7_19 = sT10_19;
            y1 = sT8_20;
           }else{
            sT5_17 = sT12_17;
            sT6_17 = sT13_17;
            sT7_19 = sT10_19;
            y2 = sT9_22;
           }
         }
       }
     }else{
     	break;
     }
   }while(1);

  sT16_24 = (res * y1);
  res = sT16_24;
  yout = sT16_24;
  printf("value of a: %d\n", yout);
  return   0;

}

