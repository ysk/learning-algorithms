#include <iostream>
#include <iomanip>

using namespace std;

int main(){
  int money;
  int price;

  cout << "所持金を入力してください：";
  cin >> money;

  while (true)
  {
    cout << "残金：" << money << "円" << endl;
    cout << "買い物した金額：";
    cin >> price;
    money -= price;
    if(money <= 0){
      break;
    }
  }

  //買い物が終了したことを示す
  cout << "買い物終了！" << endl;

  return 0;

}