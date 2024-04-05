#include <iostream>
using namespace std;

int main(){
  int N;
  cout << "数値を入力してください" << endl;
  cin >> N;
  for(int i=2; i<=N; i+=2){
    cout << i << endl;
  }

  return 0;

}
