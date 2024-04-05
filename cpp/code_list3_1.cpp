#include <iostream>
using namespace std;

int main(){

  //配列の要素数
  const int DATA_NUM = 10;

  int point[DATA_NUM] = {85, 72, 63, 45, 100, 98, 52, 88, 74, 65};
  int sum; //合計点
  double avarage; //平均点
  int i;

  sum = 0;
  for(i=0; i<DATA_NUM; i++){
    sum += point[i];
  }

 avarage = (double)sum/DATA_NUM;
 cout << "平均点：" << avarage << endl;
 return 0;

}